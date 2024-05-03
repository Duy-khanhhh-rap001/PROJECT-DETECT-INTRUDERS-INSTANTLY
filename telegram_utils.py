import telegram

def send_telegram(photo_path="alert.png"):
    try:
        my_token = "6384445491:AAH6hoe-1uyyIG3F6plwoaHS471a7gDLgcU"
        bot = telegram.Bot(token=my_token)
        bot.sendPhoto(chat_id="khanhpython", photo=open(photo_path, "rb"), caption="Có xâm nhập, nguy hiêm!")
    except Exception as ex:
        print("Can not send message telegram ", ex)

    print("Send sucess")