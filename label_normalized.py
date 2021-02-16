import os
directory = "/home/raman/Documents/albumentations/labels_augmented"
for filename in os.listdir(directory):
	g = directory +"/" + filename
	h = open(g)
	y = h.read()
	print(y,"intial")
	y = (str(y)[2:-2])
	
	writeline = "0" + " " + y +"\n"

	
	file = open(g,"w+")
	file.write(writeline)
	file.close()

	
	
