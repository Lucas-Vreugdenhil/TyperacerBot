from time import sleep
from PIL import Image
import keyboard
import sys
import numpy as np
import pyautogui
import pytesseract

#code activation
keyboard.wait('Scroll_Lock')

#taking a screenshot of the text and assigning it to a variable
screenshot = pyautogui.screenshot(region=(562, 509, 800, 165))
screenshot.save(r'C:\Users\lucas\OneDrive\Documents\iveNeverCheated\Game bots\typeracerbot\screenshots\image.png')
image = Image.open(r'C:\Users\lucas\OneDrive\Documents\iveNeverCheated\Game bots\typeracerbot\screenshots\image.png')

#reading the text of the screenshot
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
text = pytesseract.image_to_string(image)

#cleaning up the text
text = text.replace('\n', ' ')
text = text.replace('change display format','')
print(text)

#typing out the text per character
for char in text:
        #sleep(0.04)
        keyboard.write(char)
