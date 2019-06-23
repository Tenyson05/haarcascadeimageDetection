import numpy as np
import cv2

cap = cv2.VideoCapture(0)
 
while True:
    _, frame = cap.read()
    
    # hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # orange = np.array([240, 240, 255])
    # upper_orange = np.array([255, 255, 255])

    # mask = cv2.inRange(hsv, orange, upper_orange)
    # res = cv2.bitwise_and(frame, frame, mask=mask)

    # cv2.imshow('frame', frame)
    # cv2.imshow('mask', mask)
    # cv2.imshow('res', res)


    
    # # converts the image color to HSV
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # # variable for copying the frame to apply the gray color to 
    # t = frame.copy()

    # # treshold = cv2.threshold(frame, 12, 255, cv2.THRESH_BINARY )
    
    # cv2.imshow('frame',frame)
    # cv2.imshow('t' ,gray)
    # cv2.imshow('threshold', treshold)


    # laplacian = cv2.Laplacian(frame, cv2.CV_64F)
    # soblex = cv2.Sobel(frame, cv2.CV_64F,1,0,ksize=5)
    # sobley = cv2.Sobel(frame, cv2.CV_64F,0,1,ksize=5)

    # edges = cv2.Canny(frame, 100, 200)
    r = frame.copy()
    r[:, :, 1] = 0

    cv2.imshow('whatever', r)
    cv2.imshow('original', frame)
    # cv2.imshow('laplacian', laplacian)
    # cv2.imshow('edges', edges)
    # cv2.imshow('soblex', soblex)
    # cv2.imshow('sobley', sobley)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()




# # red channel
    # red = frame.copy()
    # red[:,:,0] = 0
    # red[:,:,1] = 0
    # cv2.imshow('red', red)

    # #green channel
    # green = frame.copy()
    # green[:,:,0] = 0
    # green[:,:,2] = 0
    # cv2.imshow("green", green)

    # #blue channel
    # blue = frame.copy()
    # blue[:,:,1] = 0
    # blue[:,:,2] = 0
    # cv2.imshow('blue', blue)

    # #yellow channel
    # yellow = frame.copy()
    # yellow[:,:,0] = 0
    # yellow[:,:,0] = 0
    # cv2.imshow('yellow', yellow)
