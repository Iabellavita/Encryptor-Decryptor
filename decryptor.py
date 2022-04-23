"""Теперь «зеркальный» файл. Если в шифровальщике мы писали encrypt, то в дешифраторе
пишем decrypt."""
from pyfiglet import Figlet
import os
import sys
import pyAesCrypt


# Функция расшифровки
def decrypt(file: str, password: str):
    print('-' * 80)
    # Задаем размер буфера
    buffer_size = 512 * 1024
    # Вызываем функцию шифрования
    pyAesCrypt.decryptFile(file, os.path.splitext(file)[0], password, buffer_size)
    file_decrypt = os.path.splitext(file)[0].split('\\')[-1]
    print(f"[INFO --- \033[31m\033[1mDECRYPT\033[0m] --- \033[32m\033[1m{file_decrypt}\033[0m")
    # Удаляем исходный файл
    os.remove(file)


def walk(direct: str, passwd: str):
    # Перебор всех подпапок в указанной папке
    for name in os.listdir(direct):
        path = os.path.join(direct, name)
        if os.path.isfile(path):
            # если не получится расшифровать файл, мы его пропускаем
            try:
                decrypt(path, passwd)
            except:
                pass
        # Если это папка, рекурсивно повторяем
        else:
            walk(path)


if __name__ == "__main__":
    preview_text = Figlet(font="small", width=300)
    text = preview_text.renderText('D E C R Y P T O R')
    print(f'\033[35m\033[1m{text}\033[0m')

    DIR = input("НАПИШИ ДИРЕКТОРИЮ ДЛЯ ДЕШИФРОВАНИЯ: ")
    PASS = input("ВВЕДИ ПАРОЛЬ: ")

    # Запуск
    walk(DIR, PASS)
    print('-' * 80)
    # для самоуничтожения программы
    # os.remove(str(sys.argv[0]))
