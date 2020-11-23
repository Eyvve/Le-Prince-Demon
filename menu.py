
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
    menu()

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


def menu():
    print("1: lancer partie")
    print("2: Charger partie")
    print("3: A propos")
    print("4: Quitter le jeu")
    choixmenu = int(input())
    if choixmenu == 1:
        lancerjeu()
    elif choixmenu == 2:
        charger()
    elif choixmenu == 3:
        apropos()
    elif choixmenu == 4:
        quitter()   

def lancerjeu():
    print("TODO Lancer le jeu")
    PlayerName = AskName()
    while GameIsNotFinished() :
        Description("test")
        TargetMovement = Movement()
        Event(TargetMovement)

        

def charger():
    print("TODO charger")
    lancerjeu()

def apropos():
    print("TODO apropos")
    Menu()

def quitter():
    print("TODO quitter")




titleintro()

