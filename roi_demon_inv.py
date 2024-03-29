from inventaire import *

roi_demon = {
    'xp' : {
        "lvl": 666,
        "xp" : 0,
        "lvlnext": 666,
    },
    'hands' :{
        'hand1' : None,
        'armor' : 'Armure des Abysse'
    },
    'gold' : {
        'Argent' : 666,
    },
    'inv' : {
        'Potion de soin n3' : 20,
        'Potion de mana n3' : 10,
        },
    'equipement' : {

    },
    'armor' :{
        'Armure des Abysse' : 0,
    }
}
Roi_demon_stats = ["Roi Démon", 180, 200, 150, 1, 1600, 90, 5, 4, 0, 150, 5, 4, 60, 150]
# significations : (0)nom, (1)attaque mini, (2)attaque max, (3)défense, (4)multiplicateur de dégat (arme), (5)vie, (6)précision, (7)chance de coup bas, (8)niveau de coup bas, (9)xp coup bas, (10)mana, (11)esquive, (12)attques magiques, (13) PV max, (14) MP max, (15) defense mini



def win_roi(enemie):
    print("Victoire !")
    print("Vous gagnez contre", enemie["nom"],".")


#a utiliser quand le hero trouve un coffre
def pierre_sword_roi(): #mettre le numéro du coffre
    print("Voulez vous retirer l'épée ?.")
    print("1. Oui")
    print("2. Non")    
    while True:
        choix = input("Choix :")
        if str(choix) == "":
            print("Choix indisponnible.")
        else:
            if int(choix) >= 1 or int(choix) <= 2:
                if int(choix) == 1:
                    use_equipement_wapon_roi()
                    choix =0
                    return
                elif int(choix) == 2:
                    choix = 0
                    return
                else:
                   print("Choix indisponnible.")


def print_objet_roi():
    Kinv = roi_demon['inv'].keys() #transformation de l'inv en liste
    Iinv = roi_demon['inv'].values()
    Kinv_list = list(Kinv)
    Iinv_list = list(Iinv)
    for n in range(len(Kinv_list)) :
        print(n+1,Kinv_list[n],"n°:",Iinv_list[n])


def use_objet_roi() :
    print("objet")
    print("Vie :", Roi_demon_stats[5],"/",Roi_demon_stats[13], "Mana :", Roi_demon_stats[10], "/", Roi_demon_stats[14])
    print_objet_roi()
    Kinv = roi_demon['inv'].keys()
    Kinv_list = list(Kinv)
    while True :
        Ninv = input("Utiliser quel obejt ? :")
        if str(Ninv) == "":
            print("Choix indisponnible.")
        else:
            if int(Ninv) < 1 or int(Ninv) > len(index_objet):
                print("Choix indisponnible.")
            else:
                objet = Kinv_list[int(Ninv)-1]
                if len(index_objet[str(objet)]) >= 2:
                    print("Vous utilisez ",objet,".")
                    if index_objet[str(objet)][2] == 1:
                        print("Vous gagnez ",index_objet[str(objet)][1],"Pv.")
                        Roi_demon_stats[5] += index_objet[str(objet)][1]
                        if Roi_demon_stats[5] > Roi_demon_stats[13] :
                            Roi_demon_stats[5] = Roi_demon_stats[13]
                        print("")
                        print("Vie :", Roi_demon_stats[5],"/",Roi_demon_stats[13], "Mana :", Roi_demon_stats[10], "/", Roi_demon_stats[14])
                        return
                    elif index_objet[str(objet)][2] == 2:
                        print("Vous gagnez ",index_objet[str(objet)][1], "Pm.")
                        Roi_demon_stats[10] += index_objet[str(objet)][1]
                        if Roi_demon_stats[10] > Roi_demon_stats[14] :
                            Roi_demon_stats[10] = Roi_demon_stats[14]
                        print("")
                        print("Vie :", Roi_demon_stats[5],"/",Roi_demon_stats[13], "Mana :", Roi_demon_stats[10], "/", Roi_demon_stats[14])
                        print("Utiliser un autre obejt ? :")
                        print("1. oui")
                        print("2. non")
                        while True:
                            choix = input("Choix :")
                            if str(choix) == "":
                                print("Choix indisponnible.")
                            else:
                                if int(choix) >= 1 or int(choix) <= 2:
                                    if int(choix) == 1:
                                        use_objet_roi()
                                        return
                                    elif int(choix) == 2:
                                        return
                                else:
                                    print("Choix indisponnible.")




