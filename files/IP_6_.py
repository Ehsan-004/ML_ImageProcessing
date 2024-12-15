# how to replace two part of image

import cv2

img = cv2.imread('../images/image2.jpg', cv2.IMREAD_COLOR)

# px = img[200, 200]
# print(img[:30])

img[100:200, 100:200] = img[300:400, 300:400]

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()