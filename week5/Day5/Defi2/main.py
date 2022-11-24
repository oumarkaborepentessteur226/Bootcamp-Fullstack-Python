#Partie 1 : Quizz :
# Qu'est-ce qu'une classe ?
## C'est un moyen qui permet de creer un objet

# Qu'est-ce qu'une instance ?
## Objet crée grâce à une classe

# Qu'est-ce que l'encapsulation ?
## C'est une propriété des classe, elle permet d'envelopper, de cacher ses attributs,
## de telle sorte qu'ils ne puisse pas être directement manipulés depuis l'extérieur

# Qu'est-ce que l'abstraction ?
## permet à une classe de ne pas être instanciable

# Qu'est-ce que l'héritage ?
## Permet à une classe d'avoir les attributs d'une autre classe

# Qu'est-ce que l'héritage multiple ?
## Permet à une classe d'avoir les attributs de plusiers autres classes

# Qu'est-ce que le polymorphisme ?
## Capacité à prendre plusieurs formes

# Qu'est-ce que l'ordre de résolution de méthode ou MRO ?
## C'est la façon dont python va chercher les méthodes d'une classe


# Partie 2 : Créer Une Classe De Jeu De Cartes.
class Card:
    def __init__(self,couleur,valeur):
        self.couleur = couleur
        self.valeur = valeur

class Deck:
    def shuffle(self,tab):
        import random
        tab1 = []
        taille = 51
        for x in range(0,52):
            tab1.append(tab.pop(random.randint(0,taille)))
            taille -= 1
        return tab1

    def genCard(self,couleur):
        cardTab = []
        cardTab.append(Card(couleur, "A"))
        cardTab.append(Card(couleur, "J"))
        cardTab.append(Card(couleur, "Q"))
        cardTab.append(Card(couleur, "K"))
        for i in range(2,11):
            cardTab.append(Card(couleur, i))
        return cardTab

    def deal(self,tab):
        return tab.pop()

a = Deck()
pack = a.genCard("Hearts")
pack += a.genCard("Diamonds")
pack += a.genCard("Clubs")
pack += a.genCard("Spades")

for x in pack:
    print(x.couleur,x.valeur)
print()

pack = a.shuffle(pack)

for x in pack:
    print(x.couleur,x.valeur)
print()

user = a.deal(pack)

for x in pack:
    print(x.couleur,x.valeur)
print()








