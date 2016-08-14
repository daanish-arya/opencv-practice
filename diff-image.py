import numpy as np
import cv2
from matplotlib import pyplot as plt

imgL = cv2.imread('tsukuba-l.png', cv2.CV_LOAD_IMAGE_GRAYSCALE)
imgR = cv2.imread('tsukuba-r.png', cv2.CV_LOAD_IMAGE_GRAYSCALE)
img = 0


stereo = cv2.StereoBM(cv2.STEREO_BM_BASIC_PRESET, ndisparities=16, SADWindowSize=15)
disparity = stereo.compute(imgL, imgR)
plt.figure()
plt.imshow(imgL, 'gray')
plt.figure()
plt.imshow(disparity, 'gray')
plt.show()