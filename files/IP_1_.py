import cv2
import matplotlib.pyplot as plt

img = cv2.imread("../images/image.jpeg")

cv2.imshow("image", img)

plt.imshow(img, interpolation="bicubic")
plt.plot((100,200), (200,300), 'r')
plt.show()
# cv2.waitKey(0)