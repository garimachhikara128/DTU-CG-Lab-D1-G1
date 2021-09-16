import matplotlib.pyplot as plt
from PIL import Image

import sys
sys.setrecursionlimit(500000)

white = (255,255,255)
red = (255,0,0)
yellow = (255, 255, 0)

# create a polygon on image
def createPolygon(im, width, height) :

    i = width/8
    while i <= 3 * width / 8 :
        im.putpixel((int(i),int(height/8)),red)
        i += 1
    
    i = height / 8
    while i <= 3 * height / 8 :
        im.putpixel((int(3*width/8),int(i)),red)
        i += 1

    i = 3 * width/8
    while i >= width / 8 :
        im.putpixel((int(i),int(3 * height/8)),red)
        i -= 1

    i = 3 * height / 8
    while i >= height / 8 :
        im.putpixel((int(width/8),int(i)),red)
        i -= 1

def bf(im, x, y, bc , fc) :

    cc = im.getpixel((x,y))

    if cc == bc or cc == fc :
        return 

    im.putpixel((x,y),fc)

    bf(im, x, y-1, bc, fc)
    bf(im, x, y+1, bc, fc)
    bf(im, x-1, y, bc, fc)
    bf(im, x+1, y, bc, fc)

# create an image
im1 = Image.new(mode="RGB",size=(400,250),color=white)
width, height = im1.size

# call the fxns
createPolygon(im1, width, height)
im2 = im1.copy()
bf(im2, int(width/4) , int(height/4) , red , yellow)

# im.show()
# plt.imshow(im)
# plt.show()

#Subplots
f, axis = plt.subplots(1,2,figsize=(10,5))
axis[0].imshow(im1)
axis[1].imshow(im2)

axis[0].set_title("Before Boundary Fill Algo")
axis[1].set_title("After Boundary Fill Algo")

plt.show()

