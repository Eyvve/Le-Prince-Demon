import "menu.py"

def GameIsNotFinished():
    print("TODO tester si le jeu est gagné ou perdu")
    return True

def AskName():
    Name = "Bob"
    print("TODO demander le nom")
    return Name

def Description(Lieu):
    print("TODO Afficher une description de où est le player")  

def Movement():
    print("TODO Faire le deplacement du player")
    Lieu = "Lieu test"
    return Lieu

def Event(Lieu):
    print("TODO Combat ou Item qui se passe quand on se deplace")
    Combat()
    Item()

def Combat():
    print("TODO Combat")
    print("1. Attaquer 2. Inventaire 3. Fuir")
    if choix == 1 :
        attaquer()
    elif choix == 2 :
        inventaire()
    elif choix == 3 :
        

def inventaire ():
    print("TODO inventaire qui s'ouvre quand on le veux")


def Item():
    print("TODO Item")


