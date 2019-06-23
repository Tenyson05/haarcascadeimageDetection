import os
import cv2
import numpy as pd

os.chdir("C:/Users/Rojah/Documents/OpenCV/imageset_positive")

print(os.getcwd())

# newName = "neg_"
num = 0

# for pic in os.listdir():
# 	os.rename(pic, newName + str(num)+".jpg")
	

for pic in os.listdir():
	if pic[0:3] == "pos_":
		print("skipped")
	else:
		img = cv2.imread(pic)
		resized_img = cv2.resize(img, (50,50))
		cv2.imwrite("pos_"+str(num)+".jpg", resized_img)
		num += 1