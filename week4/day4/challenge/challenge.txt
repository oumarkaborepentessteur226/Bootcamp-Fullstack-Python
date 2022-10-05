Défi Quotidien : Résoudre La Matrice
import re
parttern = re.compile(r"(^[0-9]$)")
matrix = [["7i3"],["Tsi"],["h%x"],["i #"],["sM "],["$a "],["#t%"],["^r!"]]
msgSecret = ""
for i in range(0,3) :
    for x in matrix :
        if x[0][i] != " " and parttern.search(x[0][i]) == None:
            msgSecret += x[0][i]

secret = ""
parttern2 = re.compile(r"(^[a-zA-Z]$)")
esp =0
for x in msgSecret :
    if parttern2.search(x) != None :
        secret += x
        esp=0
    elif esp != 1 :
        secret += " "
        esp=1

print(secret)

