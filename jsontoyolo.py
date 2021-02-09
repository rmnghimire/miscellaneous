#!/usr/bin/env python2.7

import sys
import json
from PIL import Image
import time

json_file = "/home/raman/Downloads/JSON_Reader-master/kavsir_bboxes.json"
img_dir = "/home/raman/Downloads/Kvasir-SEG/images"
save_dir = "/home/raman/Downloads/JSON_Reader-master/"

def via_to_yolo(json_file, img_dir, save_dir):
    with open(str(json_file)) as annotation:
        # Load items in json
        data = json.load(annotation)
        # print(data[1])
        # exit()
        for item in data:
            filename = item
            print(item)
            # exit()
            filepath = str(img_dir) + "/" + filename + ".jpg"
            print(filepath)
            # Open image file correspoding to this annotation
            im = Image.open(filepath)
            # Get width and height of image
            width, height = im.size
            # Convert to float for yolo
            im_width = float(width)
            im_height = float(height)

            # Unique names for files
            # save_name = str(int(time.time() * 1000000))
            img_name = filename + ".jpg"
            txt_name = filename + ".txt"

            # Create txt file with same name as image
            # txt_file = str(filename[:-4]) + ".txt"

            txt_file = str(save_dir) + "/" + txt_name
            f = open(txt_file, "w+")
            # Loop through all regions in the image
            for region in data[item]["bbox"]:
                # Check if region is rectangle
                # if region["shape_attributes"]["name"] != "bbox":
                #     print("In" + str(filename) + ", region is not rect\n")
                #     break
                print(region)
                # exit()
                # Read data from json in float
                top_left_x = float(region["xmin"])
                top_left_y = float(region["ymin"])
                bb_width = float(region["xmax"])
                bb_height = float(region["ymax"])

                # Convert to yolo format
                # for cat in region["bbox"]:
                    # item_cat = region["region_attributes"][str(cat)]
                # yolo_x = top_left_x/
                # yolo_y = top_left_y
                # yolo_w = im_width-yolo_x - (im_width - bb_width)
                # yolo_h = im_height-yolo_y - (im_height - bb_height)
                yolo_x = (top_left_x + (bb_width / 2)) / im_width

                yolo_y = (top_left_y + (bb_height / 2)) / im_height
                yolo_w = bb_width / im_width
                yolo_h = bb_height / im_height
                # print(yolo_x, yolo_y, yolo_w, yolo_h)
                # exit()
                # Write line to file
                writeline = "0" + " " + str(yolo_x) + " " + str(yolo_y) + " " + str(yolo_w) + " " + str(yolo_h) + "\n"
                # exit()
                f.write(writeline)
            f.close()

            # Save image in the same path as txt
            img_path = str(save_dir) + "/" + img_name
            im.save(img_path)
            time.sleep(0.00001)


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage : ./read_json_annotation.py <json file> <image directory> <save directory>")
    else:
        print("Converting json file.....")
        via_to_yolo(sys.argv[1], sys.argv[2], sys.argv[3])
        print("Done!")

via_to_yolo(json_file, img_dir, save_dir)