"""
Модуль для запуска телеграм-бота.
Бот запускается командой: python manage.py bot
"""
import random
import telebot
from django.core.management.base import BaseCommand
from django.conf import settings
from telebot import types
from ...models import *
from ...utils import *
from decouple import config

# bot = telebot.TeleBot(settings.TOKEN, threaded=False)
bot = telebot.TeleBot(config('TOKEN'), threaded=False)  # telebot.TeleBot(settings.TOKEN, threaded=False)

user_states = {}


class Command(BaseCommand):
    # Используется как описание команды обычно
    help = 'Just a command for launching a Telegram bot.'

    def handle(self, *args, **kwargs):
        bot.enable_save_next_step_handlers(delay=2)  # Сохранение обработчиков
        bot.load_next_step_handlers()  # Загрузка обработчиков
        bot.infinity_polling()


def generate_random_name():
    """
       Функция генерирует случайное имя, состоящее из 7 символов, используя заранее определенный набор символов.
       Полученный набор символов испольсуется для генерации случайного имени при сохранении загруженного изображения
       из телеграма.

       Returns:
           str: случайно сгенерированное имя.
    """
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    random_name = ''
    for i in range(7):
        random_name += random.choice(characters)
    return random_name


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    """
        Отправляет пользователю приветственное сообщение, когда бот запускается (start) или просит о помощи (help).
        Args:
            message: объект сообщения, который вызвал эту функцию.
        Returns:
            None
    """
    bot.reply_to(message, "Привет! Я бот для обнаружения объектов. ")


@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    """
        Обрабатывает сообщение с фотографией, инициализируя уровень состояния пользователя,
        отвечая сообщением и сохраняя информацию о фотографии.
        Args:
            message: объект сообщения, содержащий фотографию и информацию о чате.
        Returns:
            None
    """
    user_states[message.chat.id] = {'level': 0}
    bot.reply_to(message, "Я получил ваше фото! Выберите, что вы хотите сделать с ним.",
                 reply_markup=get_options_keyboard(message))
    user_states[message.chat.id]['photo'] = message.photo[-1].file_id
    # user_states[message.chat.id] = {'photo': message.photo[-1].file_id}
    print(user_states)


def get_options_keyboard(message):
    """
        Генерирует различные InlineKeyboards в зависимости от уровня пользователя, хранящегося в user_states.
        Args:
            message: объект сообщения, полученный от пользователя.
        Returns:
            types.InlineKeyboardMarkup: Сгенерированная InlineKeyboard.
    """
    print(user_states)
    if user_states.get(message.chat.id) and user_states[message.chat.id]['level'] == 0:
        keyboard = types.InlineKeyboardMarkup()
        load_btn = types.InlineKeyboardButton("Load image", callback_data="load_image")
        keyboard.add(load_btn)
        return keyboard
    elif user_states.get(message.chat.id) and user_states[message.chat.id]['level'] == 2:
        keyboard = types.InlineKeyboardMarkup()
        detr_btn = types.InlineKeyboardButton("DETR", callback_data="detect_image_detr")
        cafe_btn = types.InlineKeyboardButton("Cafe", callback_data="detect_image_standard")
        keyboard.add(detr_btn, cafe_btn)
        return keyboard


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    """
        Функция обратного вызова для обработки различных действий, связанных с обработкой изображений.
        Parameters:
        - call: объект запроса обратного вызова
        Returns:
        - None
    """
    chat_id = call.message.chat.id

    if call.data == "load_image":
        user_states[chat_id]['level'] = 1
        bot.answer_callback_query(call.id, "Загрузка изображения...")
        load_image(call.message)
    elif call.data == "detect_image_detr":
        user_states[chat_id]['level'] = 2
        bot.answer_callback_query(call.id, "Определение объектов на изображении...")
        image_id = ImageFeed.objects.filter(image=user_states[chat_id]['image']).values('id').first()
        process_image_detr(image_id['id'])
        message_detect(chat_id, image_id)
        # detected_objects = DetectedObject.objects.filter(image_feed=image_id['id']).values('object_type', 'confidence')
        # print(detected_objects)
        # message_text = "На изображении обнаружено " + str(len(detected_objects)) + " объектов \n"
        # for i in detected_objects:
        #     conf = '%.2f' % i['confidence']
        #     message_text += i['object_type'] + " - " + str(conf) + "\n"
        # bot.send_message(chat_id, message_text)
    elif call.data == "detect_image_standard":
        user_states[chat_id]['level'] = 2
        bot.answer_callback_query(call.id, "Определение объектов на изображении...")
        image_id = ImageFeed.objects.filter(image=user_states[chat_id]['image']).values('id').first()
        process_image(image_id['id'])
        message_detect(chat_id, image_id)
        # detected_objects = DetectedObject.objects.filter(image_feed=image_id['id']).values('object_type', 'confidence')
        # print(detected_objects)
        # message_text = "На изображении обнаружено " + str(len(detected_objects)) + " объектов \n"
        # for i in detected_objects:
        #     conf = '%.2f' % i['confidence']
        #     message_text += i['object_type'] + " - " + str(conf) + "\n"
        # bot.send_message(chat_id, message_text)


def load_image(message):
    """
        Функция для загрузки изображения из сообщения, его сохранения и обновления состояний пользователя.
        Args:
            message: объект сообщения, содержащий информацию о чате и пользователе.
        Returns:
            None
    """
    photo_id = user_states[message.chat.id]['photo']
    file_info = bot.get_file(photo_id)
    downloaded_file = bot.download_file(file_info.file_path)
    # image_stream = io.BytesIO(downloaded_file)
    # image = Image.open(image_stream)

    image_name = 'images/tg_photo_' + generate_random_name() + '.jpg'
    image_path = settings.MEDIA_ROOT + '/' + image_name  # 'tg_photo.jpg'
    with open(image_path, 'wb') as new_file:
        new_file.write(downloaded_file)
    bot.reply_to(message, 'Фотография сохранена.')
    image_feed = UserAddFields.objects.filter(tg_id=message.chat.id).values('user_id').first()

    ImageFeed.objects.create(user_id=image_feed['user_id'], image=image_name, lon=0, lat=0)

    user_states[message.chat.id]['level'] = 2
    user_states[message.chat.id]['image'] = image_name

    bot.send_message(message.chat.id,
                     f"Выберите способ детекции...",
                     reply_markup=get_options_keyboard(message))


def message_detect(chat_id, image_id):
    """
        Функция отправляет сообщение с результатами определения объектов в указанный чат.
        Args:
            chat_id (int): идентификатор чата, в который будет отправлено сообщение.
            image_id (dict): идентификатор изображения, на котором необходимо обнаружить объекты.
        Returns:
            None
    """
    detected_objects = DetectedObject.objects.filter(image_feed=image_id['id']).values('object_type', 'confidence')
    print(detected_objects)
    message_text = "На изображении обнаружено " + str(len(detected_objects)) + " объектов \n"
    for i in detected_objects:
        conf = '%.2f' % i['confidence']
        message_text += i['object_type'] + " - " + str(conf) + "\n"
    bot.send_message(chat_id, message_text)


# def insert_db(image, id):
#     con = sqlite3.connect('../../../db.sqlite3')
#     cur = con.cursor()
#     cur.execute('INSERT INTO object_detection_imagefeed VALUES (?), (?)', (image, id))

# bot.polling(none_stop=True)
