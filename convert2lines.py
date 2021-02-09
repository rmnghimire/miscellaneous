from PIL import Image
import os

directory = "/home/raman/Documents/endoccvchallenge/thulo size"
image = "/home/raman/Documents/endoccvchallenge/bbox_image"
endpint = "/home/raman/Documents/endoccvchallenge/YOLOlabel1"
for filename in os.listdir(directory):
    mm = "/home/raman/Documents/endoccvchallenge/thulo size/"
    mm = mm + filename
    x = open(mm)
    print(filename)

    y = x.read()

    print(y)
    g = y.split(" ")
    print(g)
    # exit()
    x_min = float(g[1])
    print(x_min)
    y_min = float(g[2])
    x_max = float(g[3])
    y_max = float(g[4])

    x_min1 = float(g[6])
    print(x_min)
    y_min1 = float(g[7])
    x_max1 = float(g[8])
    y_max1 = float(g[9])

    j = os.path.splitext(filename)[0] + "_bbox.jpg"

    imagepath = "/home/raman/Documents/endoccvchallenge/bbox_image/" + str(j)
    im = Image.open(imagepath)
    width, height = im.size
    im_width = float(width)
    im_height = float(height)

    dw = 1.0 / im_width
    dh = 1.0 / im_height
    x = (x_min + x_max) / 2.0
    y = (y_min + y_max) / 2.0
    w = x_max - x_min
    h = y_max - y_min
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh

    x1 = (x_min1 + x_max1) / 2.0
    y1 = (y_min1 + y_max1) / 2.0
    w1 = x_max1 - x_min1
    h1 = y_max1 - y_min1
    x1 = x1 * dw
    w1 = w1 * dw
    y1 = y1 * dh
    h1 = h1 * dh
    img_name = j + "_bbox.jpg"
    txt_name = filename

    txt_file = str(endpint) + "/" + txt_name
    f = open(txt_file, "w+")

    writeline = "0" + " " + str(x) + " " + str(y) + " " + str(w) + " " + str(h) + "\n" + "0" + " " + str(x1) + " " + str(y1) + " " + str(w1) + " " + str(h1) + "\n"
    f.write(writeline)
    f.close()

    img_path = str(endpint) + "/" + img_name
    im.save(img_path)
