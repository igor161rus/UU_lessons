import random

from django.core.management.base import BaseCommand
from django.conf import settings
import telebot
from telebot import types
from ...models import *
from ...utils import *

bot = telebot.TeleBot(settings.TOKEN, threaded=False)

user_states = {}


class Command(BaseCommand):
    # Используется как описание команды обычно
    help = 'Just a command for launching a Telegram bot.'

    def handle(self, *args, **kwargs):
        bot.enable_save_next_step_handlers(delay=2)  # Сохранение обработчиков
        bot.load_next_step_handlers()  # Загрузка обработчиков
        bot.infinity_polling()


def generate_random_name():
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    random_name = ''
    for i in range(7):
        random_name += random.choice(characters)
    return random_name


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я бот для обнаружения объектов. ")


@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    user_states[message.chat.id] = {'level': 0}
    bot.reply_to(message, "I got your photo! Please choose what you'd like to do with it.",
                 reply_markup=get_options_keyboard(message))
    user_states[message.chat.id] = {'photo': message.photo[-1].file_id}


def get_options_keyboard(message):
    if user_states.get(message.chat.id) and user_states[message.chat.id]['level'] == 0:
        keyboard = types.InlineKeyboardMarkup()
        load_btn = types.InlineKeyboardButton("Load image", callback_data="load_image")
        keyboard.add(load_btn)
        return keyboard
    elif user_states.get(message.chat.id) and user_states[message.chat.id]['level'] == 1:
        keyboard = types.InlineKeyboardMarkup()
        detect_btn = types.InlineKeyboardButton("Detect", callback_data="detect_image")
        keyboard.add(detect_btn)
        return keyboard


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    chat_id = call.message.chat.id

    if call.data == "load_image":
        user_states[chat_id]['level'] = 1
        bot.answer_callback_query(call.id, "Загрузка изображения...")
        load_image(call.message)
    elif call.data == "detect_image":
        user_states[chat_id]['level'] = 2
        bot.answer_callback_query(call.id, "Определение объектов на изображении...")
        image_id = ImageFeed.objects.filter(image=user_states[chat_id]['image']).values('id').first()
        process_image_detr(image_id)


def load_image(message):
    photo_id = user_states[message.chat.id]['photo']
    file_info = bot.get_file(photo_id)
    downloaded_file = bot.download_file(file_info.file_path)
    # image_stream = io.BytesIO(downloaded_file)
    # image = Image.open(image_stream)

    image_name = '\\images\\tg_photo_' + generate_random_name() + '.jpg'
    image_path = settings.MEDIA_ROOT + image_name  # 'tg_photo.jpg'
    image_path = image_path.replace('\\', '/')
    with open(image_path, 'wb') as new_file:
        new_file.write(downloaded_file)
    bot.reply_to(message, 'Фотография сохранена.')
    image_feed = UserAddFields.objects.filter(tg_id=message.chat.id).values('user_id').first()
    print('1----', image_feed['user_id'])

    ImageFeed.objects.create(user_id=image_feed['user_id'], image=image_name)

    user_states[message.chat.id]['level'] = 2
    user_states[message.chat.id] = {'image': image_name}
# def insert_db(image, id):
#     con = sqlite3.connect('../../../db.sqlite3')
#     cur = con.cursor()
#     cur.execute('''INSERT INTO object_detection_imagefeed VALUES (?), (?)''', (image, id))

# bot.polling(none_stop=True)
