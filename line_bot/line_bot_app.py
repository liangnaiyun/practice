from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('Puwfk+Wgv0k3jeh+c5xXeAkGa9OntxYQNyfgPfQtsnLCH9KuShjfe89TeF6DrUPJjP8fSUf9xuj60eCPDf5nn7E8VMRdSjdOktH7D2BHpzQBJMzKU+CYw/QiDay7emotxNRVCbH9BM4B7iAzfdlTOQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('588acad555d0d4529f5a9a77e7a57b31')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()