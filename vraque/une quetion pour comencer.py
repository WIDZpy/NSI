import random
import random as r

def une_questin_pour_comencer():
	lst_p = ["henri"]
	lst_c = ["bleu"]

	lst_r = []

	for prenom in lst_p:
		color = lst_c[random.randint(0, len(lst_c) - 1)]
		lst_r.append((prenom,color))

	print(lst_r)

class comprention:
	def carre(self):
		L6 = []
		for loop in range(5,12):
			L6.append(loop ** 3)

	def foctio_b(self,x):
		L7 = []
		for loop in range(1,9):
			L7.append(2*loop**2-3*loop+5)

		print(L7)

	def c(self):
		L6 = []
		for loop in range(9, 22):
			L6.append(loop * loop)

	def d(self):
		R = []
		for loop in range(111, 131):
			if loop % 3 == 0 :
				R.append(loop)



class Exo2:
	def echanger(self, lst: list, a, b):
		lst[b], lst[a] = lst[a], lst[b]
		print(lst, lst)
		return lst

	def echangerbis(self, lst: list, a, b):
		lstr = lst.copy()
		lstr[b], lstr[a] = lstr[a], lstr[b]
		print(lst, lstr)
		return lstr

	def inverser(self,lst: list):
		for loop in range(len(lst) // 2):
			self.echanger(lst, loop, -1*loop-1)

		print(lst)
		return lst

class Exo3:
	def maximum(self,lst:list):
		max = lst[0]
		for loop in lst:
			max = loop if loop > max else max

		return max

	def indice_minimum(self, lst:list):
		imin = 0
		min = lst[imin]
		for index, element in enumerate(lst):
			if element < min:
				imin = index
				min = element

	def indicemin2(self, lst: list):
		imin = 0
		for loop in range(len(lst)-1):
			if lst[loop] < lst[imin]:
				imin = loop

class Exo4:
	def moin_de_six(self, l:list):
		mots_p = []
		mots_m = []
		for mots in l:
			if len(mots) < 6:
				mots_m.append(mots)
			else:
				mots_p.append(mots)

		return mots_p, mots_m

	def palidrome(self, lst:list):
		tsl = []
		for i in range(0, len(lst)-1,-1):
			tsl.append(lst[i])

		return tsl == lst


class Exo5:
	def diviseur(self, n):
		d = []
		for loop in range(2,n):
			if n % loop == 0:
				d.append(loop)

		return d

	def estPremier(self, n):
		return self.diviseur(n) == []

	def listfacteurpremier(self, n):
		rep_lst = []
		for loop in range(2, n):
			if n % loop:
				continue

			if self.estPremier(loop):
				rep_lst.append(loop)
				continue

			rep_lst += self.listfacteurpremier(loop)





class Exo6:
	def get_key(self, code: str):
		lst = [int(i) for i in code]
		s = sum(lst[0::2])
		sp = sum(lst[1::2])
		n = s + 3 * sp
		R = n % 100

		if R:
			return 10 - R
		return 0

	def is_key(self, code: str):
		return self.get_key(code[:-1]) == int(code[-1])









if __name__ == '__main__':
	ex = Exo5()

	print(ex.listfacteurpremier(4))



