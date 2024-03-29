from random import *
from time import sleep
from intro import Sentence
from Music_sounds import *
from data import *
from maps import *
import pygame
import os

pygame.init()


# statistiques du mob seront intégrées à chaque évènement donc dépendra de la map et de l'ennemi
Mob_stats = ["Fermier", 6, 9, 2, 1.0, 400, 85, 5]
# significations : nom, attaque mini, attaque max, défense, multiplicateur de dégat (arme), vie, précision, esquive
Prince_stats = ["Prince", 8, 12, 2, 1.3, 60, 90, 5, 4, 0, 40, 5, 4, 60, 40]
# Prince_stats = ["Prince", 8, 12, 2, 1.3, 600, 90, 5, 4, 0, 100, 5, 4, 60, 40]
# significations : (0)nom, (1)attaque mini, (2)attaque max, (3)défense, (4)multiplicateur de dégat (arme), (5)vie, (6)précision, (7)chance de coup bas, (8)niveau de coup bas, (9)xp coup bas, (10)mana, (11)esquive, (12)attques magiques, (13) PV max, (14) MP max, (15) defense mini


def attaque_mob(name, atkmini, atkmax, df, mult, hp):
    total_atk = randint(atkmini, atkmax) * mult
    final_atk = total_atk - df
    if final_atk < 0:
        final_atk = 0
        Prince_hp_remaining = hp - final_atk
        round(Prince_hp_remaining, 0)
        print(name, "vous inflige", int(final_atk), "dégats.")
        return Prince_hp_remaining
    else:
        Prince_hp_remaining = hp - final_atk
        round(Prince_hp_remaining, 0)
        print(name, "vous inflige", int(final_atk), "dégats.")
        return Prince_hp_remaining


def attaque(name, atkmini, atkmax, df, mult, hp):
    total_atk = randint(atkmini, atkmax) * mult
    final_atk = total_atk - df
    mob_hp_remaining = hp - final_atk
    round(mob_hp_remaining, 0)
    print("vous infligez", int(final_atk), "dégats", "à", name)
    return mob_hp_remaining


