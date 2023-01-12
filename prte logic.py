def xor(a, b):
	if a != b:
		if a:
			return True
		if b:
			return True
	return False


binaire_lst = [(0,0) ,(1, 0), (0 , 1), (1, 1)]

for loop in binaire_lst:
	print(loop ,xor(*loop))