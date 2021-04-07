# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw
from itertools import product
from sys import argv

# q = enlarging coefficient
_, input_name, q = argv
q = int(q)

img_input = Image.open(input_name)
w, h = img_input.size

img_output = Image.new("RGBA", (w*q, h*q), (0, 0, 0, 0))

img_drw = ImageDraw.Draw(img_output)
for x, y in product(range(w), range(h)):
    c = img_input.getpixel((x, y))
    shape = [(x*q, y*q), ((x+1)*q-1, (y+1)*q-1)]
    img_drw.rectangle(shape, c)

new_filename = input_name + "_out.png"
img_output.save(new_filename, "PNG")
print("Enlarged image saved as " + new_filename)
