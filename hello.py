
"""
Function setting 
"""
def addition(operande1, operande2): 
    return operande1 + operande2

#first algorithm
resultat = 0 # Définition de la variable
operande1 = -5
operande2 = 5
resultat = addition(5,3) #call addition function with 5 and 3 params
print(addition(operande1, operande2))
print (resultat)
if resultat > 0:
    print ("resultat positif")
else:
    print ("resultat negatif")
