import glob
import os
import json

files = glob.glob("/home/minhnd/Documents/vmo/ai/3d-texture/texture/data/sample1/f1/*.cam")

for file in files:
    conOb = open(file, "r+")
    line1 = conOb.readline()
    line2 = "1460 0 0 1.33 960 720 \n"
    print(file)
    content = conOb.readlines()
    _, t = os.path.split(file)
    new_file = open("/home/minhnd/Documents/vmo/ai/3d-texture/texture/data/sample1/f2/" + t, "w")
    new_file.write(line1 + line2)