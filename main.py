import re
import cv2
from PIL import Image
import glob
from resizecrop import *

# The watermark self-created program
# create a transparent image in python pillow:
trans_img=Image.new('RGBA',(1000,400),(255,0,0,0))
trans_img.save('trans_img.png','PNG')

# open the featured image from the folder. 
# the featured images can be more than single so we will use python loop to handle all of them.

feauture_imgs=glob.glob("/Users/yaakovazat/Documents/git/blog-pic-unite/imgs/*.*")

# start handling the pictures.
def wmark(originalphoto,watermark):
    photo=Image.open(originalphoto)
    watermark=Image.open(watermark)
    photo.paste(watermark, (700, 250), watermark)
    photo.save(originalphoto)

# def resizecrop(src, out, width, height):
# 	img = Image.open(src)
# 	img = ImageOps.fit(img, (width, height), Image.ANTIALIAS, 0, (0.5, 0.5))
# 	img.save(out)

for image in feauture_imgs:
    imgcv2=cv2.imread(image)
    imgshape=imgcv2.shape
    # print(imgshape)
    height=imgshape[0]
    width=imgshape[1]
    if height <=400:
        static_height=400
        # ratio=int((400/height))
        new_width=width
    else:
        static_height=400
        ratio=int(height/400)
        new_width=int(ratio*width)
    # print(new_width)
    # resized_image=cv2.resize(imgcv2,(new_width,400))
    # cv2.imwrite(image,imgcv2) #将图片覆盖写入
    # resized_image=resizecrop(image,image,new_width,400)
    img_pillow=Image.open(image)
    resized_image=img_pillow.resize((1000,400))
    resized_image.save(image)

    #add watermark to the picture
    watermark="/Users/yaakovazat/Documents/git/blog-pic-unite/watermark.png"
    watermarked_imgage=wmark(image,watermark)
# end .