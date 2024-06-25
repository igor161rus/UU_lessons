В приложении зарегистрирован запуск телеграм-бота с помощью manage.py
https://docs.djangoproject.com/en/5.0/howto/custom-management-commands/
Бот запускается командой: python manage.py bot

management/
    __init__.py
    commands/
    __init__.py
    bot.py - содержит функции для работы с телеграм ботом

class Command(BaseCommand) - Класс для создания собственной django-admin команды

generate_random_name - Функция генерирует случайное имя, состоящее из 7 символов, используя заранее определенный набор
    символов. Полученный набор символов испольсуется для генерации случайного имени при сохранении загруженного
    изображения из телеграма.

send_welcome(message) - Отправляет пользователю приветственное сообщение, когда бот запускается (start) или
    просит о помощи (help).

handle_photo(message) - Обрабатывает сообщение с фотографией, инициализируя уровень состояния пользователя,
    отвечая сообщением и сохраняя информацию о фотографии.

get_options_keyboard(message) - Генерирует различные InlineKeyboards в зависимости от уровня пользователя,
    хранящегося в user_states.

callback_query(call) - Функция обратного вызова для обработки различных действий, связанных с обработкой изображений.

load_image(message) - Функция для загрузки изображения из сообщения, его сохранения и обновления состояний пользователя.


Модуль signals
Была идея использовать сигналы при изменении определенных объектов вызывать функции обработки
Отказался. Оставил в качкстве напоминая об интересном методе
https://docs.djangoproject.com/en/5.0/topics/signals/

signals/
    __init__.py
    signals.py


Модуль static
В модуле расположены статические файлы для отрисовки Веб-сайта, такие как изображения, JavaScript, CSS
https://docs.djangoproject.com/en/5.0/howto/static-files/
static/
    object_detection/
        css/
            docs.min.css
            styles.css
        images/
            logo.png
            site.ico
        js/
            docs.min.js

Модуль templatetags
templatetags/
    __init__.py
    detection_tag.py