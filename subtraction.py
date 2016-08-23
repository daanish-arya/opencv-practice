import cv2
from matplotlib import pyplot as plt
import numpy as np

imgL = cv2.imread('0A0B4D50-A986-4659-9E5E-2A9BBF19D594_OD_1_L.jpg', cv2.CV_LOAD_IMAGE_GRAYSCALE)
imgR = cv2.imread('0A0B4D50-A986-4659-9E5E-2A9BBF19D594_OD_1_R.jpg', cv2.CV_LOAD_IMAGE_GRAYSCALE)
imgL_colour = cv2.imread('0A0B4D50-A986-4659-9E5E-2A9BBF19D594_OD_1_L.jpg', cv2.CV_LOAD_IMAGE_COLOR)
imgR_colour = cv2.imread('0A0B4D50-A986-4659-9E5E-2A9BBF19D594_OD_1_R.jpg', cv2.CV_LOAD_IMAGE_COLOR)
rows = imgL.shape[0]
cols = imgR.shape[1]
diff = cv2.add(imgL, imgR)
threshL = cv2.adaptiveThreshold(imgL, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 433, 0)
threshR = cv2.adaptiveThreshold(imgR, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 433, 0)
contoursL, hierarchy = cv2.findContours(threshL, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contoursR, hierarchy2 = cv2.findContours(threshR, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(imgL_colour, contoursL, -1, (255, 0, 0), 1)
cv2.drawContours(imgL_colour, contoursR, -1, (255, 0, 0), 1)

print contoursL

pixelShift_y = abs(np.argmax(imgL) // 1736 - np.argmax(imgR) // 1736)  # rows shifted
pixelShift_x = abs(np.argmax(imgL) % 1736 - np.argmax(imgR) % 1736)  # columns shifted


# plt.imshow(imgL, 'gray')
# plt.figure()
# plt.imshow(imgR, 'gray')
# plt.show()

'''
commonPix = []
for i in range(0, rows):
    trueIndex = np.where(indices[i] == True)
    for item in trueIndex[0]:
        commonPix.append([i, item+1])
commonPix = np.array(commonPix)

for item in commonPix:
    diff[item[0], item[1]] = 255
# '''