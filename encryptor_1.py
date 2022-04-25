"""Шифровать и дешифровать мы будем при помощи буфера, таким
образом мы избавимся от ограничения на размер файла (по крайней мере, значительно
уменьшим это ограничение)."""
from pyfiglet import Figlet
import os
import sys
import pyAesCrypt


# Функция расшифровки
def encrypt(file: str, password: str):
    print('-' * 80)
    # Задаем размер буфера
    buffer_size = 512 * 1024
    # Вызываем функцию шифрования
    pyAesCrypt.encryptFile(file, file + ".crp", password, buffer_size)
    file_encrypt = file.split('\\')[-1]
    print(f"[INFO --- \033[31m\033[1mENCRYPT\033[0m] --- \033[32m\033[1m{file_encrypt}.crp\033[0m")
    # Удаляем исходный файл
    os.remove(file)


def walk(direct: str, passwd: str):
    # Перебор всех подпапок в указанной папке
    for name in os.listdir(direct):
        path = os.path.join(direct, name)
        # Если это файл, шифруем его
        if os.path.isfile(path):
            encrypt(path, passwd)
        # Если это папка, рекурсивно повторяем
        else:
            walk(path)


if __name__ == "__main__":
    preview_text = Figlet(font="small", width=300)
    text = preview_text.renderText('E N C R Y P T O R')
    print(f'\033[35m\033[1m{text}\033[0m')

    DIR = input("НАПИШИ ДИРЕКТОРИЮ ДЛЯ ШИФРОВАНИЯ: ")
    PASS = input("ВВЕДИ ПАРОЛЬ: ")

    # Запуск
    walk(DIR, PASS)
    print('-' * 80)
    # для самоуничтожения программы
    # os.remove(str(sys.argv[0]))
