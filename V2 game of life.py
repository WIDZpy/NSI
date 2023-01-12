from copy import copy

import pygame

l = {
    '[0, 0, 0]': 0,
    '[1, 1, 1]': 0
}

pygame.init()

#Paramètres du jeu
largeur, hauteur = 500, 500  #Taille de la fenetre en pixels
framerate = 2 #Nombre d'évolutions par seconde

#Initialisation de la fenetre et de l'horloge
pygame.display.set_caption("Jeu de la vie!")
fenetre = pygame.display.set_mode((largeur, hauteur))
clock = pygame.time.Clock()

def quitter() :
    """Retourne True si on a cliqué sur la croix en haut à droite de la fenetre"""
    events = pygame.event.get()
    for event in events :
        if event.type == pygame.QUIT :
            return True
    return False

def affichage(t, fenetre, largeur, hauteur) :
    fenetre.fill((255,255,255))
    x_size = int(largeur/len(t[0]))
    y_size = int(hauteur/len(t))
    for i in range(0, len(t)) :
        for j in range(0, len(t[0])) :
            if t[i][j] == 1 :
                pygame.draw.rect(fenetre, (0,0,0), (j*x_size, i*y_size,x_size,y_size))
    pygame.display.update()


def test_config(v):
    return l.get(v, 1)


def evolution(t):
    e = len(t)-1
    t.append([0]+[test_config(str([t[e][idx],t[e][idx + 1],t[e][idx + 2]])) for idx in range(len(t[e])-2)]+[0])


#A compléter...

t = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]] # 2 Programmation du jeu de la vie 1. A modifier

gameOver = False
while not gameOver:
    affichage(t, fenetre, largeur, hauteur)
    evolution(t)
    gameOver = quitter()
    clock.tick(framerate) #Fait une pause de sorte à respecter le nombre d'évolution par seconde

pygame.quit()
