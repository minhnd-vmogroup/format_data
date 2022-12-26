import glob
import os
import json
import shutil

folder = "/home/minhnd/Documents/vmo/ai/3d-texture/data/r&d_1/2022_12_15_15_28_30/"
files = glob.glob(folder + "*.jpg")

for file in files:
    head, tail = os.path.split(file)
    print(tail[-9:-4])
    path = folder + "*" + str(tail[-9:-4]) + "*"
    same_file = glob.glob(path)
    for i in same_file:
        _, t = os.path.split(i)
        shutil.copyfile(i, "/home/minhnd/Documents/vmo/ai/3d-texture/format_data_src/data/tmp/tmp_data_raw/"+ t)    