#這個檔案的作用是：建立功能列表

#===============這些是LINE提供的功能套組，先用import叫出來=============
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *
#===============LINEAPI=============================================

#以下是本檔案的內容本文

#1.建立旋轉木馬訊息，名為function_list(未來可以叫出此函數來使用)
#function_list的括號內是設定此函數呼叫時需要給函數的參數有哪些

def function_list():
    message = TemplateSendMessage(
        alt_text='功能列表',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    #模塊1上面的圖片要用哪一張，透過連結(URL)的方式給機器人
                    thumbnail_image_url='https://example.com/item1.jpg',
                    #模塊1的標題名稱
                    title='舉例最新優惠',
                    #模塊1的副標題或標題下的文字內容
                    text='馬上獲得最新優惠資訊',
                    actions=[
                        MessageTemplateAction(
                            #讓用戶丟出指定訊息的按鈕名稱
                            label='點我點我',
                            #按下去之後用戶會丟出什麼東西
                            text='我想瞭解目前最新優惠'
                        ),
                        URITemplateAction(
                            #讓用戶進入指定連結的按鈕名稱
                            label='進入看更多',
                            #讓用戶進入什麼連結或更多指令
                            uri='https://tw.shop.com/'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://example.com/item2.jpg',
                    title='this is menu2',
                    text='description2',
                    actions=[
                        PostbackTemplateAction(
                            label='postback2',
                            text='postback text2',
                            data='action=buy&itemid=2'
                        ),
                        MessageTemplateAction(
                            label='message2',
                            text='message text2'
                        ),
                        URITemplateAction(
                            label='uri2',
                            uri='http://example.com/2'
                        )
                    ]
                )
            ]
        )
    )
    return message