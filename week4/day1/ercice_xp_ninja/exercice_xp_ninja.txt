#Exercice1:
#La variable d'environnement PATH contient le
# chemin absolsu vers le repertoire Python

#Exercice 2 : Alias

#Exercice 3 : Sorties
#3 <= 3 < 9 # True
#3 == 3 == 3 # True
#bool(0) # False
#bool(5 == "5") # False
#bool(4 == 4) == bool("4" == "4") # True
#bool(bool(None)) # False
#    x = (1 == True)
#    y = (1 == False)
#    a = True + 4
#    b = False + 10
#
#   print("x is", x) # x is True
#   print("y is", y) # y is False #False == 0
#   print("a:", a) # 5
#   print("b:", b) # 10

#Exercice 4 : Combien De Caractères Dans Une Phrase ?
my_text = my_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, " \
                    "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. " \
                    "Ut enim ad minim veniam, quis nostrud exercitation ullamco " \
                    "laboris nisi ut aliquip ex ea commodo consequat. " \
                    "Duis aute irure dolor in reprehenderit in voluptate velit " \
                    "esse cillum dolore eu fugiat nulla pariatur. " \
                    "Excepteur sint occaecat cupidatat non proident, " \
                    "sunt in culpa qui officia deserunt mollit anim id est laborum."
print("Le nombre de caractère est : ",len(my_text))

#Exercice 5 : Mot Le Plus Long Sans Caractère Spécifique
while 1 :
    phrase = input("Entrez la phrase la plus longue possible sans "
                   "le caractère \"A\" ou taper 'oui' pour quitter : ")
    test = 0
    if phrase.lower() != "oui" :
        for x in phrase :
            if x == "A" :
                test = 1
        if test == 1 :
            print("Il ya un 'A'")
        else :
            print("Congratulation")
    else :
        break


