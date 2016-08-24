import numpy as np
import cv2
import sys
from matplotlib import pyplot as plt


imgL = cv2.imread('tsukuba-l.jpg', cv2.CV_LOAD_IMAGE_GRAYSCALE)
imgR = cv2.imread('tsukuba-r.jpg', cv2.CV_LOAD_IMAGE_GRAYSCALE)

cols = imgL.shape[0]
rows = imgR.shape[1]

print "Cols = " + str(cols) + ", Rows = " + str(rows)
stereo = cv2.StereoBM(cv2.STEREO_BM_BASIC_PRESET, ndisparities=0, SADWindowSize=19)
disparity = stereo.compute(imgL, imgR)
fig = plt.figure()
fig.canvas.set_window_title('Window Size of %d' % 19)
plt.imshow(disparity, 'gray')

# plt.figure()
# plt.imshow(imgL, 'gray')
plt.show()
