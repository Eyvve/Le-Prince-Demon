def title():
    import time
    print("Pirate studios présentent...")
    time.sleep(1.5)
    print("""

██╗     ███████╗    ██████╗ ██████╗ ██╗███╗   ██╗ ██████╗███████╗    ██████╗ ███████╗███╗   ███╗ ██████╗ ███╗   ██╗
██║     ██╔════╝    ██╔══██╗██╔══██╗██║████╗  ██║██╔════╝██╔════╝    ██╔══██╗██╔════╝████╗ ████║██╔═══██╗████╗  ██║
██║     █████╗      ██████╔╝██████╔╝██║██╔██╗ ██║██║     █████╗      ██║  ██║█████╗  ██╔████╔██║██║   ██║██╔██╗ ██║
██║     ██╔══╝      ██╔═══╝ ██╔══██╗██║██║╚██╗██║██║     ██╔══╝      ██║  ██║██╔══╝  ██║╚██╔╝██║██║   ██║██║╚██╗██║
███████╗███████╗    ██║     ██║  ██║██║██║ ╚████║╚██████╗███████╗    ██████╔╝███████╗██║ ╚═╝ ██║╚██████╔╝██║ ╚████║
╚══════╝╚══════╝    ╚═╝     ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝╚══════╝    ╚═════╝ ╚══════╝╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
                                  Canonne, Delaire & Goldbronn - 2020

                      """)


def attaque():
    from random import randint
    jet = randint(1,100) 
    if jet < 10:
        print("Le dé fait", jet ,": échec critique !")
        degats = 1
    elif jet > 10 and jet <= 90:
        print("Le dé fait", jet ,": attaque réussie !")
        degats = randint(10,14)
    elif jet > 90 and jeu <= 99:
        print("Le dé fait", jet ,": réussite critique !")
        degats = randint(15,20)
    elif jet == 100:
        print("Le dé fait", jet ,": réussite ULTRA critique !")
        degats = randint(21,30)
    print(degats)
    return degats
    

def titleintro():
    import os
    os.system("cls")
    lines = ["Il y à 200 ans, une guerre entre humains et démons faisait rage...",
            "Les démons perdirent cette guerre et furent forcés à se cacher pour survivre...",
            "Les humains, paisibles, eurent l'occasion de jouir de 200 ans ans de paix...",
            "MAIS CE TEMPS EST REVOLU."]

    from time import sleep
    import sys

    for line in lines:
        sleep(1.2)         
        for c in line:          
            print(c, end='')    
            sys.stdout.flush()  
            sleep(0.05)          
        print('')
    import time
    time.sleep(1.2)
    import os
    os.system("cls")
    title()


titleintro()
print("1: lancer partie")
print("2: Charger partie")
print("3: A propos")
print("4: Quitter le jeu")
# choixmenu = str(input())
# if choixmenu == 1:
#     lancerjeu()
# elif choixmenu == 2:
#     charger()
# elif choixmenu == 3:
#     apropos()
# elif choixmenu == 4:
#     quitter()