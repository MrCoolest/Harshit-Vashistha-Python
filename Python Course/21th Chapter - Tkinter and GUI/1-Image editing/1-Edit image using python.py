# installation of pillow library 
# change the image extension
# resize image files
# resize multiple image using for loop
# sharpness
# brightness
# Color
# Constrast
# image blur, GaussianBlur

from PIL import Image, ImageEnhance, ImageFilter
import os
# Img1 = Image.open('Dog 3.jpg')
# Img1.save('Dog3.png')
# Img1.show('Dog 3.jpg')
# min_size = (200,200)
# Img1.thumbnail(min_size)
# Img1.save('Dog3small.jpg')

# for item in os.listdir():
#     if item.endswith('.jpg'):
#         img = Image.open(item)
#         filename, extension = os.path.splitext(item)
#         img.save(f'{filename}.png')

# -------sharpness--------------
# pic = Image.open('dog2.jpg')
# enhancesss = ImageEnhance.Sharpness(pic)
# enhancesss.enhance(6).save('dog2edit.jpg')
# 0 : bluryy
# 1 : orignal
# 2 : increase sharpness
# 3 : increse more

# ------------Colour---------------
# pic1 = Image.open('dog2.jpg')
# enhancesss = ImageEnhance.Color(pic1)
# enhancesss.enhance(6).save('dog2edit.jpg')


# -----------------brightnesss ------------------
# pic2 = Image.open('Dog2.jpg')
# increase = ImageEnhance.Brightness(pic2)
# increase.enhance(1.3).save('dog2brightness.jpg') 


# --------------------contrass --------------

# pic2 = Image.open('Dog2.jpg')
# increase = ImageEnhance.Contrast(pic2)
# increase.enhance(4).save('dog2brightness.jpg') 


# --------------image blurrr------------

pic3 = Image.open('dog1.jpg')
pic3.filter(ImageFilter.GaussianBlur(radius=5)).save('dog1blurr.png')