"""
@name manip_tableau.py
@version 1.0.0
    Algorithmique spécifique sur les collections
"""

"""
getLowerOf function
return the lowest value of two params
"""
def getLowerOf(firstVal, secondVal):
    if firstVal < secondVal:
        return firstVal
    else: 
        return secondVal

"""
getGreaterOf function
returns the greater vealue of two params
"""
def getGreaterOf(firstVal, secondVal):
    if firstVal > secondVal:
        return firstVal
    else: 
        return secondVal

"""
compare fonction
@param firstVal First value to compare
@param secondVal Second value to compare
@param howTo Mode de comparaison souhaité
@return greater or lower value of two depends on howTo params
"""
"""
def compare(firstVal, secondVal, howTo): 
    if howTo == "greater":
        if firstVal > secondVal: 
            return firstVal
        else: 
            return secondVal
    if howTo == "lower": 
        if firstVal < secondVal:
             return firstVal
        else: 
            return secondVal
"""
"""
autre solution
"""
def compare(firstVal, secondVal, desc=True):
    if desc:
        return getLowerOf(firstVal,secondVal)

    return getGreaterOf(firstVal,secondVal)
"""
min function
@param anArray the array from which i want to get the min value
@return the min value of anArray
"""

def minim(anArray):
    theMin = anArray[0]
    for value in anArray[1:]: 
        theMin = compare(theMin, value) 

    return theMin 

"""
max function
@param anArray the array from which i want to get the max value
@return the max value of anArray
"""
def maxim(anArray):
    theMax = anArray[0]
    for value in anArray[1:]: 
        theMax = compare(theMax, value, False) 

    return theMax 

"""
averrage function
@param anArray the array from which i want to get the averrage
@return the averrage of anArray
"""

def averrage(anArray):
    total = 0
    nbItems = 0
    for val in anArray:
        total = total + val
        nbItems = nbItems + 1
    return total / nbItems

"""
factorial fonction
@param anArray the array from which i want to get the factorial
@return the factorial of anArray
"""

def factorial(anArray):
    fact = 1
    for val in anArray:
        fact = fact * val
    return fact

#Déclaration du tableau de démonstration
print("Toutes les valeurs:")
monTablo = [15, 3, 25, 12, 7, -15]
monTablo2 = [17, 32, 322, 2, 1, -53]
#Boucle
#for = Pour / Val = Valeur / in = Dans (en revu) / enumerate = 
for indice, val in enumerate(monTablo):
    print(monTablo[indice] *2)

#Boucle (loop) avec condition
print("les valeurs qui ont un indices pair:")
for indice, val in enumerate(monTablo):
    if indice % 2 == 0:
        print(monTablo[indice] *2)

#connaitre la valeur mini du tableau
print("La valeur minimum:")
minimum = monTablo[0]
for indice, val in enumerate(monTablo):
    minimum = getLowerOf(minimum, val)
print (minimum)

#connaitre la valeur maxi du tableau
print("La valeur maximum:")
maximum = monTablo[0]
for indice, val in enumerate(monTablo):
    maximum = getGreaterOf(maximum, val)

print (maximum)

#connaitre le cumul des valeurs du tableau
print("La valeur Cumul:")
cumul = 0
for indice, val in enumerate(monTablo):
    cumul = monTablo[indice] + cumul 

print(cumul)

print ("And the min is: ", minim(monTablo))

print ("And the max is: ", maxim(monTablo))

print ("And the averrage  of the 1st tablo is: ", averrage(monTablo))

print ("And the averrage of the 2nd tablo is: ", averrage(monTablo2))

print ("And the factorial of the 1st tablo is: ", factorial(monTablo))