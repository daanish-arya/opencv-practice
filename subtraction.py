import cv2
from matplotlib import pyplot as plt
import numpy as np

imgL = cv2.imread('0A0B4D50-A986-4659-9E5E-2A9BBF19D594_OD_1_L.jpg', cv2.CV_LOAD_IMAGE_GRAYSCALE)
imgR = cv2.imread('0A0B4D50-A986-4659-9E5E-2A9BBF19D594_OD_1_R.jpg', cv2.CV_LOAD_IMAGE_GRAYSCALE)

diff = cv2.add(imgL, imgR)
# print(diff)
# diff = cv2.subtract(orig, diff)


# ret, thresh = cv2.threshold(imgray, 100, 255, 0)
thresh = cv2.adaptiveThreshold(diff, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 433, 42)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(imgL, contours, -1, (255, 0, 0), 1)
stereo = cv2.StereoBM(cv2.STEREO_BM_BASIC_PRESET, ndisparities=32, SADWindowSize=23)
disparity = stereo.compute(imgL, imgR, cv2.CV_32F)
disp_abs = np.absolute(disparity)
min_indices = np.argmin(disp_abs)
min_pixels = np.array()

for i in range(1, len(disp_abs[0])+1):
    for j in range(1, len(disp_abs)+1):
        if min_indices[] == 0:
            continue
        else:


'''
plt.figure()
plt.title('Disparity map')
plt.imshow(disparity)
plt.figure()
plt.imshow(thresh, 'gray')
plt.figure()
plt.imshow(imgL, 'gray')
# cv2.drawContours(thresh, contours, -1, (255, 0, 0), 1)
# plt.imshow(diff)
plt.show()
'''
