import cv2
from matplotlib import pyplot as plt
import numpy as np
np.set_printoptions(threshold=np.inf)
imgL = cv2.imread('0A0B4D50-A986-4659-9E5E-2A9BBF19D594_OD_1_L.jpg', cv2.CV_LOAD_IMAGE_GRAYSCALE)
imgR = cv2.imread('0A0B4D50-A986-4659-9E5E-2A9BBF19D594_OD_1_R.jpg', cv2.CV_LOAD_IMAGE_GRAYSCALE)

diff = cv2.add(imgL, imgR)
# ret, thresh = cv2.threshold(imgray, 100, 255, 0)
# thresh = cv2.adaptiveThreshold(diff, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 433, 42)
# contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# cv2.drawContours(imgL, contours, -1, (255, 0, 0), 1)
stereo = cv2.StereoBM(cv2.STEREO_BM_BASIC_PRESET, ndisparities=32, SADWindowSize=23)
disparity = stereo.compute(imgL, imgR, cv2.CV_32F)
rows = disparity.shape[0]
cols = disparity.shape[1]
# plt.imshow(thresh, 'gray')
# plt.figure()
# plt.imshow(imgL, 'gray')
# '''
# print disparity[200]
ayus = [[0, 0]]
for i in range(0, rows):
    zero_index = np.where(disparity[i] == 0)
    for item in zero_index[0]:
        ayus.append([i, item+1])

for i in range(1, rows-200):
    for j in range(200, cols-200):
        ret, thresh = cv2.threshold(diff[(i-200):(i+200), (j-200):(j+200)], 90, 255, 0)
        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cv2.drawContours(imgL, contours, -1, (255, 0, 0), 1)
# '''

# '''
# '''
plt.figure()
#plt.title('Disparity map')
#plt.imshow(disparity)
#plt.figure()
#plt.imshow(thresh, 'gray')
#plt.figure()
plt.imshow(diff, 'gray')
# cv2.drawContours(thresh, contours, -1, (255, 0, 0), 1)
# plt.imshow(diff)
plt.show()
# '''
