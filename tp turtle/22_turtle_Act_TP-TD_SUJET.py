import random as rd
import turtle as tt
### Question 2
def polygone_regulier(n,lg):
    "Trace un polygone régulier à n côtés de longueur lg"    
    angl = 360/n
    for cotee in range(n):
        tt.fd(lg)
        tt.right(angl)
### Question 3
def flocon(n,lg):
    """Trace les rayons d'un polygone régulier à n côtés de longueur lg"""
    angl = 360 / n
    for cotee in range(n):
        tt.fd(lg)
        tt.bk(lg)
        tt.right(angl)

def disque_flocon(n,lg):
    """Trace les rayons d'un polygone régulier à n côtés de longueur lg
    et son cercle circonscrit"""
    flocon(n, lg)
    tt.fd(lg)
    tt.left(90)
    tt.circle(lg)
### Question 4
def triangle(pos1,pos2):
    """A partir de la position de la tortue, trace un triangle dont les
    deux autres sommets ont pour coordonnées pos1 et pos2"""
    start_pos = tt.pos()
    tt.goto(pos1)
    tt.goto(pos2)
    tt.goto(start_pos)

def flocon_remplissage_alterne(n,lg):
    """Trace un flocon à n rayons de longueur lg en remplissant le triangle
    entre deux rayons de façon alternée"""

    angl = 360 / n
    for cotee in range(n//2):
        tt.fd(lg)
        pos_1 = tt.pos()
        tt.bk(lg)
        tt.right(angl)
        tt.fd(lg)
        pos_2 = tt.pos()
        tt.bk(lg)
        tt.right(angl)
        tt.begin_fill()
        triangle(pos_1, pos_2)
        tt.end_fill()

### Question 5
###### Question 5.1 : Marche aléatoire
import random
def marche_aleatoire():
    """Crée deux objets Turtle, lievre et renard.
    lievre est rouge et initialement situé en (60,0)
    renard est verte et initialement situé en (0,0)
    Tant que renard ne se situe pas à une distance infèrieure à 1 de lievre :
    * lievre tourne d'un angle aléatoire compris entre -60° et 60° puis avance de 20
    * renard tourne en direction de lievre puis avance de 20
    Si renard se situe à moins de 1 de lievre en au plus 30 déplacements afficher GAGNE et
    le nombre de déplacements dans la console. Sinon, afficher PERDU.
    """
    lievre = tt.Turtle()
    lievre.up()
    lievre.setpos((60,0))
    lievre.down()

    renard = tt.Turtle()

    message = 'GAGNE'

    deplacement = 0

    while renard.distance(lievre.pos()) >= 1:
        if deplacement == 30:
            message = 'PERDU'
            break

        lievre.right(rd.randint(-60,60))
        lievre.forward(20)

        renard.setheading(renard.towards(lievre.pos()))
        renard.fd(20)

        deplacement += 1

    print(message, deplacement)
    return deplacement



###### Question 5.2 : Tortues qui se poursuivent
def poursuite_tortues(n=20):
    """4 tortues : tortue1 (vert), tortue2 (rouge, tortue3 (bleu), tortue4 (noir).
    Elles démarrent aux positions (-200,-200), (200,-200), (200,200), (-200,200).
    - A chacun des tours (Il y a n tours, avec par défaut n valant 20):
    chacune regarde la tortue devant elle,puis elles baissent toutes la tête et avancent de 10.
    - tortue1 suit tortue2, tortue2 suit tortue3, tortue3 suit tortue4, tortue 4 suit tortue1.
    - Variante : tracer à chaque fois un segment entre la tortue poursuivante et la tortue poursuivie 
    """
    tt.hideturtle()

    tortue1 = tt.Turtle()

    tortue2 = tt.Turtle()

    tortue3 = tt.Turtle()

    tortue4 = tt.Turtle()

    t_lst = [tortue1,tortue2,tortue3,tortue4]
    colors = ["green", "red", "blue", "black"]
    poss = [(-200,-200), (200,-200), (200,200), (-200,200)]
    targets = [tortue2,tortue3,tortue4,tortue1]
    target_pos = []

    for _ in range(4):
        t_lst[_].color(colors[_])
        t_lst[_].up()
        t_lst[_].setpos(poss[_])
        t_lst[_].down()

    for etape in range(n):
        for target in targets:
            pass




### Programme principal    
def main():
    tt.speed(10)
    marche_aleatoire()

if __name__ == "__main__":
    main()
    tt.exitonclick()
    