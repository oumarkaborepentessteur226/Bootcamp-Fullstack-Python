#Exercice 1 : Formule
import math
C=50
H=30
nombre = input("Entrez des nombres séparés par des virgules : ")
nombres = nombre.split(",")
for D in nombres :
    Q = math.sqrt((2 * C * int(D))/H)
    print(int(Q))

#Exercice 2 : Liste D'entiers
nombre = [3, 47, 99, -80, 22, 97, 54, -23, 5, 7]
#1#2
nombres = ""
for x in nombre :
    nombres += str(x) + " "
print(nombres)
nombresT = nombre.copy()
nombresT.sort(reverse = True)
nombres = ""
for x in nombresT :
    nombres += str(x) + " "
print(nombres)
print(sum(nombre))
#3
nombreFE = []
nombreFE.append(nombre[0])
nombreFE.append(nombre[-1])
print(nombreFE)
#4
nombresSup = []
for x in nombre :
    if x > 50 :
        nombresSup.append(x)
print(nombresSup)
#5
nombresInf = []
for x in nombre :
    if x < 10 :
        nombresInf.append(x)
print(nombresInf)
#6
nombresCar = ""
for x in nombre :
    nombresCar += str(x**2) + " "
print(nombresCar)
#7
nombresD = []
for x in nombre :
    if x not in nombresD :
        nombresD.append(x)
print(nombresD)
print(len(nombresD))
#8
print(sum(nombre)/len(nombre))
#9
print(max(nombre))
#10
print(min(nombre))

#Exercice 3 : Travail Sur Un Paragraphe
#1
paragr = "Lorem ipsum dolor sit amet, consectetur adipiscing " \
         "elit, sed do eiusmod tempor incididunt ut labore et " \
         "dolore magna aliqua. Ut enim ad minim veniam, quis " \
         "nostrud exercitation ullamco laboris nisi ut aliquip " \
         "ex ea commodo consequat. Duis aute irure dolor in " \
         "reprehenderit in voluptate velit esse cillum dolore " \
         "eu fugiat nulla pariatur. Excepteur sint occaecat " \
         "cupidatat non proident, sunt in culpa qui officia " \
         "deserunt mollit anim id est laborum."
print(paragr)
#4
print("Votre paragraphe compte ",len(paragr),"caractères.")
#5
nbr = 0
for x in paragr :
    if x == "." :
        nbr += 1
print("Ce paragraphe contient ",nbr,"phrases.");
#6
mots = paragr.split(" ")
print("Il contient ",len(mots),"mots.")
#7
motsU = []
for x in mots :
    if x not in motsU :
        motsU.append(x)
    else :
        print(x)
print("Il contient :",len(motsU),"mots uniques.")

#Exercice 4
mots = "New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3."
mots = mots.split(" ")
motsU = []
for x in mots:
    if x not in motsU:
        motsU.append(x)
for x in motsU:
    nbr = 0
    for y in mots:
        if x == y:
            nbr += 1
    print(f"{x}:{nbr}")



