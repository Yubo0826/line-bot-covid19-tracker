from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('Hm/Yzh8UEPKS9i2vKrlWj6dakJf4Y614YYM6fVqbfnV10jCLLoM+uwMM22viqbNvJvYsou/fGMNDo8dXct23YS1cG7e7Qb2mDWPTjNICCqFHhBdOFhVYF39FNX1EaY0SXqImqJ1XYWsD2+8bShOaGQdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('f9219d0bf6d9489bc0e31b7bb4f5db0a')

# 監聽所有來自 /callback 的 Post Request
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
        abort(400)
    return 'OK'

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = ImagemapSendMessage(
        base_url = "https://i.imgur.com/QFPjwp9.jpg",
        alt_text = "這是組圖訊息",
        base_size = BaseSize(height=641,width=508),
        action=[
            URIImagemapAction(
                link_uri='https://tw.shop.com/%E4%BA%94%E6%9C%88%E8%8A%B1%E6%8A%BD%E5%8F%96%E8%A1%9B%E7%94%9F%E7%B4%99-1477123666-p+.xhtml',
                area=ImagemapArea(
                    x=0,y=0,width=254,height=641
                )
            ),
            MessageImagemapAction(
                text='五月花衛生紙',
                area=ImagemapArea(
                    x=254,y=0,width=254,height=641
                )
            )
        ]
    )
    #event.message.text就是用戶傳來的文字訊息
    line_bot_api.reply_message(event.reply_token, message)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
