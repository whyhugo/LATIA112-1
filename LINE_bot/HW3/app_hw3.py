import sys
import configparser

# Azure Text Analytics
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

from flask import Flask, request, abort
from linebot.v3 import (
    WebhookHandler
)
from linebot.v3.exceptions import (
    InvalidSignatureError
)
from linebot.v3.webhooks import (
    MessageEvent,
    TextMessageContent,
)
from linebot.v3.messaging import (
    Configuration,
    ApiClient,
    MessagingApi,
    ReplyMessageRequest,
    TextMessage
)

#Config Parser
config = configparser.ConfigParser()
config.read('config.ini')

#Config Azure Analytics
credential = AzureKeyCredential(config['AzureLanguage']['API_KEY'])

app = Flask(__name__)

channel_access_token = config['Line']['CHANNEL_ACCESS_TOKEN']
channel_secret = config['Line']['CHANNEL_SECRET']
if channel_secret is None:
    print('Specify LINE_CHANNEL_SECRET as environment variable.')
    sys.exit(1)
if channel_access_token is None:
    print('Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.')
    sys.exit(1)

handler = WebhookHandler(channel_secret)

configuration = Configuration(
    access_token=channel_access_token
)

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # parse webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@handler.add(MessageEvent, message=TextMessageContent)
def message_text(event):
    sentiment_result = azure_sentiment(event.message.text)
    with ApiClient(configuration) as api_client:
        line_bot_api = MessagingApi(api_client)
        line_bot_api.reply_message_with_http_info(
            ReplyMessageRequest(
                reply_token=event.reply_token,
                messages=[TextMessage(text=sentiment_result)]
            )
        )

def azure_sentiment(user_input):
    text_analytics_client = TextAnalyticsClient(
        endpoint=config['AzureLanguage']['END_POINT'], 
        credential=credential)
    documents = [user_input]
    response = text_analytics_client.analyze_sentiment(
        documents, 
        show_opinion_mining=True,
        language="zh-Hant")
    print(response)
    docs = [doc for doc in response if not doc.is_error]
    key_phrases_response = text_analytics_client.extract_key_phrases(documents, language="zh-Hant")
    key_phrases_docs = [doc for doc in key_phrases_response if not doc.is_error]
    info = ""
    if docs:
        result = docs[0].sentiment
        scores = docs[0].confidence_scores
        if result == "positive":
            info = f"【正向 😀】\n正向分數為 {scores.positive:.2f}\n"
        elif result == "neutral":
            info = f"【中性 🗿】\n中性分數為 {scores.neutral:.2f}\n"
        elif result == "negative":
            info = f"【負向 😟】\n負向分數為 {scores.negative:.2f}\n"
    if key_phrases_docs and key_phrases_docs[0].key_phrases:
        key_phrases = key_phrases_docs[0].key_phrases
        key_phrases_info = "主詞：" + "、".join(key_phrases)
    else:
        key_phrases_info = "主詞：無～"
    info += key_phrases_info
    return info

    '''
    for idx, doc in enumerate(docs):
        print(f"Document text : {documents[idx]}")
        print(f"Overall sentiment : {doc.sentiment}")
    return docs[0].sentiment
    '''

if __name__ == "__main__":
    app.run()