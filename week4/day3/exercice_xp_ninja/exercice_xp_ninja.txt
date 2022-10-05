#Exercice 1 : Voitures
#1
marque = "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet"
#2
marque = marque.split(", ")
#3
print("Le nombre de fabricants est : ",len(marque))
#4
marque.sort( reverse = True)
print(marque)
#5
nbr = 0
for x in marque :
    if "o" in x :
        nbr += 1
print("Il ya ",nbr,"noms de fabricants qui contiennent la lettre 'o'")
nbr = 0
for x in marque :
    if "i" not in x :
        nbr += 1
print("Il ya ",nbr,"noms de fabricants qui ne contiennent pas la lettre 'i'")
#6
marque = ["Honda","Volkswagen", "Toyota", "Ford Motor", "Honda", "Chevrolet", "Toyota"]
marque = list(set(marque))
marqu = ""
for x in range(0,len(marque)) :
    if x == len(marque)-1 :
        marqu += marque[x]
    else :
        marqu += marque[x] + ", "
print(marqu)

#7
marque.sort()
marqu = ""
for x in marque :
    list(x)
    mot = ""
    for i in range((len(x)-1),-1,-1) :
        mot += x[i]
    marqu += mot + "\n"
print(marqu)