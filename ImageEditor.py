import urllib.request
import cv2
import numpy as np
import os


# def store_raw_images():
# 	# inset image link here
# 	neg_images_link = "http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n06272803"
# 	# opens image url
# 	neg_image_urls = urllib.request.urlopen(neg_images_link).read().decode()

# 	# if the taregt directory doesn't exist create it
# 	if not os.path.exists("negative_images"):
# 		os.makedirs("negative_images")

# 	pic_num = 1713
 
# 	# Iterate through all the links on the space one by one by the help of a new line
# 	for i in neg_image_urls.split("\n"):
# 		try:
# 			print(i)
# 			urllib.request.urlretrieve(i, "negative_images/"+str(pic_num)+".jpg")
# 			img = cv2.imread("negative_images/"+str(pic_num)+".jpg", cv2.IMREAD_GRAYSCALE)
# 			resized_image = cv2.resize(img, (100, 100))
# 			cv2.imwrite("negative_images/"+str(pic_num)+".jpg", resized_image)
# 			pic_num += 1

# 		except Exception as e:
# 			print(str(e))


# def find_uglies():
# 	for file_type in ["negative_images"]:
# 		for img in os.listdir(file_type):
# 			for ugly in os.listdir("uglies"):
# 				try:
# 					current_image_path = str(file_type)+"/"+str(img)
# 					ugly = cv2.imread("uglies/"+str(ugly))	
# 					question = cv2.imread(current_image_path)

# 					if ugly.shape == question.shape and not(np.bitwise_xor(ugly,question).any()):
# 						print("Be gone peasant")
# 						print(current_image_path)
# 						os.remove(current_image_path)

# 				except Exception as e:
# 					print(str(e))

def create_pos_neg():
	for file_type in ["negative_images"]:
		for img in os.listdir(file_type):
			if file_type == "negative_images":
				line = file_type+"/"+img+"\n"
				with open("bg.txt", "a") as f:
					f.write(line)
					print("Printed: ", line)

			# elif file_type == "imageset_positive":
			# 	line = file_type+"/"+img+" 1 0 0 50 50\n"
			# 	with open("info.dat","a") as f:
			# 		f.write(line)

create_pos_neg()
# find_uglies()
# store_raw_images()