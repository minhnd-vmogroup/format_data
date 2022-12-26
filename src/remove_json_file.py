import os 
import glob

folder = "/home/minhnd/ai/3d-texture/format_data_src/data/sample1/f1/"
files = glob.glob(folder + "*.jpg")

for file in files:
    os.remove(file)