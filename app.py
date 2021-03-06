from flask import Flask, request, abort
from flask.logging import create_logger

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, LocationSendMessage
)
from myFunc import fetch,update

import urllib.request as req
import bs4
import os, sys, logging

app = Flask(__name__)
log = create_logger(app)

# Channel Access Token
line_bot_api = LineBotApi('iv8CyrPQPdvtwvIANIpcFw2CZ8ZlD21Y1FPwQpHwYdT4vAkPggLRsFku36lzGt0EOuUXOhRutpxYau4VuGl8qkrU5kmnGQRH0cXhzHLtISsFzBqq/40J3oynErZ4nVetofkyMpC+9eoxGROSMGg1vQdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('5955966714c4c4ab6f82a7619f93280b')

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    log.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if 'update' in event.message.text:
        notice=update()
        notice_text=TextSendMessage(text=notice)
        line_bot_api.reply_message(event.reply_token,notice_text)
    else:
        covid_text=fetch(event.message.text)
        covid_message=TextSendMessage(text=covid_text)
        line_bot_api.reply_message(event.reply_token, covid_message)


import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