def Magic_action(nivatkmag):
    if nivatkmag == 1:
        print("1. Rayon démoniaque mineur | coût : 7 mana")
        print("2. retour au menu des actions")
        rep = str(input("=> "))
        if rep == "1":
            if Prince_stats[10] >= 7:
                evil_beam_spell.play()
                Prince_stats[10] = Prince_stats[10] - 7
                magic_attack = 12
                print("vous infligez", magic_attack, "dégats magiques !")
                mob_hp_remaining = Mob_stats[5] - magic_attack
                return mob_hp_remaining
            else:
                Sentence("pas assez de mana")
                mob_hp_remaining = Magic_action(Prince_stats[12])
                return mob_hp_remaining
        elif rep == "2":
            os.system("cls")
            print(Mob_stats[0], ":", int(Mob_stats[5]), "pv", "                         ", Prince_stats[0], ":", Prince_stats[5], "pv")
            print("                                                                 Mana :", Prince_stats[10])
            mob_hp_remaining = action()
            return mob_hp_remaining
        else:
            print("veuillez entrer un chiffre valide")
            sleep(1.5)
            os.system("cls")
            print(Mob_stats[0], ":", int(Mob_stats[5]), "pv", "                         ", Prince_stats[0], ":", Prince_stats[5], "pv")
            print("                                                                 Mana :", Prince_stats[10])
            mob_hp_remaining = Magic_action(Prince_stats[12])
            return mob_hp_remaining
    elif nivatkmag == 2:
        print("1. Rayon démoniaque | coût : 9 mana")
        print("2. Soif d'âme | coût : 15 mana")
        print("3. retour au menu des actions")
        rep = str(input("=> "))
        if rep == "1":
            if Prince_stats[10] >= 9:
                evil_beam_spell.play()
                Prince_stats[10] = Prince_stats[10] - 9
                magic_attack = 15
                print("vous infligez", magic_attack, "dégats magiques !")
                mob_hp_remaining = Mob_stats[5] - magic_attack
                return mob_hp_remaining
            else:
                Sentence("pas assez de mana")
                mob_hp_remaining = Magic_action(Prince_stats[12])
                return mob_hp_remaining
        elif rep == "2":
            if Prince_stats[10] >= 15:
                absorbtion_soundeffect.play()
                Prince_stats[10] = Prince_stats[10] - 15
                magic_attack = randint(9, 11)
                print("vous absorbez", magic_attack, "dégats magiques !")
                sleep(1.0)
                recup = randint(9, 11)
                Prince_stats[5] = Prince_stats[5] + recup
                absorbtion_gain_hp.play(3)
                print("vous récupérez" , recup , "points de vie !")
                sleep(1.0)
                mob_hp_remaining = Mob_stats[5] - magic_attack
                if Prince_stats[5] > Prince_stats[13]:
                    Prince_stats[5] = Prince_stats[13]
                    return mob_hp_remaining
                else:
                    return mob_hp_remaining
            else:
                Sentence("pas assez de mana")
                mob_hp_remaining = Magic_action(Prince_stats[12])
                return mob_hp_remaining
        elif rep == "3":
            os.system("cls")
            print(Mob_stats[0], ":", int(Mob_stats[5]), "pv", "                         ", Prince_stats[0], ":", Prince_stats[5], "pv")
            print("                                                                 Mana :", Prince_stats[10])
            mob_hp_remaining = action()
            return mob_hp_remaining
        else:
            print("veuillez entrer un chiffre valide")
            sleep(1.5)
            os.system("cls")
            print(Mob_stats[0], ":", int(Mob_stats[5]), "pv", "                         ", Prince_stats[0], ":", Prince_stats[5], "pv")
            print("                                                                 Mana :", Prince_stats[10])
            mob_hp_remaining = Magic_action(Prince_stats[12])
            return mob_hp_remaining
    elif nivatkmag == 3:
        print("1. Rayon démoniaque majeur | coût : 12 mana")
        print("2. Moisson d'âme | coût : 20 mana")
        print("3. Seconde peau | coût : 15 mana")
        print("4. retour au menu des actions")
        rep = str(input("=> "))
        if rep == "1":
            if Prince_stats[10] >= 12:
                evil_beam_spell.play()
                Prince_stats[10] = Prince_stats[10] - 12
                magic_attack = 20
                print("vous infligez" , magic_attack , "dégats magiques !")
                mob_hp_remaining = Mob_stats[5] - magic_attack
                return mob_hp_remaining
            else:
                Sentence("pas assez de mana")
                mob_hp_remaining = Magic_action(Prince_stats[12])
                return mob_hp_remaining
        elif rep == "2":
            if Prince_stats[10] >= 20:
                absorbtion_soundeffect.play()
                Prince_stats[10] = Prince_stats[10] - 20
                magic_attack = randint(12, 15)
                print("vous absorbez", magic_attack, "dégats magiques !")
                sleep(1.0)
                recup = randint(12, 15)
                Prince_stats[5] = Prince_stats[5] + recup
                absorbtion_gain_hp.play(3)
                print("vous récupérez", recup, "points de vie !")
                sleep(1.0)
                mob_hp_remaining = Mob_stats[5] - magic_attack
                if Prince_stats[5] > Prince_stats[13]:
                    Prince_stats[5] = Prince_stats[13]
                    return mob_hp_remaining
                else:
                    return mob_hp_remaining
            else:
                Sentence("pas assez de mana")
                mob_hp_remaining = Magic_action(Prince_stats[12])
                return mob_hp_remaining
        elif rep == "3":
            if Prince_stats[10] >= 15:
                absorbtion_soundeffect.play()
                Sentence("Votre corps se recouvre d'une étrange matière, elle est dure comme la pierre.")
                Sentence("Vous êtes plus résistant !")
                sleep(1.0)
                Prince_stats[10] = Prince_stats[10] - 15
                Prince_stats[3] += 5
                mob_hp_remaining = Mob_stats[5]
                return mob_hp_remaining
            else:
                Sentence("pas assez de mana")
                mob_hp_remaining = Magic_action(Prince_stats[12])
                return mob_hp_remaining
        elif rep == "4":
            os.system("cls")
            print(Mob_stats[0], ":", int(Mob_stats[5]), "pv", "                         ", Prince_stats[0], ":", Prince_stats[5], "pv")
            print("                                                                 Mana :", Prince_stats[10])
            mob_hp_remaining = action()
            return mob_hp_remaining
        else:
            print("veuillez entrer un chiffre valide")
            sleep(1.5)
            os.system("cls")
            print(Mob_stats[0], ":", int(Mob_stats[5]), "pv", "                         ", Prince_stats[0], ":", Prince_stats[5], "pv")
            print("                                                                 Mana :", Prince_stats[10])
            mob_hp_remaining = Magic_action(Prince_stats[12])
            return mob_hp_remaining
    elif nivatkmag == 4:
        print("1. Rayon Infernal | coût : 16 mana")
        print("2. Grande moisson | coût : 25 mana")
        print("3. Peau du Seigneur démon | coût : 20 mana")
        print("4. Résurgence Royale | coût : Crâne du roi démon")
        print("5. retour au menu des actions")
        rep = str(input("=> "))
        if rep == "1":
            if Prince_stats[10] >= 16:
                evil_beam_spell.play()
                Prince_stats[10] = Prince_stats[10] - 16
                magic_attack = 25
                print("vous infligez", magic_attack, "dégats magiques !")
                mob_hp_remaining = Mob_stats[5] - magic_attack
                return mob_hp_remaining
            else:
                Sentence("pas assez de mana")
                mob_hp_remaining = Magic_action(Prince_stats[12])
                return mob_hp_remaining
        elif rep == "2":
            if Prince_stats[10] >= 15:
                absorbtion_soundeffect.play()
                Prince_stats[10] = Prince_stats[10] - 15
                magic_attack = randint(15, 20)
                print("vous absorbez", magic_attack, "dégats magiques !")
                sleep(1.0)
                recup = randint(15, 20)
                Prince_stats[5] = Prince_stats[5] + recup
                absorbtion_gain_hp.play(3)
                print("vous récupérez", recup, "points de vie !")
                sleep(1.0)
                mob_hp_remaining = Mob_stats[5] - magic_attack
                if Prince_stats[5] > Prince_stats[13]:
                    Prince_stats[5] = Prince_stats[13]
                    return mob_hp_remaining
                else:
                    return mob_hp_remaining
            else:
                Sentence("pas assez de mana")
                mob_hp_remaining = Magic_action(Prince_stats[12])
                return mob_hp_remaining
        elif rep == "3":
            if Prince_stats[10] >= 20:
                absorbtion_soundeffect.play()
                Sentence("Votre corps se recouvre d'une étrange matière, elle est dure comme de l'acier.")
                Sentence("Vous êtes plus beaucoup résistant !")
                sleep(1.0)
                Prince_stats[10] = Prince_stats[10] - 20
                Prince_stats[3] += 10
                mob_hp_remaining = Mob_stats[5]
                return mob_hp_remaining
            else:
                Sentence("pas assez de mana")
                mob_hp_remaining = Magic_action(Prince_stats[12])
                return mob_hp_remaining
        elif rep == "4":
            print("a compléter")
            mob_hp_remaining = Mob_stats[5]
            return mob_hp_remaining
        elif rep == "5":
            os.system("cls")
            print(Mob_stats[0], ":", int(Mob_stats[5]), "pv", "                         ", Prince_stats[0], ":", Prince_stats[5], "pv")
            print("                                                                 Mana :", Prince_stats[10])
            mob_hp_remaining = action()
            return mob_hp_remaining
        else:
            print("veuillez entrer un chiffre valide")
            sleep(1.5)
            os.system("cls")
            print(Mob_stats[0], ":", int(Mob_stats[5]), "pv", "                         ", Prince_stats[0], ":", Prince_stats[5], "pv")
            print("                                                                 Mana :", Prince_stats[10])
            mob_hp_remaining = Magic_action(Prince_stats[12])
            return mob_hp_remaining


