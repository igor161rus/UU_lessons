# Создайте переменную с этим файлом
# Распечатайте содержимое текстового файла в консоль
# Закройте файл

file_name = 'byron.txt'
file = open(file_name, mode='r')
file_content = file.read()
file.close()
print(file_content)
