from PIL import Image
import os.path, sys

path = r"D:\both\LLRM" 
dirs = os.listdir(path)

def crop():
    for item in dirs:
        fullpath = os.path.join(path,item)         #corrected
        if os.path.isfile(fullpath):
            im = Image.open(fullpath)
            f, e = os.path.splitext(fullpath)
            # imCrop = im.crop((282,282,1054,1054)) #corrected
            imResize = im.crop((282,282,1054,1054)) #add the desired cordinates here
            imCropped = imResize.resize((128, 128)) #add the desired size here 
            imCropped.save(f + 'final.bmp', "BMP", quality=100)

crop()