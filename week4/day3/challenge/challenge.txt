#Défi 1
import re
mot = input("Entrez un mot : ")
pattern = re.compile(r"(^[a-zA-Z]+$)+")
b = pattern.fullmatch(mot)

if b == None :
    print("Entrez uniquement des lettres")
else :
    dico = {}
    for i in range(0,len(mot)) :
        if mot[i] in dico :
            dico[mot[i]].append(i)
        else :
            dico[mot[i]] = [i]
    print(dico)

#Défi 2
items = {
  "Phone": "$999",
  "Speakers": "$300",
  "Laptop": "$5000",
  "PC": "$1200"
}
wallet = "$300"
liste = []
for x in items :
    if (int(items[x][1:]) < int(wallet[1:])) :
        liste.append(x)
if liste != [] :
    print(liste)
else :
    print("Nothing")



