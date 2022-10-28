import time as ti

"""
I
	1) 2**4 = 16
	2) 2**10 = 1024
II
	1)1+2+4 H 2+8+16+32+1 = 7H59
	2)4H+1H+32m+16m+4m+2m+1m
	3)oui dans le formats 12h-12h mais pas dans le format 24H
	4)32+16+8+4+2+1 = 63 (il n'y a pas 63 min dans une H)
	5)4+16h32+8+4+2 = 20H46
III
	1)a)255 b)2019
	2)a)512 b)111111111_2 = 511_10
	3) a)
	0: 0
1 :1
2 :10
3 :11
4 :100
5 :101
6 :110
7 :111
8 :1000
9 :1001
10 :1010
11 :1011
12 :1100
13 :1101
14 :1110
15 :1111
	b)50 : 110010

	c)1000 : 1111101000

	4)a) 4 bit b) 20bit

	IV)
		1)31
		2)1023
	V)
		1)
			a) a+b = 10010
			b) c-b = 1101
		2)
			a)	ab = 1000001
			b) 	d:b

2**nde njf
"""



caractere = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
					  'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def deciversbase(b, n):
	gstr = ''
	x = 0
	y = 0
	z = 0
	while x <= n:
		y += 1
		x = b ** y

	y -= 1
	while y >= 0:
		x = b ** y
		z = int(n / x - ((n / x) % 1))
		gstr += caractere[z]
		n = n - int(z * b ** y)
		y -= 1
	return gstr

def deciversbaseV2(n, base=2):
	resultat = []
	while n != 0:
		resultat.insert(0, caractere[n % base])
		n = n//base
	return "0b".join(resultat)

def baseversdeciV2(n, base):
	a = []
	for loop in n:
		a.append(caractere.index(loop))
	b = len(a)-1
	x = 0
	print(a)
	for loop in a:
		x += loop*(base**b)
		b -= 1
	return x




deciversbaseV2(59, 16)
print(baseversdeciV2('11111111', 2))
def deciversbaseV2(n, base=2):
	resultat = []
	while n != 0:
		resultat.insert(0, caractere[n % base])
		n = n//base
	return "".join(resultat)

def deciversbaseV3(n, base):
	resultat = ''
	while n != 0:
		resultat = caractere[n % base] + resultat
		n = n//base
	return resultat

def deciversbaseV4(n, base):
	resultat = ''
	Q=1
	while Q != 0:
		resultat = caractere[n % base] + resultat
		Q = n//base
		n = Q
	return resultat

def base_vers_deciV1(str):
	"""
	:param str: la chainne de caracter en binaire
	:return:
	"""
	a = []
	for loop in str:
		a.append(caractere.index(loop))
	base = 2
	b = len(a) - 1
	x = 0
	for loop in range(b + 1):
		y = base ** loop
		x += int(a[b]) * y
		b -= 1
	print(x)

base_vers_deciV1('')