def print_equipement_roi():
    Kequipement = roi_demon['equipement'].keys()
    Iequipement = roi_demon['equipement'].values()
    Kequipement_list = list(Kequipement)
    Iequipement_list = list(Iequipement)
    for n in range(len(Kequipement_list)):
        print(n+1,Kequipement_list[n],"n°:",Iequipement_list[n])


def use_equipement_wapon_roi():
    from index import index_wapone
    if roi_demon['hands']['hand1'] == None:
        print_equipement_roi()
        wapone = str(input("Quelle equipement :"))
        Kequipement = roi_demon['equipement'].keys()
        Kequipement_list = list(Kequipement)
        wapone_equipement = Kequipement_list[int(wapone)-1]
        roi_demon['hands']['hand1'] = str(wapone_equipement)
        bonus = index_wapone[str(wapone_equipement)][0]
        combat.Roi_demon_stats[4] += bonus
        print("Vous équipez", wapone_equipement)
        roi_demon['equipement'][str(wapone_equipement)] -= 1
        return

    elif roi_demon['hands']['hand1'] != None:
        print("Voulez vous le retirer ?")
        print("1. Oui")
        print("2. Non")
        choix = 0
        while True:
            choix = input("Choix :")
            if str(choix) == "":
                print("Choix indisponnible.")
            else:
                if int(choix) >= 1 or int(choix) <= 2:
                    if int(choix) == 1:
                        remove_equipement_roi(roi_demon['hands']['hand1'])
                        return
                    elif int(choix) == 2:
                        return
                else:
                    print("Choix indisponnible.")


def remove_equipement_roi(wapone) :
    roi_demon['hands']['hand1'] = None
    combat.Roi_demon_stats[4] = 1
    roi_demon['equipement'][str(wapone)] = 1
    print("Équiper un objet à la place ?")
    print("1. Oui")
    print("2. Non")
    while True:
        choix = input("Choix :")
        if str(choix) == "":
            print("Choix indisponnible.")
        else:
            if int(choix) >= 1 or int(choix) <= 2:
                if int(choix) == 1:
                    use_equipement_wapon_roi()
                    choix =0
                    return
                elif int(choix) == 2:
                    choix = 0
                    return
            else:
                print("Choix indisponnible.")


def print_armor_roi():
    Karmor = roi_demon['armor'].keys()
    Iarmor = roi_demon['armor'].values()
    Karmor_list = list(Karmor)
    Iarmor_list = list(Iarmor)
    for n in range(len(Karmor_list)):
        print(n + 1, Karmor_list[n], "n°:", Iarmor_list[n])


def use_equipement_armor_roi():
    from index import index_wapone
    if roi_demon['hands']['armor'] == None:
        print_armor_roi()
        armor = str(input("Quelle armure :"))
        Karmor = roi_demon['armor'].keys()
        Karmor_list = list(Karmor)
        armor_equipement = Karmor_list[int(armor)-1]
        roi_demon['hands']['armor'] = str(armor_equipement)
        bonus = index_armor[str(armor_equipement)][0]
        combat.Roi_demon_stats[3] += bonus
        print("Vous équipez", armor_equipement)
        roi_demon['armor'][str(armor_equipement)] += 1
        return

    elif roi_demon['hands']['armor'] != None:
        print("Voulez vous le retirer ?")
        print("1. Oui")
        print("2. Non")
        choix = 0
        while True:
            choix = input("Choix :")
            if str(choix) == "":
                print("Choix indisponnible.")
            else:
                if int(choix) >= 1 or int(choix) <= 2:
                    if int(choix) == 1:
                        remove_armor_roi(roi_demon['hands']['armor'])
                        choix = 0
                        return
                    elif int(choix) == 2:
                        choix = 0
                        return
                else:
                    print("Choix indisponnible.")


