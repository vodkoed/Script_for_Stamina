import pyautogui
import cv2
import numpy as np
import sys

# Установить путь к Tesseract
image = pyautogui.screenshot(region=(958, 300, 40, 40))
image_array = np.array(image)

# Сохранить скриншот в файл
cv2.imwrite(f"screen.jpg", image_array)

