#19-20 марта 2:22.Вернулся к основе в vim   
#если чисто как есь 2 недели ебался сначала
#айограмм,потрм решил телебо и 2 дня
#с исправление синтаксиса пишу бота
#добавляю  ReadMe запись 24 января
#28.01.Исправляю ошибки запуска бота страдая
#31.01.Бот закончил,остался биттсч за руссификатор

#Библиотеки
import os
import time
import telebot
from telebot import types
import logging
import decouple 
from pathlib import Path
from decouple import Config, RepositoryEnv
from pathlib import Path

#Шифровка Токена
env_path = Path(__file__).parent.parent / '.env'
config = Config(RepositoryEnv(env_path))

RP_BOT_TOKEN = config('RP_BOT_TOKEN')

if not RP_BOT_TOKEN:
    print("Ошибка: Токен бота не найден в .env")
    exit()

print(f"🔍 Bot PID: {os.getpid()}")
print(f"✅ Token check: {RP_BOT_TOKEN[:5]}...{RP_BOT_TOKEN[-5:]}")

bot = telebot.TeleBot(RP_BOT_TOKEN)

#Приветствие + файл
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

#Эхо сообщения
@bot.message_handler(func = lambda message : True)
def echo_all(message):
    bot.send_message(message.chat.id,message.text)

#Эхо медиа
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

#Бот работает пока polling работает
if __name__ == "__main__":
     print ("bot is running...")
     bot.infinity_polling(timeout=20, long_polling_timeout=10)

#18 апрпля.с помощью ии убрал load .env оставилdecouople из за простоты кода.Снес http.client это костыль,остадся так же Filtr.py 
