from PIL import Image
import os

for subdirs, dirs, files in os.walk('/home/minhnd/ai/3d-texture/data/raw_data/wall_du12/'):
    for file in files:
        if file.endswith((".jpg")):
            img_path = os.path.join(subdirs, file.split('.')[0] + ".jpg")
            save_path = os.path.join("/home/minhnd/ai/3d-texture/format_data_src/data/tmp/tmp_png/" + file.split('.')[0] + ".png")
            im1 = Image.open(r'{0}'.format(img_path))
            im1.save(r'{0}'.format(save_path))
            