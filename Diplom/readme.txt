decouple
Для хранения приватной информации (ключи, адреса, токены и тд) используется библиотека decouple
https://pypi.org/project/python-decouple/
Ключи хранятся в файле .env. Файл располагается в корне проекта, рядом с manage.py
Содержание файла:
EMAIL_HOST_USER = mail@google.com
EMAIL_HOST_PASSWORD = пароль приложения google
TOKEN = телеграм токен
________________________________________________________________________________________________________________________

exif
https://pypi.org/project/exif/
Используется для извлечения exif информации из фотографии, сейчас функция read_exif_data(file_id) в utils.py
________________________________________________________________________________________________________________________

django_admin_geomap
https://github.com/vb64/django.admin.geomap/blob/main/READMEru.md
Библиотека для отрисовки карты

Для отрисовки карты в админ панели
from django_admin_geomap import ModelAdmin
class ImageFeedAdmin(ModelAdmin):
    # list_display = ('user', 'image', 'processed_image')
    list_display = ('user', 'image', 'lon', 'lat')
    geomap_field_longitude = "id_lon"
    geomap_field_latitude = "id_lat"

Для отрисовки во view
Особенность заключается в передаче контекста во view
    return render(request, 'object_detection/home.html', geomap_context(ImageFeed.objects.filter(user=request.user)))
должен быть передан только один параметр - geomap_context(ImageFeed.objects.filter(user=request.user))

Для решения создан включающий тег
@register.inclusion_tag('geomap/common.html')
def get_map(user_id):
    return geomap_context(ImageFeed.objects.filter(user=user_id))
________________________________________________________________________________________________________________________

Телеграм бот
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
    символов. Полученный набор символов используется для генерации случайного имени при сохранении загруженного
    изображения из телеграма.

send_welcome(message) - Отправляет пользователю приветственное сообщение, когда бот запускается (start) или
    просит о помощи (help).

handle_photo(message) - Обрабатывает сообщение с фотографией, инициализируя уровень состояния пользователя,
    отвечая сообщением и сохраняя информацию о фотографии.

get_options_keyboard(message) - Генерирует различные InlineKeyboards в зависимости от уровня пользователя,
    хранящегося в user_states.

callback_query(call) - Функция обратного вызова для обработки различных действий, связанных с обработкой изображений.

load_image(message) - Функция для загрузки изображения из сообщения, его сохранения и обновления состояний пользователя.

message_detect(chat_id, image_id) - Функция отправляет сообщение с результатами определения объектов в указанный чат.
________________________________________________________________________________________________________________________

Модуль signals
Была идея использовать сигналы при изменении определенных объектов вызывать функции обработки
Отказался. Оставил в качестве напоминая об интересном методе
https://docs.djangoproject.com/en/5.0/topics/signals/

signals/
    __init__.py
    signals.py
________________________________________________________________________________________________________________________

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
________________________________________________________________________________________________________________________

Модуль templatetags
Модуль расширяет механизм шаблонов, определяя пользовательские теги и фильтры с помощью Python и делает их доступными
для своих шаблонов с помощью тега .{% load %}
https://docs.djangoproject.com/en/5.0/howto/custom-template-tags/
templatetags/
    __init__.py
    detection_tag.py

current_stat(id) - простой тег. Возвращает количество обнаруженных объектов, сгруппированных по типу объекта
    и методу обнаружения для определенного изображения.

get_all_type() - простой тег. Получает список уникальных типов объектов вместе со связанными с ними
    идентификаторами изображений.

show_categories(cat_selected=0) - включающий тег. Функция получает список уникальных обнаруженных типов объектов
    вместе с соответствующими идентификаторами изображений и отображает их в шаблоне list_categories.html.

def get_map(user_id) - включающий тег. Предназначен для отображения карты с геометками фото
________________________________________________________________________________________________________________________

utils.py
Файл определения вспомогательных функций
process_image_detr(image_feed_id) - Функция определения объектов на изображении с использованием библиотеки
    DEtection TRansformers (DETR).

image_caption(image_feed_id) - Функция возвращает описание изображения.

get_graph() - Функция генерирует изображение текущего графика в кодировке Base64.

get_plot(x, y, type_graph) - Функция создает график с помощью библиотеки matplotlib и с логарифмической шкалой y.

get_plot_stat(x, y, type_graph) - Функция создает график метода определения объектов с помощью библиотеки matplotlib
    и с логарифмической шкалой y.

read_exif_data(file_id) - Функция получения гео меток из изображения
________________________________________________________________________________________________________________________

forms.py
Файл определения форм
https://docs.djangoproject.com/en/5.0/ref/forms/
https://docs.djangoproject.com/en/5.0/topics/forms/
https://docs.djangoproject.com/en/5.0/topics/auth/default/#built-in-auth-forms

RegisterUserForm(UserCreationForm) - форма связанная с моделью для регистрации пользователя
https://docs.djangoproject.com/en/5.0/topics/auth/default/
На форме выводятся следующие поля модели User:
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    username, с подписью 'Логин'
    email, с подписью 'Email'
    password1, с подписью 'Пароль'
    password2, с подписью 'Повтор пароля'
Все поля выводятся со стилем 'class': 'form-input'

LoginUserForm(AuthenticationForm) - форма связанная с моделью для аутентификации пользователя
На форме выводятся следующие поля:
    username, с подписью 'Логин'
    password, с подписью 'Пароль'

ImageFeedForm(forms.ModelForm) - форма связанная с моделью ImageFeed для загрузки изображения


________________________________________________________________________________________________________________________

models.py

________________________________________________________________________________________________________________________
templates
Шаблоны
templates/
    object_detection/
        email/
            password_reset_mail.html
            password_subject_reset_mail.txt
        about.html
        add_image_feed.html
        base.html
        dashboard.html
        home.html
        image_detect.html
        list_categories.html
        login.html
        register.html
        user_password_reset.html
        user_password_set_new.html
