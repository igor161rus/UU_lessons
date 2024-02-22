# 1. Выберите одну или несколько сторонних библиотек Python, например, requests, pandas, numpy, matplotlib, pillow
# и другие.
# 2. Изучите документацию выбранных библиотек, ознакомьтесь с их основными возможностями и функциями.
# 3. Напишите простые задачи, в которых нужно использовать выбранные библиотеки, и выполните их.
# Приведите примеры использования библиотек в различных сценариях:
#   - Запросить данные с помощью библиотеки requests из API и вывести их в консоль.
#   - Считать данные из файла с помощью библиотеки pandas, выполнить простой анализ данных и вывести результаты.
#   - Создать массив чисел с помощью библиотеки numpy, выполнить математические операции с массивом и
#   вывести результаты.
#   - Визуализировать данные с помощью библиотеки matplotlib.
#   - Обработать изображение с помощью библиотеки pillow, например, изменить его размер, применить эффекты и
#   сохранить в другой формат.
# 4. Поясните, как выбранные библиотеки помогли в решении поставленных задач и какие преимущества они предоставили
# по сравнению с базовым функционалом Python.
#
# Рекомендации:
# - Используйте документацию и примеры кода из официальных ресурсов выбранных библиотек.
# - Экспериментируйте с разными параметрами и функциями в выбранных библиотеках, чтобы лучше понять их возможности.
# - Делайте выводы о преимуществах и удобстве использования сторонних библиотек в различных задачах.
#
# Оценка:
# Оценивайте выполнение задания по следующим критериям:
# - Верное использование выбранных сторонних библиотек Python.
# - Корректная работа и отображение результатов в соответствии с задачами.
# - Качество и полнота выполнения задания.

import requests
from github import Github

from utils import print_repo
from setings import token, password, user


# Использование requests
# Получаем веб-страницу с помощью get-запроса
response = requests.get('https://api.github.com/repos/igor161rus/UU_lessons', auth=(user, token))
# Выводим статус запроса, если 200, то ок
print(response.status_code)
# Для получения содержимого страницы используем метод content
print(response.content)
# Получаем содержимое в виде JSON и выводим некоторые ключи
data = response.json()
print(data['name'])
print(data['full_name'])

# Раз уж начал использовать github, то пробую библиотеку github
g = Github()
# получаем имя пользователя
username = g.get_user(user)

# выводим список всех публичных репозиториев
for repo in username.get_repos():
    print(repo)
print('**********************')
for repo in username.get_repos():
    print_repo(repo)
    print("="*100)

