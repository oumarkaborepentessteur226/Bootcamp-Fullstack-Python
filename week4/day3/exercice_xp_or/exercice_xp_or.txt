birthdays = {
    "henry" : "1999/01/02",
    "helene" : "2000/02/03",
    "hamed" : "2001/03/04",
    "harry" : "2002/04/05",
    "herman" : "2003/05/06"
}
#Exercice 1 : Recherche D'anniversaire
print("\nWelcome, You can look up the birthdays "
      "of the people in the list\n")
nom = input("Entrez le nom d'une personne : ")
date = birthdays[nom.lower()]
print("La date d'anniversaire de :",nom,"est",date)

#Exercice 2 : Anniversaires Avancé
for x in birthdays :
    print(x)

nom = input("Entrez le nom d'une personne : ")
if nom not in birthdays :
    print("Désolé, nous n'avons pas les informations d'anniversaire pour ",nom)
else :
    date = birthdays[nom.lower()]
    print("La date d'anniversaire de :", nom, "est", date)

#Exercice 3 : Ajoutez Votre Propre Anniversaire
nomA = input("Entrez le nom d'une personne : ")
print("Entrez la date de naissance de :",nomA, "au format YYYY/MM/DD")
dateA = input()
birthdays[nomA] = dateA
for x in birthdays :
    print(x)

#Exercice 4 : Magasin De Fruits
#1
items = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
phrase = " Nous avons :"
for x in items :
    phrase += "\n"+x+" avec pour prix "+str(items[x])
print(str(phrase))
#2
items = {
    "banana": {"price": 4 , "stock":10},
    "apple": {"price": 2, "stock":5},
    "orange": {"price": 1.5 , "stock":24},
    "pear": {"price": 3 , "stock":1}
}
prix = 0
for x in items :
    prix += items[x]["price"]*items[x]["stock"]
print(prix)