def remove_armor_roi(armor) :
    combat.Roi_demon_stats[3] = combat.Roi_demon_stats[15]
    roi_demon['armor'][str(armor)] += 1
    roi_demon['hands']['armor'] = None
    print("Équiper un objet à la place ?")
    print("1. Oui")
    print("2. Non")
    while True:
        choix = input("Choix :")
        if str(choix) == "":
            print("Choix indisponnible.")
        else:
            if int(choix) >= 1 or int(choix) <= 2:
                if int(choix) == 1:
                    use_equipement_armor_roi()
                    choix = 0
                    return
                elif int(choix) == 2:
                    choix = 0
                    return
            else:
                print("Choix indisponnible.")



def menu_roi() :
    print("Voulez vous faire quelque chause ?")
    print("1. Inventaire")
    print("2. Sauvgarder")
    print("3. Continuer")
    while True :
        choix = input("Choix :")
        if str(choix) == "":
            print("Choix indisponnible.")
        else:
            if int(choix) >= 1 or int(choix) <= 3:
                if int(choix) == 1 : #inventaire
                    print(roi_demon['gold']['Argent'], "or.")
                    print("1. Objet")
                    print("2. Équipement")
                    print('3. Retour')
                    while True:
                        choix = input("Choix :")
                        if str(choix) == "":
                            print("Choix indisponnible.")
                        else:
                            if int(choix) >= 1 or int(choix) <= 3:
                                if int(choix) == 1:
                                    print("Vie :", Roi_demon_stats[5],"/",Roi_demon_stats[13], "Mana :", Roi_demon_stats[10],"/",Roi_demon_stats[14])
                                    print_objet_roi()
                                    print("1. Utiliser un objet")
                                    print("2. Retour")
                                    while True:
                                        choix = input("Choix :")
                                        if str(choix) == "":
                                            print("Choix indisponnible.")
                                        else:
                                            if int(choix) >= 1 or int(choix) <= 2:
                                                if int(choix) == 1:
                                                    use_objet_roi()
                                                    menu_roi()
                                                elif int(choix) == 2:
                                                    menu_roi()
                                            else:
                                                print("Choix indisponnible.")
                                elif int(choix) == 2:
                                    if roi_demon['hands']['hand1'] != None:
                                        print("Vous avez", roi_demon['hands']['hand1'], "d'équipé.")
                                    if roi_demon['hands']['armor'] != None:
                                        print("Vous avez", roi_demon['hands']['armor'], "d'équipé.")
                                    print("1. Equiper une arme")
                                    print("2. Equiper une armure")
                                    print("3. Retour")
                                    while True:
                                        choix = input("Choix :")
                                        if str(choix) == "":
                                            print("Choix indisponnible.")
                                        else:
                                            if int(choix) >= 1 or int(choix) <= 2:
                                                if int(choix) == 1:
                                                    use_equipement_wapon_roi()
                                                    menu_roi()
                                                elif int(choix) == 2:
                                                    use_equipement_armor_roi()
                                                    menu_roi()
                                                elif int(choix) == 3:
                                                    menu_roi()
                                            else:
                                                print("Choix indisponnible.")
                                elif int(choix) == 3:
                                    menu_roi()
                            else:
                                print("Choix indisponnible.")
                elif int(choix) == 2 : #sauvgarder :
                    print("Êtes vous sur de vouloir sauvegarder ?")
                    print("1. oui")
                    print("2. non")
                    while True:
                        choix = input("Choix :")
                        if str(choix) == "":
                            print("Choix indisponnible.")
                        else:
                            if int(choix) >= 1 or int(choix) <= 2:
                                if int(choix) == 1:
                                    save(roi_demon, history)
                                    print("Voulez vous quiter ?")
                                    print("1. oui")
                                    print("2. non")
                                    while True:
                                        choix = input("Choix :")
                                        if str(choix) == "":
                                            print("Choix indisponnible.")
                                        if int(choix) == 1 or int(choix) == 2:
                                            if int(choix) == 1:
                                                titlebis()
                                                return
                                            elif int(choix) == 2:
                                                menu_roi()
                                        else:
                                            print("Choix indisponnible.")
                                elif int(choix) == 2:
                                    menu_roi()
                            else:
                                print("Choix indisponnible.")
                elif int(choix) == 3:
                    return
            else:
                print("Choix indisponnible.")


menu_roi()