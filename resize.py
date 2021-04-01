directory = "/home/raman/Documents/deep learning/Medical-Transformer-main/Kvasir-SEG/masks"

import PIL
import os
import os.path
from PIL import Image

for file in os.listdir(directory):
	print(file)
	f_img = directory + "/" + file 
	img = Image.open(f_img)
	img = img.resize((128,128))
	img.save(f_img)
