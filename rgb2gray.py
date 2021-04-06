import os
import cv2 
directory = "/home/raman/Documents/deep learning/Medical-Transformer-main/labelcol"
dest = "/home/raman/Documents/deep learning/rmn/"
listinfo = os.listdir(directory)

for i in listinfo:
	c = directory + "/" + i
	d = dest + "/" + i
	img = cv2.imread(c)
	img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
	cv2.imwrite(d, img_gray) 
	
	
