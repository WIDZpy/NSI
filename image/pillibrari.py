from math import floor

import PIL.Image as pil
the = pil.open("teapot.png")
img = the.copy()
def horizontal_ligne(im,y,c):
	for loop in range(the.size[0]):
		im.putpixel((loop, y), c)

def horizontal_grid(im,d,c):
	for loop in range(0,im.size[1],d):
		horizontal_ligne(im, loop, c)

def diagonale(im,c):

	if im.size[0] > im.size[1]:
		i = 0
	else:
		i = 1

	L = im.size[i]
	l = im.size[1-i]

	cord = [0,0]

	for loop in range(L):
		cord[i] = loop
		cord[1-i] = floor((loop / L)*l)
		im.putpixel(cord, c)

def garde_rouge(im, c):
	im = im.copy()
	col = [0,0,0]
	for i in range(im.size[0]):
		for j in range(im.size[1]):
			col[c] = im.getpixel((i,j))[c]
			im.putpixel((i,j), tuple(col))

	return im

def garde_moyen(im):
	im = im.copy()
	for i in range(im.size[0]):
		for j in range(im.size[1]):
			c = int((im.getpixel((i,j))[0] + im.getpixel((i,j))[1] + im.getpixel((i,j))[2])/3)
			col = [c,c,c]
			im.putpixel((i,j), tuple(col))

	return im
def all(im):
	im = im.copy()

	for i in range(im.size[0]):
		for j in range(im.size[1]):
			col=[255, 0, 0, 100]
			im.putpixel((i,j),tuple(col))

	return im

def reverse_horizontaly(im):
	for loop in range(im.size[1]//2):
		pass



garde_rouge(img, 2)

img_f = pil.new("RGB",(img.size[0]*5, img.size[1]))
li = [the.copy(), garde_rouge(img, 0), garde_rouge(img, 1), garde_rouge(img, 2), garde_moyen(img)]
for idx, im in enumerate(li):
	for i in range(im.size[0]):
		for j in range(im.size[1]):
			img_f.putpixel((im.size[0] * idx + i, j),im.getpixel((i,j)))


img_f.show()
