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


def distance_to_point(p, x, y):
	return np.sqrt((p[0]-x)**2 + (p[1]-y)**2)


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


if __name__ == '__main__':
	n = 30
	points_lst = [random_pos(W, H) for loop in range(n)]
	dist_arr_lst = [distance_to_point(p, X, Y) for p in points_lst]
	# for point in points_lst:
	# 	plt.plot(*point, 'w.')

	plt.imshow(create_color_matrice_V2(*dist_arr_lst))
	plt.show()
