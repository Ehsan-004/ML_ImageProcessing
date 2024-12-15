# how to delete background of an image:

import cv2

img1 = cv2.imread('image2.jpg') # as a logo
img2 = cv2.imread('logo.png')

# print(img1.shape)
# print(img2.shape)

rows, cols, channels = img2.shape

# we want to put logo on first image, so we get the specified part of first image
# then we place the logo and put the part with logo bck
roi = img1[0:rows, 0:cols]

# image with no color is easier to process
img2_gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# cv2.threshold(src, limit, maximum_value, how) 
# under limit will be 0 and over will be 1 (black and white)
# the white parts of this image are iamge and blacks are background
ret, mask = cv2.threshold(img2_gray, 220, 255, cv2.THRESH_BINARY_INV)

# this one will have white background
mask_inv = cv2.bitwise_not(mask)

# parts of first image which logo will be placed not background
# uses a mask, white parts will 
img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
img1_fg = cv2.bitwise_and(img2, img2, mask=mask)

# place the logo with no bg in part with empty place
final = cv2.add(img1_bg, img1_fg)

# place the result in main image:
img1[0:rows, 0:cols] = final

# cv2.imshow('source', img2)
# cv2.imshow('mask', mask)
cv2.imshow('result', img1)

cv2.waitKey(0)
cv2.destroyAllWindows()