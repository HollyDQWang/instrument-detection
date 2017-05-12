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

anno_path="../Annotations/DET/train"
image_path="../Data/DET/train"
train_filename = "DET/train.txt"
val1_filename = "DET/val1.txt"
val2_filename = "DET/val2.txt"
test_filename = "DET/test.txt"

full_list = []

pattern = "*.xml"

for path, subdirs, files in os.walk(os.path.join(anno_path)):
	for name in files:
		pname = name.split('/')[-1].split('.')[0]
		if fnmatch(name, pattern):
			if os.path.exists(os.path.join(image_path, pname+".JPEG")):
				full_list.append(pname)

print len(full_list)
random.shuffle(full_list)

cut = int(len(full_list)*0.6)
cut2= int(len(full_list)*0.1)


with open(train_filename, "w") as output_file:
	for i in range(cut):
		output_file.write(full_list[i] +" "+str(i+1)+"\n")

full_list = full_list[cut:]

with open(val1_filename, "w") as output_file:
	for i in range(cut2):
		output_file.write(full_list[i] +" "+str(i+1)+"\n")

full_list = full_list[cut2:]

with open(val2_filename, "w") as output_file:
	for i in range(cut2):
		output_file.write(full_list[i] +" "+str(i+1)+"\n")

full_list = full_list[cut2:]
with open(test_filename, "w") as output_file:
	for i in range(len(full_list)):
		output_file.write(full_list[i] +" "+str(i+1)+"\n")
