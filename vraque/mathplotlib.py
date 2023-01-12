import matplotlib.pyplot as plt

def rectangle(point1, point2):
	return [point1[0], point2[0], point2[0], point1[0], point1[0]], [point1[1], point1[1], point2[1], point2[1], point1[1]]

def pligone(*pos, t=True):
	x = []
	y = []
	for loop in pos:
		x.append(loop[0])
		y.append(loop[1])

	if t:
		x.append(x[0])
		y.append(y[0])

	print(x,y)

	return x, y


# plt.plot(*rectangle((0,0), (5,3)), "r")
# plt.plot(*rectangle((1, 0), (2, 2)), "r")
# plt.plot(*rectangle((1, 0), (2, 2)), "r")
# plt.plot(*rectangle((3, 1), (4, 2)), "r")
# plt.plot(*pligone((0, 3), (2.5, 4), (5, 3)), "r")

def cheme(lst):
	for colone in range(3):
		for ligne in range(3):
			plt.plot(colone, ligne, "k.", ms=50)

	plt.plot(*pligone(*lst, t=False))

cheme([[2,2],[0,2],[0,1], [1,1], [2,0], [0,0]])

plt.show()