def Fuite():
    #définir la fonction de fuite, mais pour l'instant :
    mob_hp_remaining = Mob_stats[5]
    return mob_hp_remaining


def Low_Blow(x):
    # x représente le niveau de coups bas, le niveau va déterminer le menu de coups bas et la pussance des capacités
    # il manque le coup bas du grand Sagzinoth
    if x == 1:
        print("1. Sable dans les yeux | 1 sur 2")
        print("2. Retour au menu des actions")
        rep = str(input("=> "))
        if rep == "1":
            rate = randint(1, 10)
            if rate > 5:
                print("Vous vous placez efficacement devant " + Mob_stats[0] + " et vous jetez une poignée de sable dans les yeux !")
                sand_low_blow.play()
                print("Cela l'aveugle partiellement. " + Mob_stats[0] + " est moins précis !")
                sleep(1.0)
                Mob_stats[6] = Mob_stats[6] - 10
                mob_hp_remaining = Mob_stats[5]
                return mob_hp_remaining
            else:
                Sentence("Raté")
                mob_hp_remaining = Mob_stats[5]
                return mob_hp_remaining
        elif rep == "2":
            os.system("cls")
            print(Mob_stats[0], ":", int(Mob_stats[5]), "pv", "                         ", Prince_stats[0], ":", Prince_stats[5], "pv")
            print("                                                                 Mana :", Prince_stats[10])
            mob_hp_remaining = action()
            return mob_hp_remaining
        else:
            print("veuillez entrer un chiffre valide")
            sleep(1.5)
            os.system("cls")
            print(Mob_stats[0], ":", int(Mob_stats[5]), "pv", "                         ", Prince_stats[0], ":", Prince_stats[5], "pv")
            print("                                                                 Mana :", Prince_stats[10])
            mob_hp_remaining = Low_Blow(Prince_stats[8])
        return mob_hp_remaining
    elif x == 2:
        print("1. Sable dans les yeux | 6 sur 10")
        print("2. Coup dans le genou | 1 sur 2")
        print("3. Retour au menu des actions")
        rep = str(input("=> "))
        if rep == "1":
            rate = randint(1, 10)
            if rate > 4:
                print("Vous vous placez efficacement devant " + Mob_stats[0] + " et vous jetez une poignée de sable dans les yeux !")
                sand_low_blow.play()
                print("Cela l'aveugle partiellement. " + Mob_stats[0] + " est moins précis !")
                sleep(1.0)
                Mob_stats[6] = Mob_stats[6] - 10
                mob_hp_remaining = Mob_stats[5]
                return mob_hp_remaining
            else:
                print("Raté")
                mob_hp_remaining = Mob_stats[5]
                return mob_hp_remaining
        elif rep == "2":
            rate = randint(1,10)
            if rate > 5:
                print("Vous visez le genou de votre adversaire et mettez un puissant coup de pied dedans !")
                crack.play()
                print(Mob_stats[0], "boite, son esquive diminue !")
                sleep(1.0)
                Mob_stats[7] = Mob_stats[7] - 5
                if Mob_stats[7] < 0:
                    print(Mob_stats[0], "ne peut plus esquiver !")
                    mob_hp_remaining = Mob_stats[5]
                    return mob_hp_remaining
                else:
                    mob_hp_remaining = Mob_stats[5]
                    return mob_hp_remaining
            else:
                print("Raté")
                mob_hp_remaining = Mob_stats[5]
                return mob_hp_remaining
        elif rep == "3":
            os.system("cls")
            print(Mob_stats[0], ":", int(Mob_stats[5]), "pv", "                         ", Prince_stats[0], ":", Prince_stats[5], "pv")
            print("                                                                 Mana :", Prince_stats[10])
            mob_hp_remaining = action()
            return mob_hp_remaining
        else:
            print("veuillez entrer un chiffre valide")
            sleep(1.5)
            os.system("cls")
            print(Mob_stats[0], ":", int(Mob_stats[5]), "pv", "                         ", Prince_stats[0], ":", Prince_stats[5], "pv")
            print("                                                                 Mana :", Prince_stats[10])
            mob_hp_remaining = Low_Blow(Prince_stats[8])
        return mob_hp_remaining
    elif x == 3:
        print("1. Sable dans les yeux | 7 sur 10")
        print("2. Coup dans le genou | 6 sur 10")
        print("3. Brise armure | 4 sur 10")
        print("4. Retour au menu des actions")
        rep = str(input("=> "))
        if rep == "1":
            rate = randint(1, 10)
            if rate > 3:
                print("Vous vous placez efficacement devant " + Mob_stats[0] + " et vous jetez une poignée de sable dans les yeux !")
                sand_low_blow.play()
                print("Cela l'aveugle partiellement. " + Mob_stats[0] + " est moins précis !")
                sleep(1.0)
                Mob_stats[6] = Mob_stats[6] - 10
                mob_hp_remaining = Mob_stats[5]
                return mob_hp_remaining
            else:
                print("Raté")
                mob_hp_remaining = Mob_stats[5]
                return mob_hp_remaining
        elif rep == "2":
            rate = randint(1, 10)
            if rate > 4:
                print("Vous visez le genou de votre adversaire et mettez un puissant coup de pied dedans !")
                crack.play()
                print(Mob_stats[0], "boite, son esquive diminue !")
                sleep(1.0)
                Mob_stats[7] = Mob_stats[7] - 5
                if Mob_stats[7] <= 0:
                    Mob_stats[7] = 0
                    print(Mob_stats[0], "ne peut plus esquiver !")
                    mob_hp_remaining = Mob_stats[5]
                    return mob_hp_remaining
                else:
                    mob_hp_remaining = Mob_stats[5]
                    return mob_hp_remaining
            else:
                print("Raté")
                mob_hp_remaining = Mob_stats[5]
                return mob_hp_remaining
        elif rep == "3":
            rate = randint(1,10)
            if rate > 6:
                print("Vous trouvez une faille dans la défense de votre adversaire !")
                broken_armor.play()
                print("La protection de votre adversaire se fragilise !")
                sleep(1.0)
                Mob_stats[3] = Mob_stats[3] - 2
                if Mob_stats[3] <= 0:
                    Mob_stats[3] = 0
                    print(Mob_stats[0], "voit sa seule protection partir en morceaux !")
                    sleep(1.0)
                    mob_hp_remaining = Mob_stats[5]
                    return mob_hp_remaining
                else:
                    mob_hp_remaining = Mob_stats[5]
                    return mob_hp_remaining
            else:
                print("Raté")
                mob_hp_remaining = Mob_stats[5]
                return mob_hp_remaining
        elif rep == "4":
            os.system("cls")
            print(Mob_stats[0], ":", int(Mob_stats[5]), "pv", "                         ", Prince_stats[0], ":", Prince_stats[5], "pv")
            print("                                                                 Mana :", Prince_stats[10])
            mob_hp_remaining = action()
            return mob_hp_remaining
        else:
            print("veuillez entrer un chiffre valide")
            sleep(1.5)
            os.system("cls")
            print(Mob_stats[0], ":", int(Mob_stats[5]), "pv", "                         ", Prince_stats[0], ":", Prince_stats[5], "pv")
            print("                                                                 Mana :", Prince_stats[10])
            mob_hp_remaining = Low_Blow(Prince_stats[8])
        return mob_hp_remaining
    elif x == 4:
        print("1. Sable dans les yeux | 7 sur 10")
        print("2. Coup dans le genou | 7 sur 10")
        print("3. Brise armure | 1 sur 2")
        print("4. Liquide corrosif | 1 sur 2")
        print("5. retour au menu des actions")
        rep = str(input("=> "))
        if rep == "1":
            rate = randint(1, 10)
            if rate > 3:
                print("Vous vous placez efficacement devant " + Mob_stats[0] + " et vous jetez une poignée de sable dans les yeux !")
                sand_low_blow.play()
                print("Cela l'aveugle partiellement. " + Mob_stats[0] + " est moins précis !")
                sleep(1.0)
                Mob_stats[6] = Mob_stats[6] - 15
                mob_hp_remaining = Mob_stats[5]
                return mob_hp_remaining
            else:
                print("Raté")
                mob_hp_remaining = Mob_stats[5]
                return mob_hp_remaining
        elif rep == "2":
            rate = randint(1, 10)
            if rate > 3:
                print("Vous visez le genou de votre adversaire et mettez un puissant coup de pied dedans !")
                crack.play()
                print(Mob_stats[0], "boite, son esquive diminue !")
                sleep(1.0)
                Mob_stats[7] = Mob_stats[7] - 7
                if Mob_stats[7] <= 0:
                    Mob_stats[7] = 0
                    print(Mob_stats[0], "ne peut plus esquiver !")
                    mob_hp_remaining = Mob_stats[5]
                    return mob_hp_remaining
                else:
                    mob_hp_remaining = Mob_stats[5]
                    return mob_hp_remaining
            else:
                print("Raté")
                mob_hp_remaining = Mob_stats[5]
                return mob_hp_remaining
        elif rep == "3":
            rate = randint(1, 10)
            if rate > 5:
                print("Vous trouvez une faille dans la défense de votre adversaire !")
                broken_armor.play()
                print("La protection de votre adversaire se fragilise !")
                sleep(1.0)
                Mob_stats[3] = Mob_stats[3] - 4
                if Mob_stats[3] <= 0:
                    Mob_stats[3] = 0
                    print(Mob_stats[0], "voit sa seule protection partir en morceaux !")
                    sleep(1.0)
                    mob_hp_remaining = Mob_stats[5]
                    return mob_hp_remaining
                else:
                    mob_hp_remaining = Mob_stats[5]
                    return mob_hp_remaining
            else:
                print("Raté")
                mob_hp_remaining = Mob_stats[5]
                return mob_hp_remaining
        elif rep == "4":
            rate = randint(1,10)
            if rate > 5:
                print("vous profitez du moment parfait pour verser un liquide corrosif sur l'arme de l'adversaire !")
                sleep(1.0)
                acid_sound.play()
                print("les dégats de l'adversaire sont réduits !")
                Mob_stats[2] = Mob_stats[2] - 2
                if Mob_stats[2] <= 0:
                    Mob_stats[2] = 0
                    print(Mob_stats[0], "voit son arme fondre devant ses yeux !")
                    mob_hp_remaining = Mob_stats[5]
                    return mob_hp_remaining
                else:
                    mob_hp_remaining = Mob_stats[5]
                    return mob_hp_remaining
            else:
                print("Raté")
                mob_hp_remaining = Mob_stats[5]
                return mob_hp_remaining
        elif rep == "5":
            os.system("cls")
            print(Mob_stats[0], ":", int(Mob_stats[5]), "pv", "                         ", Prince_stats[0], ":", Prince_stats[5], "pv")
            print("                                                                 Mana :", Prince_stats[10])
            mob_hp_remaining = action()
            return mob_hp_remaining
        else:
            print("veuillez entrer un chiffre valide")
            sleep(1.5)
            os.system("cls")
            print(Mob_stats[0], ":", int(Mob_stats[5]), "pv", "                         ", Prince_stats[0], ":", Prince_stats[5], "pv")
            print("                                                                 Mana :", Prince_stats[10])
            mob_hp_remaining = Low_Blow(Prince_stats[8])
        return mob_hp_remaining


