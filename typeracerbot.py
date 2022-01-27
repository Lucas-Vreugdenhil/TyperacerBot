from time import sleep
from PIL import Image
import keyboard
import sys
import numpy as np
import pyautogui
import pytesseract

#code activation
keyboard.wait('enter')

#taking a screenshot of the text and assigning it to a variable
screenshot = pyautogui.screenshot(region=(508, 605, 883, 200))
screenshot.save('image.png')
image = Image.open('image.png')

#reading the text of the screenshot
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
text = pytesseract.image_to_string(image)

#cleaning up the text
text = text.replace('\n', ' ')
text = text.replace('change display format','')
print(text)

#typing out the text per character
for char in text:
        sleep(0.02)
        keyboard.write(char)
