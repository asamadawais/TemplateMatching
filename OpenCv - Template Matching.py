#!/usr/bin/env python
# coding: utf-8

# In[3]:


import cv2
import numpy as np
from matplotlib import pyplot as plt

img_rgb = cv2.imread('group.jpg')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
template = cv2.imread('abs.png',0)
#template = cv2.imread('waldo.png',0)
# saves the width and height of the template into 'w' and 'h'
w, h = template.shape[::-1]

res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.9
# finding the values where it exceeds the threshold
loc = np.where( res >= threshold)
for pt in zip(*loc[::-1]):
    #draw rectangle on places where it exceeds threshold
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (255,0,0), 2)

#cv2.imwrite('found_waldo.png',img_rgb)
cv2.imwrite('found_abs.png',img_rgb)



