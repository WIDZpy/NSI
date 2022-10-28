import math as mt
import turtle


def EX3():
	a = int(input("a ? :"))
	b = int(input("b ? :"))
	c = int(input("c ? :"))
	d = int(input("d ? :"))

	if a == c:
		print("les droite son paralléle")
	else:
		inter_point = (d-b)/(a-c), (a*d-b*c)/(a-c)
		print(inter_point)

def EX4():
	n = int(input("le nombre de devoire(s)\n"))
	lst = []
	somme_note_X_coef = 0
	somme_coef = 0

	for loop in range(n):
		lst.append([float(input(f"not  N°{loop+1}: ")), float(input(f"coef N°{loop+1}: "))])

	for note ,coef in lst:
		somme_note_X_coef += note * coef
		somme_coef += coef

	print(somme_note_X_coef/somme_coef)

def EX4_2():
	n = int(input("le nombre de devoire(s)\n"))

	somme_note_X_coef = 0
	somme_coef = 0

	for loop in range(n):
		note = float(input(f"not  N°{loop+1}: "))
		coef = float(input(f"coef N°{loop+1}: "))
		somme_coef += coef
		somme_note_X_coef += coef * note

	print(somme_note_X_coef / somme_coef)

def EX5():
	car = input("caractaire :\n")
	ligne = range(int(input('nombre de ligne\n')))
	colone = range(int(input('nb de colone \n')))
	for loop in ligne:
		for looop in colone:
			print(car, end='')
		print()

def EX6():
	for loop in range(100):
		if loop % 3 == 0:
			print("fizz", end="")
		if loop % 5 == 0:
			print("buzz", end="")
		if loop % 5 != 0 or loop % 3 != 0:
			print(loop, end="")
		print()

def EX7():
	while True:
		a = float(input('a = '))
		if a != 0:
			break
		print("a doit etre diferent de 0")

	b = float(input('b = '))
	c = float(input('c = '))

	delta = b**2 - 4 * a * c

	if delta < 0:
		print("la f° n'admet aucune solution")
	elif delta == 0:
		print("delta est nul la f° admet 1 racine x0 :", (b * -1)/(2 * a))
	else:
		print(f"delta est positif la f° admet 2 racine : \n X1 = {((0-b) - mt.sqrt(delta))/(2*a)}		et		X2 = {((0 - b) + mt.sqrt(delta)) / (2 * a)}" )

def EX8(n):
	if n < 0: # <=> if not n >= 0:
		print("n incorect")
		return
	n = str(n)
	return len(n)

def EX9():
	n = int(input("un entier strictement pausitif :\n"))
	if n <= 0:
		print("n n'est pas valid")
		return

	while n != 1: # en partent du principe que la conjecture est vrais le vol atérira toujour en bouclan sur {4;2;1;4;2;1;...}
		if n % 2 == 0:
			n /= 2
		else:
			n = 3 * n + 1

		print(int(n))
	print("le vol a atterie")

#EX10

def testTriengle(a,b,c):
	# on utilise l'inégaliter triangulaire
	A = b+c > a
	B = a+c > b
	C = a+b > c
	return A and B and C


def testPythagore(a,b,c):
	return a**2 + b**2 == c**2

def testNatureTriangle(a,b,c):
	nature = ""

	if testTriengle(a,b,c):
		if testPythagore(a,b,c) or testPythagore(a,c,b) or testPythagore(b,a,c) or testPythagore(b,c,a) or testPythagore(c,a,b) or testPythagore(c,b,a): # c'est long
			nature += "rectangle   "
		if a == b == c:
			nature += "equilateral   "
		elif a==b or b==c or c==a :
			nature += "isosel   "
		return nature
	else:
		return "a,b,c n'est pas un triangle"

if __name__ == '__main__':
	while True: #
		print(EX5())   # permet de tester plusieur foix de suite sans tout relancer
		input() #
































