import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('lab1\Lena.png')

red = (0.8 * img[:, : , 0]).astype(img.dtype)

blue = (1.2 * img[:, : , 2]).astype(img.dtype)

img2 = cv2.merge([red ,img[:, : , 1], blue])


cv2.imshow("TEST_ORIGINAL", img)


gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
blurred = cv2.GaussianBlur(src=gray, ksize=(3, 5), sigmaX=0.1) 
      
edges = cv2.Canny(blurred, 70, 135)

thresh, thresh_img = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)

cv2.imshow("THRESH", thresh_img)

cv2.waitKey(0)