def mob_action():
    print(Mob_stats[0], "attaque !")
    sleep(1.0)
    rateaccuracy = randint(1, 100)
    if rateaccuracy < Mob_stats[6]:
        rateesq = randint(1, 100)
        if rateesq <= Prince_stats[11]:
            print("Vous esquivez l'attaque !")
            degats = Prince_stats[5]
            return degats
        else:
            degats = attaque_mob(Mob_stats[0], Mob_stats[1], Mob_stats[2], Prince_stats[3], Mob_stats[4], Prince_stats[5])
            sword_sound.play()
            fork_sound.play()
            return degats
    else:
        print(Mob_stats[0], "rate son attaque !")
        degats = Prince_stats[5]
        return degats


def action():
    Sentence("A votre tour :")
    print("1. Attaquer")
    print("2. Magie")
    print("3. Coup bas")
    print("4. Fuite")
    rep = str(input("=> "))
    if rep == "1":
        Sentence("Vous attaquez !")
        rateaccuracy = randint(1,100)
        if rateaccuracy < Prince_stats[6]:
            rateesq = randint(1,100)
            if rateesq <= Mob_stats[7]:
                print(Mob_stats[0], "esquive votre attaque !")
                degats = Mob_stats[5]
                return degats
            else:
                degats = attaque(Mob_stats[0], Prince_stats[1], Prince_stats[2], Mob_stats[3], Prince_stats[4], Mob_stats[5])
                sword_sound.play()
                return degats
        else:
            print("vous ratez votre attaque !")
            degats = Mob_stats[5]
            return degats

    elif rep == "2":
        Sentence("Vous concentrez votre mana")
        degats = Magic_action(Prince_stats[12])
        return degats
    elif rep == "3":
        Sentence("Vous prenez un air sournois...")
        degats = Low_Blow(Prince_stats[8])
        return degats
    elif rep == "4":
        Sentence("Vous tentez de fuir")
        #fly_chance = randint(1, 10)
        #if fly_chance > 5:
        degats = Fuite()
        return degats
        #else:
            #Sentence("Votre fuite échoue")
            #degats = Mob_stats[5]
            #return degats
    else:
        while rep != "1" or rep != "2" or rep != "3" or rep != "4":
            Sentence("veuillez entrer un chiffre valide")
            sleep(1.5)
            os.system("cls")
            print(Mob_stats[0], ":", int(Mob_stats[5]), "pv", "                         ", Prince_stats[0], ":", Prince_stats[5], "pv")
            print("                                                                 Mana :", Prince_stats[10])
            degats = action()
            return degats


