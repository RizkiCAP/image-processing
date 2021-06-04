# -*- coding: utf-8 -*-


import cv2

img = cv2.imread('foto.JPG')

b, g, r = cv2.split(img)
img = cv2.merge((b, g, r))

x = img[:, :, 1]
cv2.imshow('image', x)
cv2.waitKey(0)
