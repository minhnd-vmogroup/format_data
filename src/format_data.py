import glob
import os
import json
import shutil
from PIL import Image


def format_data(new_fold):
    files = glob.glob(new_fold + "*.json")

    for json_file in files:
        conten_ob = open(json_file, "r")
        data = json.load(conten_ob)
        _, tail = os.path.split(json_file)

        new_name = new_fold + tail[0:-4] + 'cam'
        if os.path.exists(new_name):
            os.remove(new_name)
        new_file = open(new_name, 'w')
        string_number = ""
        string_number += str(data["cameraPoseARFrame"][3]) + " " + str(data["cameraPoseARFrame"][7]) + " " + str(data["cameraPoseARFrame"][11]) + " " \
                + str(data["cameraPoseARFrame"][0]) + " " + str(data["cameraPoseARFrame"][1]) + " " + str(data["cameraPoseARFrame"][2]) + " " \
                +  str(data["cameraPoseARFrame"][8]) + " " + str(data["cameraPoseARFrame"][9]) + " " + str(data["cameraPoseARFrame"][10]) + " "\
                +  str(data["cameraPoseARFrame"][4]) + " " + str(data["cameraPoseARFrame"][5]) + " " + str(data["cameraPoseARFrame"][6]) + "\n"
        string_number += "0.77 0 0 0.1 0.5 0.5\n" # sam5 1.03 0 0 1.333 0.5 0.5 102000 sam6 0.76 0 0 1.333 0.5 0.5 95000 sam7 0.76 0.1 0.1 1.3 0.5 0.5 96000
        #
        new_file.write(string_number)
        
        os.remove(json_file)

def select_file(raw_fold, new_fold):
    files = glob.glob(raw_fold + "*.jpg")

    for file in files:
        _, tail = os.path.split(file)
        print(tail[-9:-4])
        path = raw_fold + "*" + str(tail[-9:-4]) + "*"
        same_file = glob.glob(path)
        for i in same_file:
            _, t = os.path.split(i)
            shutil.copyfile(i, new_fold + t) 
def add_intrinsic_para(fold, new_fold):
    files = glob.glob(fold + "*.cam")
    for file in files:
        _, tail = os.path.split(file)
        readFile = open(file, "r")
        string_content = readFile.readline()
        string_content += "0.9 0.1 0.1 0.75 0.5 0.5"
        new_name = new_fold + tail[0:-4] + '.cam'
        if os.path.exists(new_name):
            os.remove(new_name)
        new_file = open(new_name, 'w')
        new_file.write(string_content)
        print(new_file)
        

def rotate_img(fold):
    files = glob.glob(fold + "*.jpg")
    files1 = glob.glob(fold + "*.png")
    for file in files:
        # print(file)
        image = Image.open(file)
        # image = image.transpose(method=Image.FLIP_LEFT_RIGHT)
        # print(image.size)
        image = image.rotate(-90)
        # image = image.resize((1440, 1920))
        # print(image.size)
        image.save(file)
        # break
    for file in files1:
        # print(file)
        image = Image.open(file)
        # print(image.size)
        # image = image.transpose(method=Image.FLIP_LEFT_RIGHT)
        image = image.rotate(-90)
        # print(image.size)
        # image = image.resize((192, 256))
        image.save(file)

if __name__=="__main__":
    raw_fold = "/home/minhnd/ai/3d-texture/format_data_src/data/cup/"
    new_fold = "/home/minhnd/ai/3d-texture/format_data_src/data/cup1/image/"
    select_file(raw_fold, new_fold)
    format_data(new_fold)
    # rotate_img(new_fold)

    # raw_fold = "/home/minhnd/ai/3d-texture/g2ltex/src/Data/apt0/apt0/"
    # new_fold = "/home/minhnd/ai/3d-texture/format_data_src/data/apt0/apt0/"
    # add_intrinsic_para(raw_fold, new_fold)
