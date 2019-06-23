import numpy
import cv2

cap = cv2.VideoCapture(0)

while True:
	ret, frame = cap.read()
	cv2.imshow('frame', frame)

	#make red channel
	r = frame.copy()
	
	#erase other colours
	r[:, :, 0] = 0
	r[:, :, 1] = 0

	#Show red channel 
	cv2.imshow('RED', r)

	#make green channel
	g = frame.copy()

	#erase other colours from frame
	g[:, :, 0] = 0
	g[:, :, 2] = 0

	#show green channel
	cv2.imshow('GREEN', g)

	#make blue channel
	b = frame.copy()

	#erase other colours
	b[:, :, 1] = 0
	b[:, :, 2] = 0

	#show blue frame
	cv2.imshow('BLUE', b)

	if cv2.waitKey(20) & 0xFF == ord('q'):
		break