# Вывод
# C:\Python\Python38\python.exe C:\Python\Projects\UU_lessons\lesson_011\01_hw.py
# 200
# b'{"id":725074464,"node_id":"R_kgDOKzfCIA","name":"UU_lessons","full_name":"igor161rus/UU_lessons","private":false,"owner":{"login":"igor161rus","id":75830181,"node_id":"MDQ6VXNlcjc1ODMwMTgx","avatar_url":"https://avatars.githubusercontent.com/u/75830181?v=4","gravatar_id":"","url":"https://api.github.com/users/igor161rus","html_url":"https://github.com/igor161rus","followers_url":"https://api.github.com/users/igor161rus/followers","following_url":"https://api.github.com/users/igor161rus/following{/other_user}","gists_url":"https://api.github.com/users/igor161rus/gists{/gist_id}","starred_url":"https://api.github.com/users/igor161rus/starred{/owner}{/repo}","subscriptions_url":"https://api.github.com/users/igor161rus/subscriptions","organizations_url":"https://api.github.com/users/igor161rus/orgs","repos_url":"https://api.github.com/users/igor161rus/repos","events_url":"https://api.github.com/users/igor161rus/events{/privacy}","received_events_url":"https://api.github.com/users/igor161rus/received_events","type":"User","site_admin":false},"html_url":"https://github.com/igor161rus/UU_lessons","description":null,"fork":false,"url":"https://api.github.com/repos/igor161rus/UU_lessons","forks_url":"https://api.github.com/repos/igor161rus/UU_lessons/forks","keys_url":"https://api.github.com/repos/igor161rus/UU_lessons/keys{/key_id}","collaborators_url":"https://api.github.com/repos/igor161rus/UU_lessons/collaborators{/collaborator}","teams_url":"https://api.github.com/repos/igor161rus/UU_lessons/teams","hooks_url":"https://api.github.com/repos/igor161rus/UU_lessons/hooks","issue_events_url":"https://api.github.com/repos/igor161rus/UU_lessons/issues/events{/number}","events_url":"https://api.github.com/repos/igor161rus/UU_lessons/events","assignees_url":"https://api.github.com/repos/igor161rus/UU_lessons/assignees{/user}","branches_url":"https://api.github.com/repos/igor161rus/UU_lessons/branches{/branch}","tags_url":"https://api.github.com/repos/igor161rus/UU_lessons/tags","blobs_url":"https://api.github.com/repos/igor161rus/UU_lessons/git/blobs{/sha}","git_tags_url":"https://api.github.com/repos/igor161rus/UU_lessons/git/tags{/sha}","git_refs_url":"https://api.github.com/repos/igor161rus/UU_lessons/git/refs{/sha}","trees_url":"https://api.github.com/repos/igor161rus/UU_lessons/git/trees{/sha}","statuses_url":"https://api.github.com/repos/igor161rus/UU_lessons/statuses/{sha}","languages_url":"https://api.github.com/repos/igor161rus/UU_lessons/languages","stargazers_url":"https://api.github.com/repos/igor161rus/UU_lessons/stargazers","contributors_url":"https://api.github.com/repos/igor161rus/UU_lessons/contributors","subscribers_url":"https://api.github.com/repos/igor161rus/UU_lessons/subscribers","subscription_url":"https://api.github.com/repos/igor161rus/UU_lessons/subscription","commits_url":"https://api.github.com/repos/igor161rus/UU_lessons/commits{/sha}","git_commits_url":"https://api.github.com/repos/igor161rus/UU_lessons/git/commits{/sha}","comments_url":"https://api.github.com/repos/igor161rus/UU_lessons/comments{/number}","issue_comment_url":"https://api.github.com/repos/igor161rus/UU_lessons/issues/comments{/number}","contents_url":"https://api.github.com/repos/igor161rus/UU_lessons/contents/{+path}","compare_url":"https://api.github.com/repos/igor161rus/UU_lessons/compare/{base}...{head}","merges_url":"https://api.github.com/repos/igor161rus/UU_lessons/merges","archive_url":"https://api.github.com/repos/igor161rus/UU_lessons/{archive_format}{/ref}","downloads_url":"https://api.github.com/repos/igor161rus/UU_lessons/downloads","issues_url":"https://api.github.com/repos/igor161rus/UU_lessons/issues{/number}","pulls_url":"https://api.github.com/repos/igor161rus/UU_lessons/pulls{/number}","milestones_url":"https://api.github.com/repos/igor161rus/UU_lessons/milestones{/number}","notifications_url":"https://api.github.com/repos/igor161rus/UU_lessons/notifications{?since,all,participating}","labels_url":"https://api.github.com/repos/igor161rus/UU_lessons/labels{/name}","releases_url":"https://api.github.com/repos/igor161rus/UU_lessons/releases{/id}","deployments_url":"https://api.github.com/repos/igor161rus/UU_lessons/deployments","created_at":"2023-11-29T11:39:30Z","updated_at":"2023-12-21T06:45:43Z","pushed_at":"2024-02-22T16:52:43Z","git_url":"git://github.com/igor161rus/UU_lessons.git","ssh_url":"git@github.com:igor161rus/UU_lessons.git","clone_url":"https://github.com/igor161rus/UU_lessons.git","svn_url":"https://github.com/igor161rus/UU_lessons","homepage":null,"size":1333,"stargazers_count":0,"watchers_count":0,"language":"Python","has_issues":true,"has_projects":true,"has_downloads":true,"has_wiki":false,"has_pages":false,"has_discussions":false,"forks_count":0,"mirror_url":null,"archived":false,"disabled":false,"open_issues_count":0,"license":null,"allow_forking":true,"is_template":false,"web_commit_signoff_required":false,"topics":[],"visibility":"public","forks":0,"open_issues":0,"watchers":0,"default_branch":"master","permissions":{"admin":true,"maintain":true,"push":true,"triage":true,"pull":true},"network_count":0,"subscribers_count":1}'
# UU_lessons
# igor161rus/UU_lessons
# Repository(full_name="igor161rus/UU_lessons")
# **********************
# Наименование: igor161rus/UU_lessons
# Описание: None
# Дата создания: 2023-11-29 11:39:30+00:00
# Дата последнего обновления: 2024-02-22 16:52:43+00:00
# Домашняя страница: None
# Язык: Python
# Номер ветки: 0
# Количество звезд: 0
# --------------------------------------------------
# Содержание:
# ContentFile(path="lesson_002")
# ContentFile(path="lesson_003")
# ContentFile(path="lesson_004")
# ContentFile(path="lesson_005")
# ContentFile(path="lesson_006")
# ContentFile(path="lesson_007")
# ContentFile(path="lesson_008")
# ContentFile(path="lesson_009")
# ContentFile(path="lesson_010")
# ContentFile(path="lesson_010_1")
# ContentFile(path="lesson_011")
# ContentFile(path="readme.txt")
# ====================================================================================================
#
# Process finished with exit code 0