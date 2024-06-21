from django.core.management.base import BaseCommand
from django.conf import settings
import telebot
from telebot import types
from ...models import *

bot = telebot.TeleBot(settings.TOKEN, threaded=False)

user_states = {}


class Command(BaseCommand):
    # Используется как описание команды обычно
    help = 'Just a command for launching a Telegram bot.'

    def handle(self, *args, **kwargs):
        bot.enable_save_next_step_handlers(delay=2)  # Сохранение обработчиков
        bot.load_next_step_handlers()  # Загрузка обработчиков
        bot.infinity_polling()


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я бот для обнаружения объектов. ")


@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    bot.reply_to(message, "I got your photo! Please choose what you'd like to do with it.",
                 reply_markup=get_options_keyboard())
    user_states[message.chat.id] = {'photo': message.photo[-1].file_id}


def get_options_keyboard():
    keyboard = types.InlineKeyboardMarkup()
    load_btn = types.InlineKeyboardButton("Load image", callback_data="load_image")
    ascii_btn = types.InlineKeyboardButton("ASCII Art", callback_data="ascii")
    keyboard.add(load_btn, ascii_btn)
    return keyboard


def load_image(message):
    photo_id = user_states[message.chat.id]['photo']
    file_info = bot.get_file(photo_id)
    downloaded_file = bot.download_file(file_info.file_path)
    # image_stream = io.BytesIO(downloaded_file)
    # image = Image.open(image_stream)

    save_path = 'media/images/tg_photo.jpg'
    with open(save_path, 'wb') as new_file:
        new_file.write(downloaded_file)
    bot.reply_to(message, 'Фотография сохранена.')


# def insert_db(image, id):
#     con = sqlite3.connect('../../../db.sqlite3')
#     cur = con.cursor()
#     cur.execute('''INSERT INTO object_detection_imagefeed VALUES (?), (?)''', (image, id))

# bot.polling(none_stop=True)
