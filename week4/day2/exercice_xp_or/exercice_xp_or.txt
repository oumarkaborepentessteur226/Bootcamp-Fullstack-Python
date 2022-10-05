#Exercice 1 : Concaténer Des Listes
list1 = [111,22,22,11,55]
list2 = [2111,5522,2442,1441,2255]
list1.extend(list2)
print(list1)

#Exercice 2 : Plage De Nombres
for x in range(1500,2501) :
    if x%5 == 0 and x%7 == 0 :
        print(x)

#Exercice 3 : Vérifier L'index
names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
nom = input("Entrez votre nom : ")
if nom in names :
    print("Index",names.index(nom))

#Exercice 4 : Le Plus Grand Nombre
nombre = input("Input the 1st number: ")
nombre1 = input("Input the 2nd number: ")
if nombre1 > nombre :
    nombre = nombre1
nombre1 = input("Input the 3rd number: ")
if nombre1 > nombre :
    nombre = nombre1
print("Le plus grand nombre est",nombre)

#Exercice 5 : L'alphabet
alphabet = []
for i in range(ord("a"),ord("z")) :
    alphabet.append(chr(i))

for x in alphabet :
    if x == "a" or x == "e" or x=="i" or x=="o" or x=="u" :
        print(x," est une voyelle")
    else :
        print(x,"est une consonne")

#Exercice 6 : Mots Et Lettres
words = []
words.append(input("Entrez le 1 er mot :"))
for i in range(1,7) :
    print("Entrez le", i+1, "ième mot : ")
    words.append(input())
letter = input("Entrez maintenant une lettre : ")
for word in words :
    if letter in word :
        print("Dans le mot",word,"l'index de la première apparition de ",letter,"est",word.index(letter))
    else :
        print("Mot :",word,"Lettre :",letter)

#Exercice 7 :
nombre = []
for i in range(1,1000001) :
    nombre.append(i)
print(min(nombre))
print(max(nombre))
print(sum(nombre))

#Exercice 8 : Liste Et Tuple
nombres = input("Entrez des nombres séparés par des virgules")
print(nombres.split(","))
print(tuple(nombres.split(",")))

#Exercice 9 : Nombre Aléatoire
import random
gagner = 0
perdu = 0
while 1 :
    nombre = input("Entrez un nombre de 1 à 9 : ")
    alea = random.randint(1,9)
    if int(nombre) == alea :
        print("WINNER")
        gagner += 1
    else :
        print("Good luck for the next time")
        perdu += 1
    stop = input("Voulez vous arrêter ? ? oui ou non : ")
    if stop.lower() == "oui" :
        break
print("\nTotal Victoire : ",gagner,"\nTotal Défaite :",perdu)





