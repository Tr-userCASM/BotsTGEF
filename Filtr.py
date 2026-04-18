#Я вернулся спустя 10 дннй от 8 марта,18 марта 2026.Задачи:Взять из исходников код,улучшить панель для админа ,чтобв после /admin работала.
#19 марта 2:51 пока без админской панели,только не забыть про гитхаб.я в потоке,раз вспомнил даже какие мелочи нужно (например,Портфодио по монтажу без моих мыслей но с датой),несмотря,что на фоне слушаю музыку.
#Исходник,моего опыта.9-10 февраля.
#структура:импорт,токен,хандлер,клавиаутура,пока бот работаeт. по поллинг
#18 апреля.добавил структуру описанин и исправил код в плане структуры с помощью ии (Dseek)

# Библиотеки
import os
import time
import logging
import telebot
from telebot import types
from telebot.apihelper import ApiTelegramException
from decouple import Config, RepositoryEnv
from pathlib import Path

# Шифровка токена
env_path = Path(__file__).parent.parent / '.env'
config = Config(RepositoryEnv(env_path))

FILTR_BOT_TOKEN = config('FILTR_BOT_TOKEN')

if not FILTR_BOT_TOKEN:
    print("Ошибка: Токен бота не найден в .env")
    exit()

logging.basicConfig(level=logging.DEBUG)

print(f"🔍 Bot PID: {os.getpid()}")
print(f"✅ Token check: {FILTR_BOT_TOKEN[:5]}...{FILTR_BOT_TOKEN[-5:]}")

bot = telebot.TeleBot(FILTR_BOT_TOKEN)

class ExceptionHandler:
    def handle(self, e: Exception):
        if isinstance(e, ApiTelegramException) and e.description == "Forbidden: bot was blocked by the user":
            print(f"❌ Бот заблокирован пользователем")
        else:
            print(f"⚠️ Другая ошибка: {e}")

def save_users(user_id):
    with open("users.txt", "a+",encoding="utf-8") as f:
        f.seek(0)
        users = f.read().splitlines()
        if str(user_id) not in users:
            f.write(str(user_id) + "\n")

ADMINS = [2135772776]

CHANNEL_ID = -1002025073862
def check_subscription (user_id):
  try:
     member = bot.get_chat_member(CHANNEL_ID,user_id)
     if member.status in ["member","administrator","creator"]:
        return True
     else:
        return False
  except Exception as e:
    print("Ошибка Подписки:",e)
    return False

@bot.message_handler(commands=['start'])
def cmd_start(message):
    save_users(message.from_user.id)
    user_id = message.from_user.id
    if not check_subscription(user_id):
        markup = types.InlineKeyboardMarkup()
        btn = types.InlineKeyboardButton("Подпишись",url="https://t.me/+T96k-Zvv_lcwZjYy")
        markup.add(btn)
        bot.send_message(message.chat.id, "Подпишись, чтоб пользоваться ботом https://t.me/+T96k-Zvv_lcwZjYy")

        return
    if message.from_user.is_bot:
        return
    name = message.from_user.username
    bot.send_message(message.chat.id,
        f"""Добро пожаловать в Filtr,{name}!

Это бот-переходник в мою среду 🍥.
Прочитайте README, чтоб ознакомиться с ботом.

Резерв на случай,если бот будет дорабатываться:@EcobeBot

Команды:
/start - обновить / ознакомиться с ботом.
/menu - переходит к кнопкам: Портфолио, Другие каналы,
кубик, связь с админом.""")


    if os.path.exists("F-tr.Readme.md.md"):
        try:
           with open("F-tr.Readme.md","rb") as file:
              bot.send_document(message.chat.id,file,caption = """Ознакомление с ботом
для клиента,пользователей""")
        except Exception as e:
             bot.send_message(message.chat.id,f"Ошибка при отправке:{str(e)}")
    else:
        bot.send_message(message.chat.id,"Файл F-tr.Readme.md не найден на сервере")

#оставлю это.1:55 11 февраля на наушниках
#Numd/Encore -Linkin park. Воспоминание об
#усном собеседование прочувствал.Клавитуру допишу
#Завтра. Полкодк и один день проверки,пока привпствии не готово.Все.хоть сейчас 8:57.Нало сделптт пррверку на подпискки на бота.

