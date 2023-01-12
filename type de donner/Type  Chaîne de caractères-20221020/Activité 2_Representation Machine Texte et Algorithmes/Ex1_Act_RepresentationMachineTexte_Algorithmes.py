# coding: utf-8
# noinspection PyUnresolvedReferences
import numpy as np

messageBinaire="01001100 01100101 00100000 01100010 01110101 01110100 00100000 01100100 01100101 00100000 01101100 01100001 00100000 01110011 01100011 01101001 01100101 01101110 01100011 01100101 00100000 01100101 01110011 01110100 00100000 01100100 01100101 00100000 01110000 01110010 01100101 01110110 01101111 01101001 01110010 00101100 00100000 00100000 01101110 01101111 01101110 00100000 01100100 01100101 00100000 01100011 01101111 01101101 01110000 01110010 01100101 01101110 01100100 01110010 01100101"
def retir_car(chaine):
    return chaine.replace(" ","")

def ASCIIbinaireVersCaracteres(chaine):
    """ Conversion du ASCII binaire vers la chaîne de caractères
aa    correspondant aux codes ASCII des caractères d'une phrase
    Retour : resultat chaîne de caractères correspondant au message"""
    chaine = chaine.split(" ")
    result = ''


    for letter in chaine:
        result += chr(int(letter,2))
    return result

def ASCIIbinaireVersCaracteres_V2(chaine):
    result = ""
    for _ in range(len(chaine)//8):
        result += chr(int(chaine[_*8:_*8+8],2))
    return result

def ASCIICaracteresVersBinaire(chaine):
    result = ''
    for caractere in chaine:
        result += np.binary_repr(ord(caractere) ,8)
        result += " "
    return result[:-1]




if __name__ == '__main__':
    print(ASCIICaracteresVersBinaire("€"))