from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from msrest.authentication import CognitiveServicesCredentials
from PIL import Image
import requests
import io

app = Flask(__name__)

# 設定 Line Bot 金鑰和端點
line_bot_api = LineBotApi('apikey')
handler = WebhookHandler('secret')

# 設定 Azure 資源金鑰和端點
subscription_key = "key"
endpoint = "endpoint"
computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
    reply_text = process_image(event.message.id)
    line_bot_api.reply_message(event.reply_token, TextSendMessage(text=reply_text))

def process_image(message_id):
    # 取得圖片 URL
    image_url = line_bot_api.get_message_content(message_id).content_url

    # 下載圖片
    response = requests.get(image_url)
    image = Image.open(io.BytesIO(response.content))

    # 使用 Computer Vision 服務進行 OCR
    result = computervision_client.read_in_stream(image.tobytes(), raw=True)

    # 取得結果
    operation_location = result.headers["Operation-Location"]
    operation_id = operation_location.split("/")[-1]

    while True:
        result = computervision_client.get_read_result(operation_id)
        if result.status not in [OperationStatusCodes.running]:
            break

    # 輸出提取的文字
    extracted_text = ""
    for region in result.analyze_result.read_results:
        for line in region.lines:
            extracted_text += " ".join([word.text for word in line.words]) + "\n"

    return extracted_text

if __name__ == "__main__":
    app.run(debug=True)