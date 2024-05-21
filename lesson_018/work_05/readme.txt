PS D:\Python\Projects\UU\lessons\lesson_018\work_05> django-admin startproject todo
PS D:\Python\Projects\UU\lessons\lesson_018\work_05> ls


    Каталог: D:\Python\Projects\UU\lessons\lesson_018\work_05


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
PS D:\Python\Projects\UU\lessons\lesson_018\work_05> cd todo
PS D:\Python\Projects\UU\lessons\lesson_018\work_05\todo> django-admin startapp tasks
PS D:\Python\Projects\UU\lessons\lesson_018\work_05\todo> python manage.py migrate
PS D:\Python\Projects\UU\lessons\lesson_018\work_05\todo> python manage.py createsuperuser
Username (leave blank to use 'admin'): admin
Email address:
Password: 123456
Password (again):
This password is too short. It must contain at least 8 characters.
This password is too common.
This password is entirely numeric.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.
PS D:\Python\Projects\UU\lessons\lesson_018\work_05\todo> python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
May 21, 2024 - 10:14:54
Django version 5.0.6, using settings 'todo.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
