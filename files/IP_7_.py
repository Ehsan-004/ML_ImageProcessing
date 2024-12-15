# how to combine and mix two images:

import cv2

img1 = cv2.imread('image.jpeg')
img2 = cv2.imread('image2.jpg')

# add = img1 + img2
# cv2.imshow('add', add)

# add = cv2.add(img1, img2)

add = cv2.addWeighted(img1, 0.4, img2, 0.7, gamma=0)

cv2.imshow('add', add)



cv2.waitKey(0)
cv2.destroyAllWindows()
