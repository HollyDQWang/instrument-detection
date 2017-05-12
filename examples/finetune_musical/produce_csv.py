'''
Fetch images in "equipboard" folder; store their urls and labels.
'''

import os
import urllib
import hashlib
import argparse
import numpy as np
import pandas as pd
from skimage import io
import multiprocessing
import csv
from fnmatch import fnmatch
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import random
import uuid

image_path="/home/ubuntu/data/equipboard/"

label_filename = "/home/ubuntu/caffe/examples/finetune_musical/style_names.txt"

csv_filenmae = "/home/ubuntu/caffe/examples/finetune_musical/equipboard_category.csv"

with open(label_filename, 'r') as label_file:
	labels =  [_.rstrip() for _ in label_file.readlines()]

print labels

dictionary = []

pattern = "*.jpg"

for ind in range(len(labels)):
	label = labels[ind]
	for path, subdirs, files in os.walk(os.path.join(image_path, label)):
		for name in files:
			if fnmatch(name, pattern):
				uid =  uuid.uuid4()
				dictionary.append({"id": uid, "image_url": os.path.join(path, name), "label": ind})

random.shuffle(dictionary)
with open(csv_filenmae, "w") as output_file:
	writer = csv.writer(output_file)
	writer.writerow(["id","image_url", "label", "_split"])
	for i in range(len(dictionary)):
		if (i<round(len(dictionary)*0.7)):
			dictionary[i]['_split'] = 'train'
		else:
			dictionary[i]['_split'] = 'test'
		writer.writerow([dictionary[i]["id"], dictionary[i]["image_url"], dictionary[i]["label"], dictionary[i]["_split"]])

