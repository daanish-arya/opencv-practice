import cv2
from matplotlib import pyplot as plt

orig = cv2.imread('original.jpg')
edit = cv2.imread('edited.jpg')

diff = cv2.subtract(orig, edit)
imgray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 127, 255, 0)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(edit, contours, -1, (255, 0, 0), 1)

plt.imshow(edit)
plt.show()