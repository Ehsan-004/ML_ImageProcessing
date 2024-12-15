import cv2

img = cv2.imread('img_text.png')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# the result will be good for well taken pictures
# chnage second arg and see the result
ret, threshholded = cv2.threshold(img, 140, 255, cv2.THRESH_BINARY)

# if there are other colors in your picture, use:
adaptiveThreshholded = cv2.adaptiveThreshold(
    img_gray,
    255, 
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
    cv2.THRESH_BINARY, 
    255, 
    1
    )


cv2.imshow('text', threshholded)
cv2.imshow('text2', adaptiveThreshholded)
cv2.waitKey(0)
cv2.destroyAllWindows()