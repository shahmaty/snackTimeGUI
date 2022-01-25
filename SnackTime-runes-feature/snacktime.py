import cv2 as cv
import numpy as np
import pyautogui
import time
from matplotlib import pyplot as plt
time.sleep(5)
leaguescreen = pyautogui.screenshot('ScreenShotProcessing/league.png')

img = cv.imread('ScreenShotProcessing/league.png', 0)
img2 = img.copy()
template = cv.imread('LeagueSquares/small_EvelynnSquare.png', 0)
w, h = template.shape[::-1]
img = img2.copy()
method = eval('cv.TM_CCORR_NORMED')
# Apply template Matching
res = cv.matchTemplate(img,template,method)
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
print(res)
top_left = max_loc
bottom_right = (top_left[0] + w, top_left[1] + h)
print(top_left, bottom_right)

centerX = (top_left[0] + bottom_right[0]) / 2
centerY = (top_left[1] + bottom_right[1]) / 2
print(centerX, centerY)

pyautogui.moveTo(centerX, centerY, 2)