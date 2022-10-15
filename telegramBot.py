import telebot
import cv2
tokenName = telebot.TeleBot("5619962504:AAFarPrHH4YUUvR2I-9LUWCiRkZGs3dvu_4")

@tokenName.message_handler(commands=['start'])
def start(message):
    mess = f'hey, {message.from_user.last_name}'
    tokenName.send_message(message.chat.id, mess)

@tokenName.message_handler(commands=['info'])
def sendInfo(message):
    data = message.photo
    if data is None:
        mess = 'Sorry, bro, but not today'
        tokenName.send_message(message.chat.id, mess)
    else:
        tokenName.send_message(message.chat.id, data)

@tokenName.message_handler(content_types=['text'])
def anyInput(message):
    mess = 'Sorry, bro, but not today'
    tokenName.send_message(message.chat.id, mess)



    

@tokenName.message_handler(content_types=['photo'])
def GrayScale(message):
    image = message.photo[-1].file_id
    #image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    tokenName.send_message(message.chat.id, image)

tokenName.polling(non_stop=True)


