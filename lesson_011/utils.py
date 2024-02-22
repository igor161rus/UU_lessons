import base64


def print_repo(repo):
    """Печать полей репозитория"""
    # Полное имя репозитория
    print('Наименование:', repo.full_name)
    # Описание репозитория
    print('Описание:', repo.description)
    # Дата создания репозитория
    print('Дата создания:', repo.created_at)
    # Дата последнего обновления
    print('Дата последнего обновления:', repo.pushed_at)
    # Веб сайт
    print('Домашняя страница:', repo.homepage)
    # Язык
    print('Язык:', repo.language)
    # Номер ветки
    print('Номер ветки:', repo.forks)
    # number of stars
    print('Количество звезд:', repo.stargazers_count)
    print("-"*50)
    # Содержание репозитория
    print('Содержание:')
    for content in repo.get_contents(""):
        print(content)
    try:
        # repo license
        print('Лицензия:', base64.b64decode(repo.get_license().content.encode()).decode())
    except:
        pass
