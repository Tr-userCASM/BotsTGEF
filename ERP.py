#19-20 марта 2:22.Вернулся к основе в vim   
#если чисто как есь 2 недели ебался сначала
#айограмм,потрм решил телебо и 2 дня
#с исправление синтаксиса пишу бота
#добавляю  ReadMe запись 24 января
#28.01.Исправляю ошибки запуска бота страдая
#31.01.Бот закончил,остался биттсч за руссификатор

import os
import time
from dotenv import load_dotenv
import telebot
from telebot import types
import logging
import http.client
import decouple
from decouple import config

http.client.HTTPConnection.debuglevel = 1

load_dotenv()

ECHO1_BOT_TOKEN = os.environ.get("ECHO1_BOT_TOKEN")
ECHO1_BOT_TOKEN = config('ECHO1_BOT_TOKEN', default=None)

logging.basicConfig(level=logging.DEBUG)
print(f"🔍 Bot PID: {os.getpid()}")

print(f"!Token check: {RP_BOT_TOKEN[:5]}...{RP_BOT_TOKEN[-5:]}")
if RP_BOT_TOKEN is None:
    print (" Ошибка: Токен бота не найден.\n "
        "Убедитесь, что файл .env существует\n"
        "и содержит строку BOT_TOKEN=")
    exit()

print(f"ECHO1_BOT_TOKEN получен:{RP_BOT_TOKEN[:5]}...")

bot = telebot.TeleBot(RP_BOT_TOKEN)

@bot.message_handler(commands=['start'])
def cmd_start(message):
    bot.send_message(message.chat.id,"""
Добро пожаловать в Эхо РП
Где есть все:
и ничего, кроме твоего бота и ты""")
    if os.path.exists("EchoRP-READMe.md"):
       try:
           with open("EchoRP-READMe.md","rb") as file:
               bot.send_document(message.chat.id,file,caption="""
Ознакомтесь с ботом.
Файл для клиента/пользователя""")
       except Exception as e:
           bot.send_message(message.chat.id,f"Ошибка при отправки файла:{str(e)}")
    else:
        bot.send_message(message.chat.id,"Файл EchoRP-READMe.md не найден на сервере")

@bot.message_handler(func = lambda message : True)
def echo_all(message):
    bot.send_message(message.chat.id,message.text)

@bot.message_handler(content_type=['photo','video','document','voice'])
def echo_media(message):
    try:
        if message.content_type == 'photo':
           bot.send_photo(message.chat.id,message.photo[-1].file_id,caption=message.caption)
        elif message.content_type == 'video':
             bot.send_video(message.chat.id,message.video.file_id,caption=message.caption)
        elif message.content_type == 'document':
             bot.send_document(message.chat.id,message.document.file_id,caption=message.caption)
        elif message.content_type == 'voice':
             bot.send_voice(message.chat.id,message.voice.file_id,caption=message.caption)
    except Exception as e:
        bot.reply_to(message,f"Произошла ошибка при отправке файла!!!:\n{e}")

if __name__ == "__main__":
     print ("bot is running...")
     bot.infinity_polling(timeout=20, long_polling_timeout=10) 
