import cv2
from matplotlib import pyplot as plt
import numpy as np

imgL = cv2.imread('0A0B4D50-A986-4659-9E5E-2A9BBF19D594_OD_1_L.jpg', cv2.CV_LOAD_IMAGE_GRAYSCALE)
imgR = cv2.imread('0A0B4D50-A986-4659-9E5E-2A9BBF19D594_OD_1_R.jpg', cv2.CV_LOAD_IMAGE_GRAYSCALE)
imgL_colour = cv2.imread('0A0B4D50-A986-4659-9E5E-2A9BBF19D594_OD_1_L.jpg', 1)
imgL_colour = cv2.cvtColor(imgL_colour, cv2.COLOR_BGR2RGB)
imgL_green = imgL_colour[:, :, 1]
imgL_green = np.bitwise_not(imgL_green)
imgL_red = imgL_colour[:, :, 0]
imgL_blue = imgL_colour[:, :, 2]
# imgR_colour = cv2.imread('0A0B4D50-A986-4659-9E5E-2A9BBF19D594_OD_1_R.jpg', 1)
# imgR_colour = cv2.cvtColor(imgR_colour, cv2.COLOR_BGR2RGB)
# rows = imgL.shape[0]
# cols = imgR.shape[1]
# stereo = cv2.StereoBM(cv2.STEREO_BM_BASIC_PRESET, ndisparities=0, SADWindowSize=27)
# disparity = stereo.compute(imgL, imgR)
# # diff = cv2.add(imgL, imgR)
# threshL = cv2.adaptiveThreshold(imgL, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 433, 0)
# threshR = cv2.adaptiveThreshold(imgR, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 433, 0)
# contoursL, hierarchy = cv2.findContours(threshL, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# contoursR, hierarchy2 = cv2.findContours(threshR, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# cv2.drawContours(imgL_colour, contoursL, -1, (255, 255, 255), 1)
# cv2.drawContours(imgL_colour, contoursR, -1, (255, 255, 255), 1)

# pixelShift_y = abs(np.argmax(imgL) // cols - np.argmax(imgR) // cols)  # rows shifted
# pixelShift_x = abs(np.argmax(imgL) % cols - np.argmax(imgR) % cols)  # columns shifted
# 120, 1695
# 891, 916


plt.figure()
plt.title('Red')
plt.imshow(imgL_red)
plt.figure()
plt.title('Green')
plt.imshow(imgL_green, 'Greens')
plt.figure()
plt.title('Blue')
plt.imshow(imgL_blue)
plt.show()
'''
commonPix = []
for i in range(0, rows):
    trueIndex = np.where(indices[i] == True)
    for item in trueIndex[0]:
        commonPix.append([i, item+1])
commonPix = np.array(commonPix)

for item in commonPix:
    diff[item[0], item[1]] = 255
'''
