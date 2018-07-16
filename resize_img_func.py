import PIL
from PIL import Image

img_path = 'gear_images/boots/10101265x1011117_zm.jpeg'
img_path_new = 'rotemp/10101265x1011117_zmresized.jpg'

def resize_img(image_path):
    size = 128, 128
    img = Image.open(image_path)
    img.thumbnail(size)
    img.save(img_path_new)
    imgnew = Image.open(img_path_new)
    return imgnew

resize_img(img_path)
