# how to draw and write on video

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    # draw shapes
    # cv2.line(frame, (100, 200), (200, 400), (255, 0, 0), 10)
    # cv2.rectangle(frame, (100,200), (200, 300), (0, 0, 255), 2)
    # cv2.circle(frame, (200, 200), 70, (0, 120, 255), 2)
    # points = np.array([[10,120], [140, 170], [220,20], [140,500]])
    # cv2.polylines(frame, [points], True, (100, 100, 100), 5)

    font = cv2.FONT_HERSHEY_SCRIPT_COMPLEX
    cv2.putText(frame, 'hello world', (100, 200), font, 1, (100, 100, 250))

    cv2.imshow('webcam window', frame)

    if cv2.waitKey(1) and 0XfF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()