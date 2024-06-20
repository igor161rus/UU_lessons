import sqlite3

import telebot
from PIL import Image
import io
from telebot import types
from settings import TOKEN_BOT

TOKEN = TOKEN_BOT
bot = telebot.TeleBot(TOKEN)

user_states = {}


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Send me an image, and I'll provide options for you!")


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


def insert_db(image, id):
    con = sqlite3.connect('db.sqlite3')
    cur = con.cursor()
    cur.execute('''INSERT INTO object_detection_imagefeed VALUES (?), (?)''', (image, id))



bot.polling(none_stop=True)
