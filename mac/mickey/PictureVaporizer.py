# encoding: utf-8
import Image
import ImageDraw
import ImageFont
import dimensions
import math
from random import randint

def vaporizer(image):
	img = Image.open(image)
	dims = dimensions.dimensions(image)
	width = dims[0]
	height = dims[1]
	text = addtext(width, height);
	for i in range(width):
		for j in range(height):
			color = img.getpixel((i,j))
			newcolor = colorshift(color)
			img.putpixel((i,j), newcolor)
	
	img.save(image)
	print img.getpixel((250,250)), width, height

def addtext(w, h):
	with open ("Characters.py") as myfile:
		charlist = myfile.read()
		charlist_length = len(charlist)

	rand_char = randint(0,((charlist_length-1)/3)-1)*3
	name = ''
	name += charlist[rand_char] + charlist[rand_char + 1] + charlist[rand_char + 2]
	image = Image.new("RGBA", (w, h), (255,255,255,0))
	draw = ImageDraw.Draw(image)
	font = ImageFont.truetype("aquafont.ttf", 128)
	
	draw.text((10, 0), name, (0,0,0), font=font)

	
	return image

def colorshift(color):
	d = .97;
	r,g,b = color[:3]
	
	if (((b*d)>r) and ((b*d)>g)):
		r = .8*r
		g = .8*g

	if (((r*d)>b) and ((r*d)>g)):
		b = r
		g = .7*g

	if (((g*d)>b) and ((g*d)>r)):
		b = .5*b
		r = .8*r

	if (((r*d)>b) and ((g*d)>b)):
		b += (255-b)*.7

	if (((g*d)>r) and ((b*d)>r)):
		r = .5*r

	if (((r*d)>g) and ((b*d)>g)):
		g = .7*g
	
	if (((r*d)>b) and not ((g*d)>b) and not ((b*d)>r) and not ((g*d)>r) and not ((b*d)>g) and not ((r*d)>g)):
		if ((r > 255*d) and (g > 255*d) and (b > 255*d)):
			b += (204-(2*b))/3
			r += (204-g)/2
			g += (204-g)/2
		else:
			r += (204-r)/1.2
			g += (204-g)/1.2
			b += (204-g)/2

	return (int(r),int(g),int(b))

vaporizer('nmh.png')