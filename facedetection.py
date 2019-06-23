import numpy as np 
import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(grayFrame, 1.3, 5)
    font = cv2.FONT_HERSHEY_SIMPLEX
    for (x,y,w,h) in faces:
        owo = cv2.rectangle(frame,(x,y),(x+w, y+h),(255,0,0),2)
        cv2.putText(owo,'face',(x, y), font, .6, (255,255,255),2)
        roi_gray = grayFrame[y:y+h, x:x+w]
        roi_color =  frame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.3, 5)
        smile = smile_cascade.detectMultiScale(roi_gray, 1.3, 5)
        for (ex, ey, ew, eh) in eyes:
            uwu = cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh),(0, 255, 0), 2)
            cv2.putText(uwu,'eyes',(ex, ey), font, .6, (255,255,255),2)
        for (rx, ry, rw, rh) in smile:
            wuw = cv2.rectangle(roi_color, (rx, ry), (rx+rw, ry+rh),(0, 255, 0), 2)
            cv2.putText(wuw,'smile',(rx, ry), font, .6, (255,255,255),2)

    cv2.imshow('frame', frame)   

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()
    