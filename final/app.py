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
import csv
import openai  # Import the OpenAI library

app = Flask(__name__)

# Set Line Bot keys and endpoints
line_bot_api = LineBotApi('your_channel_access_token')
handler = WebhookHandler('your_channel_secret')

# Set Azure keys and endpoints
subscription_key = "your_subscription_key"
endpoint = "your_endpoint"
computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))

# Set OpenAI API key
openai.api_key = 'your_openai_api_key'

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
    image_url = line_bot_api.get_message_content(message_id).content_url
    response = requests.get(image_url)
    image = Image.open(io.BytesIO(response.content))
    result = computervision_client.read_in_stream(image.tobytes(), raw=True)

    operation_location = result.headers["Operation-Location"]
    operation_id = operation_location.split("/")[-1]

    while True:
        result = computervision_client.get_read_result(operation_id)
        if result.status not in [OperationStatusCodes.running]:
            break

    extracted_text = ""
    for region in result.analyze_result.read_results:
        for line in region.lines:
            extracted_text += " ".join([word.text for word in line.words]) + "\n"

    # Find the most similar video link using OpenAI API
    similar_video_link = find_most_similar_video(extracted_text)
    return f"你輸入的題目:\n{extracted_text}\n\n推薦給你的學習資源:\n{similar_video_link}"

def find_most_similar_video(ocr_text):
    # Use OpenAI API to find the most similar video link
    junyi_data = read_junyiacademy()
    prompt = f"請幫我根據題目：「{ocr_text}」, 並且從 {junyi_data} 的單元與課程名稱欄位中尋找最相關的網址"
    responses = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.7
    )

    # Extract the chosen completion
    chosen_completion = responses['choices'][0]['text'].strip()

    # Find the most similar video link based on the chosen completion
    most_similar_video_link = find_video_link(junyi_data, chosen_completion)

    return most_similar_video_link

def find_video_link(junyi_data, chosen_completion):
    for row in junyi_data:
        if chosen_completion.lower() in row[1].lower():
            return row[2]

    return "No similar video link found."

def read_junyiacademy():
    data = {}
    with open(r'D:\programing\swiftx\NTNU\LATIA112-1\均一高中生物.csv', 'r', encoding='utf-8-sig') as file:
        junyi_data = csv.DictReader(file)
        count = 0
        for row in junyi_data:
            data[count] = row
            count += 1
    return data

if __name__ == "__main__":
    app.run(debug=True)
