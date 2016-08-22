import cv2
from matplotlib import pyplot as plt
import numpy as np
np.set_printoptions(threshold=np.inf)
imgL = cv2.imread('0A0B4D50-A986-4659-9E5E-2A9BBF19D594_OD_1_L.jpg', cv2.CV_LOAD_IMAGE_GRAYSCALE)
imgR = cv2.imread('0A0B4D50-A986-4659-9E5E-2A9BBF19D594_OD_1_R.jpg', cv2.CV_LOAD_IMAGE_GRAYSCALE)
rows = imgL.shape[0]
cols = imgR.shape[1]
diff = cv2.add(imgL, imgR)
# ret, thresh = cv2.threshold(imgray, 100, 255, 0)
# thresh = cv2.adaptiveThreshold(diff, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 21, 42)
# contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# cv2.drawContours(imgL, contours, -1, (255, 0, 0), 1)
stereo = cv2.StereoBM(cv2.STEREO_BM_BASIC_PRESET, ndisparities=32, SADWindowSize=31)
disparity = stereo.compute(imgL, imgR)
'''
zeroDisp = []
for i in range(0, rows // 2):
    zero_index = np.where(disparity[i] == 0)
    for item in zero_index[0]:
        zeroDisp.append([i, item+1])
zeroDisp = np.array(zeroDisp)
'''
'''
windowSize = 11
for coord in zeroDisp:
    thresh = cv2.adaptiveThreshold(diff[(coord[0]-windowSize):(coord[0]+windowSize), (coord[1]-windowSize):(coord[1]+windowSize)],
                                   255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 433, 42)
    diff[(coord[0] - windowSize):(coord[0] + windowSize), (coord[1] - windowSize):(coord[1] + windowSize)] = thresh
# '''
''''''
thresh = cv2.adaptiveThreshold(diff, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 345, 42)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(diff, contours, -1, (255, 0, 0), 1)

plt.imshow(imgL, 'gray')
plt.figure()
plt.imshow(diff, 'gray')
plt.show()

# '''
'''
plt.figure()
#plt.title('Disparity map')
#plt.imshow(disparity)
#plt.figure()
#plt.imshow(thresh, 'gray')
#plt.figure()
plt.imshow(possibleDust, 'gray')
# cv2.drawContours(thresh, contours, -1, (255, 0, 0), 1)
# plt.imshow(diff)
plt.show()
# '''
