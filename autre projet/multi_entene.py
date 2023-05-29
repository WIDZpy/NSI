import numpy as np
from matplotlib import pyplot as plt
import PIL.Image as pil
import entne
import random


class Anthene:
	def __init__(self, pos:tuple, world_size, color, vector=(0, 0)):
		self.pos = pos
		self.vector = vector
		self.world_size = world_size
		self.color = color
		self.arr_dist = None

	def moov(self, speed):
		n_x = (self.pos[0] + self.vector[0]) * speed
		n_y = (self.pos[1] + self.vector[1]) * speed
		self.pos = n_x % self.world_size[0], n_y % self.world_size[1]

	def gen_array_dist(self, X, Y):
		self.arr_dist = entne.distance_to_point(self.pos, X, Y)


class Valle:
	def __init__(self, world_size):
		self.world_size = world_size
		self.X = np.repeat(np.arange(world_size[1]).reshape(1, world_size[1]), world_size[0], 0)
		self.Y = np.repeat(np.arange(world_size[0]).reshape(world_size[0], 1), world_size[1], 1)

		self.anthene_list = []

	def gen_anthene(self, n):
		for loop in range(n):
			self.anthene_list.append(Anthene(
				(random.randrange(self.world_size[1]), random.randrange(self.world_size[0])),
				self.world_size, entne.random_color(),
				(random.random(), random.random())))

	def update_all_dist(self):
		for loop in self.anthene_list:
			loop.gen_array_dist(self.X, self.Y)

	def moov_all(self, speed):
		for loop in self.anthene_list:
			loop.moov(speed)

	def get_diagram(self):
		final = np.ones((*self.world_size, 3)).astype(np.uint8)
		for i, anthene in enumerate(self.anthene_list):
			print("\r", i, end="")
			dist_arr = anthene.arr_dist
			c = np.ones(self.world_size).astype(bool)
			color = anthene.color
			for loop in range(len(self.anthene_list) - 1):
				id = (loop + i + 1) % (len(self.anthene_list) - 1)

				c[dist_arr > self.anthene_list[loop].arr_dist] = False

			final[c] = color
		return final.copy()


if __name__ == '__main__':
	M = Valle((1_080, 1_920))
	print(M.X.shape)
	M.gen_anthene(5)
	M.update_all_dist()
	a = M.get_diagram()
	pil.fromarray(a, mode="RGB").save('test_a.png')
	M.moov_all(100)
	b = M.get_diagram()
	pil.fromarray(b, mode="RGB").save('test_b.png')


	plt.imshow(a)
	plt.show()
