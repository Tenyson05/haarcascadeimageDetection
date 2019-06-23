import numpy
import cv2

# color detection
# object detection 
# edge detection
# detect different shapes 

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
     
    # show original frame
    cv2.imshow('Original', frame)

    c = frame.copy()

#contour with  thresholding
    img2gray = cv2.cvtColor(c, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(img2gray,127,255,0)
    image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    img1 = cv2.drawContours(frame, contours, -1, (0,0,255), 3)
    cv2.imshow('test1',img1)

# contour with canny, edge detection
    edges = cv2.Canny(c, 100, 100)
    # cv2.imshow('edges', edges)    
    image, contours, hierarchy = cv2.findContours(edges,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    img = cv2.drawContours(c, contours, -1, (0,255,0), 3)
    cv2.imshow('test', img)
   



    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()