import os

file = open("/home/minhnd/Documents/vmo/ai/3d-texture/data/du18_sample/du18_exp1/2022_12_13_17_14_57/format_data/textured_output_1.ply", "r")
new_file = open("/home/minhnd/Documents/vmo/ai/3d-texture/data/du18_sample/du18_exp1/2022_12_13_17_14_57/format_data/textured_output_new.ply", "w")
while(True):
    line = file.readline()
    x = line.split()
    string_line = ""
    if len(x) == 5:
        string_line += x[0] + " " + x[1] + " " + x[2]+ "\n"
        new_file.writelines(string_line)
    

