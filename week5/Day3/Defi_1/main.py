class Circle:
    def __init__(self, radius):
        self.radius = radius

    def aire(self):
        import math
        return math.pi * self.radius

    def __str__(self):
        return "Super"

    def __add__(self, other):
        return self.radius + other.radius

    def comp(self, other):
        if self.radius < other.radius :
            return f"Le cercle avec pour rayon {other.radius} est le plus grand."
        elif self.radius > other.radius :
            return f"Le cercle avec pour rayon {self.radius} est le plus grand."
        return "Egalité"

    def egal(self, other):
        if self.radius == other.radius:
            return True
        return False

    def trie(self,*args):
        tab = []
        for x in args:
            tab.append(x)
        for i in range(0,len(tab)):
            tmp = tab[i]
            j=i-1
            while j>=0 and tab[j].radius > tmp.radius:
                tab[j+1] = tab[j]
                j=j-1
            tab[j+1] = tmp
            print(tab)
        return tab

boite = Circle(5)
lol  = Circle(51)
lol1  = Circle(15)
lol2  = Circle(115)
lol3  = Circle(511)
lol4  = Circle(50)
print(boite)
print(boite.aire())
print(boite.comp(lol))
print(boite.egal(lol))
tab = boite.trie(lol,lol1,lol2,lol3,lol4)
for x in tab :
    print(x.radius)