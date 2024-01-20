import cv2
from pytesseract import pytesseract
import easyocr
import keyboard
import pyautogui
import subprocess

while 1 == 1:
    subprocess.Popen('support_4_script.py', shell=True)
    key_up = False
    """считыавем букву с картинки"""
    reader = easyocr.Reader(["ru"])
    result = reader.readtext("screen.jpg", detail=0)
    try:
        print(result[0])
        key = result[0]
        print(key_up)
        """Проверяем на заглавные"""
        if result[0].isupper():
            key_up = True
            key = key.lower()
            """если есть то превращаем в строчные чтобы всё работало"""
        print(key_up)
        """перебор всей клавиатуры чтобы всё нажималось"""
        match key:
            case 'й':
                key = 'q'
            case 'ц':
                key = 'w'
            case 'у':
                key = 'e'
            case 'к':
                key = 'r'
            case 'е':
                key = 't'
            case 'н':
                key = 'y'
            case 'г':
                key = 'u'
            case 'ш':
                key = 'i'
            case 'щ':
                key = 'o'
            case 'з':
                key = 'p'
            case 'х':
                key = '['
            case 'ъ':
                key = ']'
            case 'ф':
                key = 'a'
            case 'ы':
                key = 's'
            case 'в':
                key = 'd'
            case 'а':
                key = 'f'
            case 'п':
                key = 'g'
            case 'р':
                key = 'h'
            case 'о':
                key = 'j'
            case 'л':
                key = 'k'
            case 'д':
                key = 'l'
            case 'ж':
                key = ';'
            case 'э':
                key = "'"
            case 'я':
                key = 'z'
            case 'ч':
                key = 'x'
            case 'с':
                key = 'c'
            case 'м':
                key = 'v'
            case 'и':
                key = 'b'
            case 'т':
                key = 'n'
            case 'ь':
                key = 'm'
            case 'б':
                key = ','
            case 'ю':
                key = '.'
            case _:
                key = key

        if key_up == True:
            keyboard.press(f"shift+{key}")
        else:
            keyboard.press(key)
    except IndexError:
        keyboard.press(" ")
