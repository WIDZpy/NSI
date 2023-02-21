import random
import random as rd
import time


def time_operate(action):
	a = time.time()
	action()
	return time.time() - a



def generate_group(n):
	date = {}
	for loop in range(n):
		a = random.randint(1,14_138)
		if a in date:
			return True
		else:
			date[a] = ""

	return False


def test(taile, nb):
	s = 0
	for loop in range(nb):
		if generate_group(taile):
			s += 1
	return s / nb


def conjoncture(nb):
	p = 0
	s = 1
	while p < 0.5:
		s += 1
		p = test(s, nb)
	return s



print(conjoncture(10_000))
# print(time_operate(lambda: test(23, 100_000)))
