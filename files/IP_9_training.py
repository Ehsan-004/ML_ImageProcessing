import cv2

img = cv2.imread("img_text2.jpg")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, threshholded_image = cv2.threshold(img_gray, 100, 255, cv2.THRESH_BINARY)
adapted = cv2.adaptiveThreshold(
    img_gray,
    255, 
    cv2.ADAPTIVE_THRESH_MEAN_C,
    cv2.THRESH_BINARY,
    100,
    1
)

cv2.imshow('image', threshholded_image)
cv2.imshow('image2', adapted)
cv2.waitKey(0)
cv2.destroyAllWindows()
