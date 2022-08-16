from PIL import Image
import os
import PIL
import glob
def resize(src):
    fix_height = 960
    fix_width = 636
    img = Image.open(src)
    new_size = img.resize((fix_height,fix_width))
    #new_size.show()
    new_size.save(src)



# resize()