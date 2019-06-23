import numpy as np
import cv2

shape_cascade = cv2.CascadeClassifier("shapeCascade.xml")

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    shapes = shape_cascade.detectMultiScale(grayFrame, 50, 50)
    print(shapes)

    for (x, y, w, h) in shapes:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255,0,0),2)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()
