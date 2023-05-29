import math
import random
import matplotlib.pyplot as plt

import numpy as np
W,H = 500, 500
X = np.repeat(np.arange(W).reshape(1, W), H, 0)
Y = np.repeat(np.arange(H).reshape(H, 1), W, 1)
P = 50, 50


def random_color():
	return random.randrange(255),  random.randrange(255),  random.randrange(255)

def random_arr_color(w, h):
	c = np.zeros((W, H, 3))

	c[:,:,0] = random.randrange(255)
	c[:,:,1] = random.randrange(255)
	c[:,:,2] = random.randrange(255)

	return c.astype(np.uint8)


def random_pos(w, h):
	return random.randrange(w),  random.randrange(h)


def distance_to_point_arr(p, x, y):
	return np.sqrt((p[0]-x)**2 + (p[1]-Y)**2)

def distance_to_point_point(p1, p2):
	return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def create_color_matrice_V1(m, max_value):
	a = (np.repeat(m.reshape((*m.shape, 1)), 3, 2) * (255/max_value))
	a[a > 255] = 255
	return (a).astype(np.uint8)

def create_color_matrice_V2(*matrice):
	final = np.ones((W, H, 3)).astype(np.uint8)
	for i, dist_arr in enumerate(matrice):
		c = np.ones((W, H)).astype(bool)
		color = random_color()
		for loop in range(len(matrice)-1):
			id = (loop + i + 1) % (len(matrice)-1)

			c[dist_arr > matrice[loop]] = False

		final[c] = color
		print(i)
	return final


def get_pos_plus_pres(i, n, l):
	p = l[i]
	final = []
	print(p)
	for loop in l:
		if loop != p:
			print(loop)
			if not final:
				final.append(loop)
			else:
				for id, looop in enumerate(final):
					if distance_to_point_point(p, loop) < distance_to_point_point(p, looop):
						final.insert(id, loop)
						del final[n:]
						break


	return final


if __name__ == '__main__':
	n = 30
	points_lst = [random_pos(W, H) for loop in range(n)]
	dist_arr_lst = [distance_to_point_arr(p, X, Y) for p in points_lst]
	for point in points_lst:
		plt.plot(*point, 'w.')

	print(get_pos_plus_pres(0, 3, points_lst))

	plt.imshow(create_color_matrice_V2(*dist_arr_lst))
	plt.show()