@bot.message_handler(commands=['menu'])
def markup_keyboard(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard= True)
    btn1 = types.KeyboardButton("Другие Проекты")
    btn2 = types.KeyboardButton("Портфолио(для клиента")
    btn3 = types.KeyboardButton("Тех.Поддержка✅")
    btn4 = types.KeyboardButton("Кубик 🎲")
    markup.add(btn1, btn2, btn3, btn4)
    bot.send_message(message.chat.id, "Главное Меню:",reply_markup = markup)

@bot.message_handler(func=lambda message: message.text == "Другие Проекты")
def other_project(message):
    bot.send_message(message.chat.id, """Другие Проекты:

�Архив

• @Ivnilbot - не рабочий

• @NS2Freedom - старый канал по саморазвитию

[Список будет пополняться].

🌀Экосистема:

Основной ;

• AR1DM —канал по дизайну и монтажу :
https://t.me/+QkDZYObO9LY0OGNi

• Мадара • арт-мемы⚡️(я незнаю что сказать о канале🤫):

https://t.me/+w2Z8SIONrs0zOWMy

• Автор Бота -Админ シタデル:
(ты уже подписан,раз читаешь это)

Базовый;

МУЗЫКА:
@Dart_muzik

МЕМЫ:
@me3meDa """)

@bot.message_handler(func=lambda message: message.text == "Портфолио(для клиента")
def portfolio_greeting(message):
    bot.send_message(message.chat.id, """Портфолио

Ссылки на каналы, где показаны мои работы

Дизайн/Инфографика:
https://t.me/+4Zwp8H90-540MTdi

Баннеры для тг-постов:
https://t.me/+PRubDk8r4dFlZDBi

Монтаж:
https://t.me/+Tx2oQqjnRCxkMzk6

Портфолио Боты,Аватарки:
https://t.me/+mgVQDDrM_hE2MDUy """)

@bot.message_handler(func=lambda message: message.text == "Тех.Поддержка✅")
def support_greeting(message):
    bot.send_message(message.chat.id, """🥱Техническая Поддержка.Связь с админом/создателем бота.
Функцию обратной связи и дополного сценария  не добавлю
, поэтому вопросы / проблемы (конкретная) в лс:

@s4k_4n0""")

@bot.message_handler(func=lambda message: message.text == "Кубик🎲")
def send_dice(message):
    dice = bot.send_dice(chat_id=message.chat.id, emoji="🎲")
    time.sleep(1)
    bot.send_message(chat_id=message.chat.id, text=f"Выпало: {dice.dice.value}")


#3:13.Прошлая версия админскоц панели не работало /admin,возможна была ошибка в тексте или .txt файлы не подходили.Но улучшу как то (json,можпт быть чем то другим).Исходникр хранить в гитхабе,а не в тг.
#16:28.Я решил одно менять сообщение (репли кнопкам,не надо) не обезательно,ведт в процессе работы можно добавить,единсивенное в админке только уведомить пользователей и все.
#23 марта.23:04 Исправио ошибку в коде с ии.

@bot.message_handler(commands=['alert_admins'])
def alert_broadcast(message):
    if message.from_user.id in ADMINS:
        bot.send_message(message.chat.id, """
Введи текст уведомление для всех             Этика:
1. Не писать бред.

2. Писать о обновах ботах и связанных с ним сообщения.

3. Предупреждать или напоминать пользователю нужное иногда свои мысли                                                                  исключение уместны""")
        bot.register_next_step_handler(message, start_cast)
    else:
        bot.send_message(message.chat.id, "Нет доступа")


def start_cast(message):
    text_to_send = message.text

    with open("users.txt", "r", encoding="utf-8") as f:
        users = f.read().splitlines()

    count = 0

    for user_id in users:
        try:
            bot.send_message(user_id, text_to_send)
            count += 1
        except Exception as e:
            print(f"Ошибка {user_id}: {e}")

    bot.send_message(message.chat.id, f"Отправлено: {count}")

if __name__ == "__main__":
     print ("bot is running...")
     bot.infinity_polling(timeout=20, long_polling_timeout=10) 

