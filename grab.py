from PIL import Image

im = Image.open("1.png")
box = (0, 300, 700, 700)
region = im.crop(box)
region.show()