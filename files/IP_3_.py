import cv2

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
output = cv2.VideoWriter('output.avi', fourcc, 24.0, (120, 120))

while(True):
    ret, frame = cap.read()
    output.write(frame)
    cv2.imshow('webcam window', frame)

    if cv2.waitKey(1) and 0XfF == ord('q'):
        break

cap.release()
output.release()
cv2.destroyAllWindows()


# Just to open the camera:
# import cv2

# cap = cv2.VideoCapture(0)

# while(True):
#     ret, frame = cap.read()
#     cv2.imshow('webcam window', frame)
#     if cv2.waitKey(1) and 0XfF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()