def combat(princes_stats, MobStats, music):
    music
    print(princes_stats)
    print(MobStats)
    first = randint(1, 10)
    prince_life = Prince_stats[5]
    mob_life = Mob_stats[5]
    mp = Prince_stats[10]
    hp = Prince_stats[5]
    os.system("cls")
    if first < 5:
        Sentence("Vous frappez en premier !")
        print(Mob_stats[0], ":", int(Mob_stats[5]), "pv", "                         ", Prince_stats[0], ":", Prince_stats[5], "pv")
        print("                                                                 Mana :", Prince_stats[10])
        mob_life = action()
        sleep(1.5)
        Mob_stats[5] = mob_life
        os.system("cls")
        while prince_life > 0 or mob_life > 0:
            print(Mob_stats[0], ":", int(Mob_stats[5]), "pv", "                         ", Prince_stats[0], ":", Prince_stats[5], "pv")
            print("                                                                 Mana :", Prince_stats[10])
            prince_life = mob_action()
            Prince_stats[5] = prince_life
            sleep(1.5)
            os.system("cls")
            if prince_life < 0:
                print("Défaite")
                Prince_stats[5] = hp
                Prince_stats[10] = mp
                #la musique s'arrête
                #fonction défaite avec tp au sancturaire des démons
                victoire = False,
                return victoire

            print(Mob_stats[0], ":", int(Mob_stats[5]), "pv", "                         ", Prince_stats[0], ":", Prince_stats[5], "pv")
            print("                                                                 Mana :", Prince_stats[10])
            mob_life = action()
            Mob_stats[5] = mob_life
            sleep(1.5)
            os.system("cls")
            if mob_life < 0:
                print(Mob_stats[0], "est vaincu")
                Prince_stats[10] = mp
                enemy_death.play()
                sleep(4.0)
                # la musique s'arrête
                # fonction victoire avec musique de victoire + affichage du loot + xp
                # faire en sorte de return la vie restante et de la réattribuer à la liste Prince_Stats
                victoire = True
                return victoire
    else:
        Sentence(str(Mob_stats[0]) + " frappe en premier !")
        print(Mob_stats[0], ":", int(Mob_stats[5]), "pv", "                         ", Prince_stats[0], ":", Prince_stats[5], "pv")
        print("                                                                 Mana :", Prince_stats[10])
        prince_life = mob_action()
        Prince_stats[5] = prince_life
        sleep(1.5)
        os.system("cls")
        while prince_life > 0 or mob_life > 0:
            print(Mob_stats[0], ":", int(Mob_stats[5]), "pv", "                         ", Prince_stats[0], ":", Prince_stats[5], "pv")
            print("                                                                 Mana :", Prince_stats[10])
            mob_life = action()
            Mob_stats[5] = mob_life
            sleep(1.5)
            os.system("cls")
            if mob_life < 0:
                print(Mob_stats[0], "est vaincu")
                Prince_stats[10] = mp
                enemy_death.play()
                sleep(4.0)
                #la musique s'arrête
                #fonction victoire avec musique de victoire + affichage du loot + xp
                # faire en sorte de return la vie restante et de la réattribuer à la liste Prince_Stats
                victoire = True
                return victoire

            print(Mob_stats[0], ":", int(Mob_stats[5]), "pv", "                         ", Prince_stats[0], ":", Prince_stats[5], "pv")
            print("                                                                 Mana :", Prince_stats[10])
            prince_life = mob_action()
            Prince_stats[5] = prince_life
            sleep(1.5)
            os.system("cls")
            if prince_life < 0:
                print("Défaite")
                Prince_stats[10] = mp
                Prince_stats[5] = hp
                # la musique s'arrête
                # fonction défaite avec tp au sancturaire des démons
                victoire = False
                return victoire
