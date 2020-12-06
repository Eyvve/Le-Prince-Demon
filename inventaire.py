
from random import *
from collections import *
from index import *
from mob import *
from sauvgarde import *
from combat import *

#permet de fusioner les inventaires ou l'xp gagner au combat
#exemple : updating(char['inv'], gobelin['inv'])
#exemple : updating(char['xp'], gobelin['xp'])
def updating(objetupdate1, objetupdate2):
    for k, v in objetupdate2.items():
        if k in objetupdate1:
            objetupdate1[k] += objetupdate2[k]
        else:
            objetupdate1[k] = objetupdate2[k]

# permet la monter de niveau du hero
# exemple : update_niv(char['xp'])
def update_niv(xp1) :
    while xp1['xp'] >= xp1['lvlnext'] :
        xp1['lvl'] += 1
        xp1['xp'] -= xp1['lvlnext']
        xp1['lvlnext'] = round(xp1['lvlnext'] * 1.5)
        print("Félicitation vous avez gagner 1 niveau")
        print("vous êtes au niveau", xp1['lvl'])
        update_stats(char['stats'])


# permet la monter des stats du hero quand il gagne un niveau
# exemple : update_niv(char['stats'])
def update_stats(stats1) : #changer par les stats utiliser en combat (Dorian)
    a = 0
    b = 2
    c = 3
    d = 5
    e = 7
    stats1['atk'] = stats1['atk'] + randint(a, c)
    stats1['def'] = stats1['def'] + randint(a, c)
    stats1['mp'] = stats1['mp'] + randint(b, d)
    hp = randint(d, e)
    stats1['hp'] += hp
    stats1['maxhp'] += hp
    print("Atk = ",  stats1['atk'])
    print("Def = ", stats1['def'])
    print("Mp = ", stats1['mp'])
    print("hp = ", stats1['hp'])


#permet de fusioner les inventaires en cas de défaite.
#exemple : updating(char[inv], defeated[inv])
def update_defaite(d1, d2):
    for k, v in d2.items():
        if k in d1:
            d1[k] -= d2[k]
        else:
            d1[k] = d2[k]


#a utiliser quand le hero gagne un combat
def win(enemie):
    print("Victoire !")
    print("Vous gagnez", enemie["xp"],".")
    print("Le ", enemie["nom"], " avait sur lui ", enemie["inv"], "et", enemie["gold"],".")
    updating(char['inv'], enemie['inv']) #gaint des drops de l'enemie
    updating(char['xp'], enemie['xp']) # gaint de l'xp de l'enemie
    updating(char['gold'], enemie['gold'])
    update_niv(char['xp']) #monté de niveau du hero si possible


#a utiliser quand le hero perd un combat
def defeat():
    print("Vous êtes mort.")
    update_defaite(char['gold'], defeated['gold'])


#a utiliser quand le hero trouve un coffre
def chest(coffreN): #mettre le numéro du coffre
    print("Vous ouvrez le coffre.")
    print("Il contenait ", coffreN["inv"],".")
    updating(char['inv'], coffreN["inv"])


def print_objet():
    Kinv = char['inv'].keys() #transformation de l'inv en liste
    Iinv = char['inv'].values()
    Kinv_list = list(Kinv)
    Iinv_list = list(Iinv)
    for n in range(len(Kinv_list)) :
        print(n+1,Kinv_list[n],"n°:",Iinv_list[n])

def print_objet_sell():
    Kinv = char['inv'].keys() #transformation de l'inv en liste
    Iinv = char['inv'].values()
    Kinv_list = list(Kinv)
    Iinv_list = list(Iinv)
    for n in range(len(Kinv_list)) :
        print(n+1,Kinv_list[n],"n°:",Iinv_list[n]," Prix :",index_objet[Kinv_list[n]][0])


def use_objet() :
    print("objet")
    from combat import Prince_stats
    print_objet()
    Kinv = char['inv'].keys()
    Kinv_list = list(Kinv)
    while True :
        Ninv = int(input("Utiliser quel obejt ? :"))
        if Ninv < 1 or Ninv > len(index_objet):
            print("Choix indisponnible.")

        else:
            objet = Kinv_list[Ninv-1]
            if len(index_objet[str(objet)]) >= 2:
                print("Vous utilisez ",objet,".")
                if index_objet[str(objet)][2] == 1:
                    print("Vous gagnez ",index_objet[str(objet)][1],"Pv.")
                    Prince_stats[5] += index_objet[str(objet)][1]
                    if Prince_stats[5] > Prince_stats[13] :
                        Prince_stats[5] = Prince_stats[13]
                    break
                elif index_objet[str(objet)][2] == 2:
                    print("Vous gagnez ",index_objet[str(objet)][1], "Pm.")
                    Prince_stats[11] += index_objet[str(objet)][1]
                    if Prince_stats[11] > Prince_stats[14] :
                        Prince_stats[11] = Prince_stats[14]
                    break

            else:
                print("Ce n'est pas un objet utilisable.")
                break




def print_equipement():
    Kequipement = char['equipement'].keys()
    Iequipement = char['equipement'].values()
    Kequipement_list = list(Kequipement)
    Iequipement_list = list(Iequipement)
    for n in range(len(Kequipement_list)):
        print(n+1,Kequipement_list[n],"n°:",Iequipement_list[n])


