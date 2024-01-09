file_name = 'byron.txt'
file = open(file_name, mode='r', encoding='utf8')
print(file.tell())

print('читаем 100 символов')
file_content = file.read(100)
print(file_content)
print(file.tell())

print('читаем остальное')
file_content = file.read()
print(file_content)
print(file.tell())

file.close()