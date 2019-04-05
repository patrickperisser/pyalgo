"""
@Passeword
@author Aélion
@version 1.0.0 
"""
import random
import string
"""
Définir longueur mot de passe et définir les caractères (maj/ponctuation/chiffre)
"""

lenghtPasseword = random.randint(8,12)
print(lenghtPasseword)
nbMaj = random.randint(1,lenghtPasseword-2)
print(nbMaj)
nbPonctuation = random.randint(1,lenghtPasseword-2-nbMaj)
print(nbPonctuation)
nbChiffre = random.randint(1,lenghtPasseword-nbMaj-nbPonctuation)
print(nbChiffre)
if lenghtPasseword-nbMaj-nbPonctuation-nbChiffre > 0:
    nbMin= lenghtPasseword-nbMaj-nbPonctuation-nbChiffre
else:
    nbMin = 0
print(nbMin)
"""
Listes des caractères utilisés 
"""
listPonctuation = ["*",",",";","/","+","-","(",")","[","]"]
"""
Déclaration des tableaux contenant les caractères du mdp
"""
passMaj = []
passPonct = []
passChiffre = []
passMin = []
"""
Remplissage des tableaux
"""
for i in range(nbMaj):
    passMaj.append((random.choice(string.ascii_letters)).upper())
print(passMaj)
for i in range(nbPonctuation): 
    passPonct.append(random.choice(listPonctuation))
print(passPonct)
for i in range(nbChiffre):
    passChiffre.append(random.randint(0,9))
print(passChiffre)
for i in range(nbMin):
    passMin.append((random.choice(string.ascii_letters)).lower())
print(passMin)

"""
génére le mdp
"""
tablo = passChiffre + passMaj + passMin + passPonct
print(tablo)
random.shuffle(tablo)
print(tablo)
mdp = ""
for i in range(lenghtPasseword):
    mdp = mdp + str(tablo[i])
print(mdp)