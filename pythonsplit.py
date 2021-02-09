import os
directory = "/home/raman/Documents/trainData_EndoCV2021_5_Feb2021/data_C1/bbox_C1" 

for filename in os.listdir(directory):
	if filename.endswith(".txt"):
		fd=open(filename)
		d = fd.read()
		m=d.split("\n")
		s="\n".join(m[:-1])
		fd=open(filename,"w+")
		for i in range(len(s)):
    			fd.write(s[i])
		fd.close()
			
