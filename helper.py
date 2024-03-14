import os

def make_dirs(path):
    """создает директории если их нет"""

    if not os.path.isdir('home_01/work_1'):
        os.makedirs('home_01/work_1')