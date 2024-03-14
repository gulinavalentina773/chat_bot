# работа с файлами

import os 

# ин6формация о текущем файле
print(
    os.getcwd()
)
# result
# C:\Users\User\Desktop\Гулина\chat_bot-main

# Получить список файлов в директории
print(
    os.listdir()
)
# result
# ['arr.py', 'dict_01.py', 'filesystem.py', 'hello_world.txt', 'main.py', 'README.md', 'str.py']

#проверка есть ли директория
print(
    os.path.isdir('homeworks')
)

for f in os.listdir():
    print(
        f'is dir: {f}', os.path.isdir(f)
    )

# result
# is dir: arr.py False
# is dir: dict_01.py False
# is dir: filesystem.py False
# is dir: hello_world.txt False
# is dir: homeworks True
# is dir: main.py False
# is dir: README.md False
# is dir: str.py False

# создание директорий
    
# os.mkdir('home_01/work_1')
# if not os.path.isdir('home_01/work_1'):
#   os.makedirs('home_01/work_1')

def make_dirs(path):
    if not os.path.isdir('home_01/work_1'):
        os.makedirs('home_01/work_1')

# make_dirs('home_01/work_2')
        
# 1. проверка существует ли директория
# 1.1 если существует, то ничего не делать
# 1.2 если не существует, то создать
# 2. ищем файлы, которые будем переносить
# 2.1 ищем файлы с форматом .txt
# 2.2 ищем файлы название которых содержит "homework"
# 3. перемещение
# 3.1 выбор файла
# 3.2 копируем файл
# 3.3 переходим в директорий
# 3.4 добавляем файл
# 3.4.1 проверка исходного и нового файла
# 3.5 удаляем исходный файл