# importing the module
from PIL import Image
import os
fix_height = 640
fix_width = 640

def formatToJpg(src):
    im = Image.open(src)
    im = im.resize((fix_height,fix_width))
    im.save(src)
    rgb_im = im.convert("RGB")
    # src = src[:-3]
    rgb_im.save(src[:-3] + "jpg")
    os.remove(src)

# formatToJpg('./img_file/a.png')