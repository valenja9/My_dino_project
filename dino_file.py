#I) Import knihoven
from PIL import ImageGrab, ImageOps
import pyautogui
from numpy import *

#komen
count = 0
while True:
  x1, y1, a, b = 129, 461, 64, 26
  box = x1, y1, x1 + a, y1 + b
  image = ImageGrab.grab(box)
  gray = ImageOps.grayscale(image)
  a = array(gray.getcolors())
  value = a.sum()

  if value != 1911:
      count += 1
      print(count, value)
      pyautogui.press("space")  # Zmáčkne za nás space(mezernik)





