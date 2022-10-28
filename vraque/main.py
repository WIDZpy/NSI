from random import randint
def prix1(couleur, masse):
	if couleur == 'rouge' or masse > 200:
		return 2
	else:
		return 1
def prix2(couleur, masse):
	if couleur == 'rouge' or masse > 200:
		return 2
	else:
		if couleur == 'vert' and masse > 100:
			return 1.5
		else:
			return 1


couleur_lst = ['rouge', 'rouge', 'rouge', 'vert', 'vert', 'vert']
masse_lst = [80, 300, 150, 80, 300, 150]

for loop in range(6):
	print(couleur_lst[loop], masse_lst[loop], 'prix1', prix1(couleur_lst[loop],masse_lst[loop]))
	print(couleur_lst[loop], masse_lst[loop], 'prix2', prix2(couleur_lst[loop],masse_lst[loop]))

def lance_de():
	return randint(1, 6)

def somme_deux_des(resultat):
	somme = lance_de() + lance_de()
	compte = 1
	while somme != resultat:
		somme = lance_de() + lance_de()
		compte += 1
	return compte
print(somme_deux_des(7))

def somme_des_carre(n):
	resultat = 0
	for loop in range(1, n+1):
		resultat += loop ** 2

	return resultat

print(somme_des_carre(5))

def pptentier_sup(n):
	somme = 0
	compteur = 0
	while somme < n:
		compteur += 1
		somme += compteur**2
		print(f'{compteur} au carré = {compteur**2} et la somme done {somme}')
	return compteur

print(pptentier_sup(10**9))

def nb_ocurence(letrre='l', texte='Hellow, world !'):
	compteur = 0
	for loop in texte:
		if loop == letrre:
			compteur += 1
	return compteur

print(nb_ocurence())

def plus_grand_nb_ocur(text='Hellow, world !'):
	nbr_max_aucur=0
	caractaire = ''
	pluriel = False
	ban_leter = []

	for textletre in text:
		if not textletre in ban_leter:
			x = nb_ocurence(textletre, text)
			print('&', x, nbr_max_aucur)
			if x > nbr_max_aucur:
				nbr_max_aucur = x
				caractaire = textletre
				pluriel = False
			elif x == nbr_max_aucur:
				print('== ', textletre)
				caractaire = caractaire + textletre
				pluriel = True
			ban_leter.append(textletre)
			print(ban_leter)
	return caractaire, nbr_max_aucur, pluriel
phrase = input("phrase:")
resulta = plus_grand_nb_ocur(phrase)
print(resulta)

if not resulta[2]:
	corectsenters = '''La letre que l'on retrouve le plus est "''' + resulta[0] + f'" avec {resulta[1]} exemplair'
else:
	corectsenters =  """les letres que l'on retrouve le plus sont """+"".join([i + " et "  for i in resulta[0]])[:-4] + f' avec {resulta[1]} exemplairs chacune'
print(f'''dan la phrase : "{phrase}" ''' + corectsenters)



#print(f'''\n{"La letre que l'on retrouve le plus est "+resulta[0] if not resulta[2] else """les letres que l'on retrouve le plus sont """+"".join([i + " et "  for i in resulta[0]])[:-4]} avec {resulta[1]} exemplair{"s" if resulta[2] else ""}''')
