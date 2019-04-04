"""
@name rendu_monnaie.py
@authot Aélion
@version 0.0.1
A poor coins counter
"""

#Lecture du montant
billet100 = 0
billet50 = 0
billet20 = 0
billet10 = 0
billet5 = 0
piece2 = 0
piece1= 0

montant = 687
somme = 672
monnaie = somme - montant
if monnaie > 0:
    print("TOTAL:", montant, "€\n")
    print("CLIENT", somme, "€")
    #calcul de la monnaie
    billet100 = monnaie // 100
    rendu100 = monnaie % 100
    if rendu100 > 0:
        billet50 = rendu100 // 50
        rendu50 = rendu100 % 50
        if rendu50 > 0:
            billet20 = rendu50 // 20
            rendu20 = rendu50 % 20
            if rendu20 > 0:
                billet10 = rendu20 // 10
                rendu10 = rendu20 % 10
                if rendu10 > 0:
                    billet5 = rendu10 // 5
                    rendu5 = rendu10 % 5
                    if rendu5 > 0:
                        piece2 = rendu5 // 2
                        rendu2 = rendu5 % 2
                        if rendu2 > 0:
                            piece1 = rendu2 // 1
                            rendu1 = rendu2 % 1
    #print(billet100, billet50, billet20, billet10, billet5 , piece2 , piece1)
    print()
    #rendu de monnaie
    print("RENDU:", monnaie, "€")
    if (billet100 != 0):
        print(billet100, "x 100€")
    if (billet50 != 0):
        print(billet50, "x 50€")
    if (billet20 != 0):
        print(billet20, "x 20€")
    if (billet10 != 0):
        print(billet10, "x 10€")
    if (billet5 != 0):
        print(billet5, "x 5€")
    if (piece2 != 0):
        print(piece2, "x 2€")
    if (piece1 != 0):
        print(piece1, "x 1€")
    print()
else:
    if(monnaie == 0):
        print("Merci de votre achat")
    else:
        print("PAS ASSEZ !!!")
