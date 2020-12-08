from mob import *
from index import *
from inventaire import *

def print_objet_sell():
    Kinv = char['inv'].keys() #transformation de l'inv en liste
    Iinv = char['inv'].values()
    Kinv_list = list(Kinv)
    Iinv_list = list(Iinv)
    for n in range(len(Kinv_list)) :
        print(n+1,Kinv_list[n],"n°:",Iinv_list[n]," Prix :",index_objet[Kinv_list[n]][0],"or")
    print(n + 2, "quitter")


def print_objet_buy():
    Kbuy = vendeur1['buy'].keys() #transformation de l'inv en liste
    Ibuy = vendeur1['buy'].values()
    Kbuy_list = list(Kbuy)
    Ibuy_list = list(Ibuy)
    for n in range(len(Kbuy_list)) :
        print(n+1,Kbuy_list[n],"n°:",Ibuy_list[n][0]," Coute :",index_objet_sell[Kbuy_list[n]][0],"or")
    print(n+2, "quitter" )

def sell():
    print("Argent :",char['gold']['Argent'],"or.")
    print("Vous voulez vendre quoi ?")
    print_objet_sell()
    Kinv = char['inv'].keys()
    Kinv_list = list(Kinv)
    while True:
        Ninv = str(input("Quelle objet :"))
        if int(Ninv) == len(Kinv_list) + 1:
            break
        if int(Ninv) < 1 or int(Ninv) > len(index_objet):
            print("Choix indisponnible.")
            sleep(1.0)
            final = sell()
            return
        elif Ninv == "":
            print("Choix indisponnible.")
            sleep(1.0)
            final = sell()
            return

        else:
            objet = Kinv_list[int(Ninv) - 1]
            char['gold']['Argent'] += index_objet[str(objet)][0]
            print("Vous avez vendu",objet,"vous avez maintenant", char['gold']['Argent'],"d'or")
            break




def buy(vendeur):
    print("Argent :", char['gold']['Argent'], "or.")
    print("Vous voulez acheter quoi ?")
    print_objet_buy()
    Kbuy = vendeur['buy'].keys()
    Kbuy_list = list(Kbuy)
    while True:
        Nbuy = str(input("Quelle objet :"))
        if int(Nbuy) == len(Kbuy_list) + 1:
            break
        objet = Kbuy_list[int(Nbuy) - 1]
        if int(Nbuy) < 1 or int(Nbuy) > len(Kbuy_list):
            print("Choix indisponnible.")
            sleep(1.0)
            final = buy(vendeur)
            return
        elif Nbuy == "":
            print("Choix indisponnible.")
            sleep(1.0)
            final = buy(vendeur)
            return
        elif char['gold']['Argent'] < index_objet_sell[objet][0]:
            print("Vous n'avez pas assez d'argent.")
            sleep(1.0)
            final = buy(vendeur)
            return
        elif vendeur['buy'][str(objet)][0] == 0 :
            print("Cette article n'est plus en stock.")
            sleep(1.0)
            final = buy(vendeur)
            return
        else:
            if vendeur['buy'][str(objet)][1] == 1:
                if vendeur['buy'][str(objet)][2] == 1:
                    updating(char['inv'], vendeur['inv1'])
                if vendeur['buy'][str(objet)][2] == 2:
                    updating(char['inv'], vendeur['inv2'])
            elif vendeur['buy'][str(objet)][1] == 2:
                updating(char['equipement'], vendeur['equipement'])
            elif vendeur['buy'][str(objet)][1] == 3:
                updating(char['armor'], vendeur['armor'])
            vendeur['buy'][str(objet)][0] -= 1
            char['gold']['Argent'] -= index_objet_sell[str(objet)][0]
            print("Vous avez achetez",objet,"il vous reste maintenant", char['gold']['Argent'],"or")
            rebuy(vendeur)
            break


def rebuy(vendeur):
    print("Voulez vous acheter autre chose ?")
    print("1. Oui")
    print("2. Non")
    choix = 0
    while True:
        choix = str(input())
        if int(choix) >= 1 or int(choix) <= 2:
            if choix == "1":
                final = buy(vendeur)
                break
            elif choix == "2":
                break
        else:
            print("")
        print("Choix indisponnible.")
        sleep(1.0)
        final = rebuy(vendeur)
        return

def vendeur(vendeur):
    print("boujour vous voulez quelque chose ?")
    print("1. acheter")
    print("2. vendre")
    print("3. quitter")
    choix = 0
    while True:
        choix = str(input())
        if int(choix) >= 1 or int(choix) <= 2:
            if choix == "1":
                buy(vendeur)
                break
            elif choix == "2":
                sell()
                break
            elif choix == "3":
                break
        else:
            print("")
        print("Choix indisponnible.")
        sleep(1.0)
        final = vendeur(vendeur)
        return

