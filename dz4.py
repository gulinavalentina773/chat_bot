#1 Функция выбора случайного(рандомного) элемента из списка
import random

a = [1,23,45,6,2566,66]
result = random.choice(a)
print('Random element:', result)

#2 Получить список файлов в директории и выбрать случайный файл
import os

folder = 'images\pony'
p = []

for files in os.scandir(folder):
    if files.is_file():
        p.append(files.name)

random_file = random.choice(p)
print('Random file:', random_file)