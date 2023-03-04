from PIL import Image
import pytesseract
import numpy as np
import cv2
pytesseract.pytesseract.tesseract_cmd = r'F:\Tesseract\tesseract.exe'


images_path = 'images/'


filename = '1.PNG'
img = np.array(Image.open(images_path + filename))


wimg = img[:, :, 0]
ret,thresh = cv2.threshold(wimg,100,255,cv2.THRESH_BINARY)

kernel = np.ones((7, 7), np.uint8)
closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
erosion = cv2.erode(closing, kernel, iterations = 1)
mask = cv2.bitwise_or(erosion, thresh)
white = np.ones(img.shape,np.uint8)*255
white[:, :, 0] = mask
white[:, :, 1] = mask
white[:, :, 2] = mask
result = cv2.bitwise_or(img, white)

cv2.imshow('image', result)
cv2.waitKey(0)
cv2.destroyAllWindows()