def use_equipement_wapon():
    from index import index_wapone
    if char['hands']['hand1'] == None:
        print_equipement()
        wapone = int(input("Quelle equipement :"))
        Kequipement = char['equipement'].keys()
        Kequipement_list = list(Kequipement)

        wapone_equipement = Kequipement_list[wapone-1]
        char['hands']['hand1'] = str(wapone_equipement)
        bonus = index_wapone[str(wapone_equipement)][0]
        combat.Prince_stats[4] += bonus
        print("Vous équipez", wapone_equipement)
        char['equipement'][str(wapone_equipement)] -= 1
        return

    elif char['hands']['hand1'] != None:
        print("Voulez vous le retirer ?")
        print("1. Oui")
        print("2. Non")
        choix = 0
        while True:
            choix = int(input())
            if choix >= 1 or choix <= 2:
                if choix == 1:
                    remove_equipement(char['hands']['hand1'])
                    break
                elif choix == 2:
                    break
            else:
                print("Choix indisponnible.")


def remove_equipement(wapone) :
    char['hands']['hand1'] = None
    combat.Prince_stats[4] = 0
    char['equipement'][str(wapone)] += 1
    print("Équiper un objet à la place ?")
    print("1. Oui")
    print("2. Non")
    while True:
        choix = int(input())
        if choix >= 1 or choix <= 2:
            if choix == 1:
                use_equipement()
                break
            elif choix == 2:
                choix = 0
                break
        else:
            print("Choix indisponnible.")



def menu() :
    print("Voulez vous faire quelque chause ?")
    print("1. Inventaire")
    print("2. Sauvgarder")
    while True :
        choix = int(input())
        if choix >= 1 or choix <= 2:
            if choix == 1 : #inventaire
                print(char['gold'])
                print("1. Objet")
                print("2. Équipement")
                print('3. Quitter')
                while True:
                    choix = int(input())
                    if choix >= 1 or choix <= 3:
                        if choix == 1:
                            print_objet()
                            print("1. Utiliser un objet")
                            print("2. Quitter")
                            while True:
                                choix = int(input())
                                if choix >= 1 or choix <= 2:
                                    if choix == 1:
                                        use_objet()
                                        choix = 0
                                        break
                                    elif choix == 2:
                                        choix = 0
                                        break
                                else:
                                    print("Choix indisponnible.")
                        elif choix == 2:
                            print_equipement()
                            print("1. Equiper un objet")
                            print("2. Quitter")
                            while True:
                                choix = int(input())
                                if choix >= 1 or choix <= 2:
                                    if choix == 1:
                                        if char['hands']['hand1'] != None:
                                            print("Vous avez d'équipé", char['hands']['hand1'],".")
                                        use_equipement()
                                        choix=0
                                        break
                                    elif choix == 2:
                                        choix=0
                                        break
                                else:
                                    print("Choix indisponnible.")
                        elif choix == 3:
                            choix = 0
                            break
                    else:
                        print("Choix indisponnible.")

            elif choix == 2 : #sauvgarder
                print("Êtes vous sur de vouloir sauvegarder ?")
                print("1. oui")
                print("2. non")
                while True:
                    choix = int(input())
                    if choix >= 1 or choix <= 2:
                        if choix == 1:
                            save(char, history)
                            print("Voulez vous quiter ?")
                            print("1. oui")
                            print("2. non")
                            while True:
                                choix = int(input())
                                if choix >= 1 or choix <= 2:
                                    if choix == 1:
                                        choix = 0
                                        print("title()")
                                    elif choix == 2:
                                        choix = 0
                                        break
                    else:
                        print("Choix indisponnible.")

        else:
            print("Choix indisponnible.")



####in comming###

def print_armor():
    Karmor = char['armor'].keys()
    Iarmor = char['armor'].values()
    Karmor_list = list(Karmor)
    Iarmor_list = list(Iarmor)
    for n in range(len(Karmor_list)):
        print(n + 1, Karmor_list[n], "n°:", Iarmor_list[n])



def use_armor():
    from index import index_wapone
    if char['hands']['hand1'] == None:
        print_equipement()
        wapone = int(input("Quelle equipement :"))
        Kequipement = char['armor'].keys()
        Kequipement_list = list(Kequipement)

        wapone_equipement = Kequipement_list[wapone-1]
        char['hands']['hand1'] = str(wapone_equipement)
        bonus = index_wapone[str(wapone_equipement)][0]
        combat.Prince_stats[4] += bonus
        print("Vous équipez", wapone_equipement)
        char['armor'][str(wapone_equipement)] -= 1
        return

    elif char['hands']['hand1'] != None:
        print("Voulez vous le retirer ?")
        print("1. Oui")
        print("2. Non")
        choix = 0
        while True:
            choix = int(input())
            if choix >= 1 or choix <= 2:
                if choix == 1:
                    remove_equipement(char['armor']['head'])
                    break
                elif choix == 2:
                    break
            else:
                print("Choix indisponnible.")


# def remove_armor(wapone):