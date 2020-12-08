from random import *
# from time import sleep
# from testintro import Sentence
# import pygame
# import os
#
# pygame.init()
# combat_music = pygame.mixer.Sound("field_fight.ogg")
# sword_sound = pygame.mixer.Sound("coup.wav")
# fork_sound = pygame.mixer.Sound("coup_fourche.wav")
# enemy_death = pygame.mixer.Sound("ennemi_mort.wav")
# evil_beam_spell = pygame.mixer.Sound("evil_beam.wav")
# absorbtion_soundeffect = pygame.mixer.Sound("absorbtion_sound.wav")
# absorbtion_gain_hp = pygame.mixer.Sound("heal_spell.wav")
#
# # statistiques du mob seront intégrées à chaque évènement donc dépendra de la map et de l'ennemi
# Mob_stats = ["fermier", 6, 9, 2, 1.0, 40, 70]
# # significations : nom, attaque mini, attaque max, défense, multiplicateur de dégat (arme), vie,pvmax, précision
Prince_stats = ["Prince", 8, 12, 3, 1.3, 60, 90, 5, 1, 0, 15, 0, 1, 60, 15, 2]
# significations : (0)nom, (1)attaque mini, (2)attaque max, (3)défense, (4)multiplicateur de dégat (arme), (5)vie, (6)précision, (7)chance de coup bas, (8)niveau de coup bas, (9)xp coup bas, (10)mana, (11)puissance magique, (12)attques magiques, (13) PV max, (14) MP max, (15) def mini
#
#
# def attaque_mob(name, atkmini, atkmax, df, mult, hp):
#     total_atk = randint(atkmini, atkmax) * mult
#     final_atk = total_atk - df
#     Prince_hp_remaining = hp - final_atk
#     round(Prince_hp_remaining, 0)
#     print(name, "vous inflige", int(final_atk), "dégats.")
#     return Prince_hp_remaining
#
#
# def attaque(name, atkmini, atkmax, df, mult, hp):
#     total_atk = randint(atkmini, atkmax) * mult
#     final_atk = total_atk - df
#     mob_hp_remaining = hp - final_atk
#     round(mob_hp_remaining, 0)
#     print("vous infligez", int(final_atk), "dégats", "à", name)
#     return mob_hp_remaining
#
#
# def Magic_action(nivatkmag):
#     prince_life = Prince_stats[5]
#     if nivatkmag == 1:
#         print("1. Rayon démoniaque mineur | coût : 7 mana")
#         print("2. retour au menu des actions")
#         rep = str(input())
#         if rep == "1":
#             if Prince_stats[10] >= 7:
#                 evil_beam_spell.play()
#                 Prince_stats[10] = Prince_stats[10] - 7
#                 magic_attack = 12 + Prince_stats[11]
#                 print("vous infligez", magic_attack, "dégats magiques !")
#                 mob_hp_remaining = Mob_stats[5] - magic_attack
#                 return mob_hp_remaining
#             else:
#                 Sentence("pas assez de mana")
#                 mob_hp_remaining = Magic_action(Prince_stats[12])
#                 return mob_hp_remaining
#         elif rep == "2":
#             os.system("cls")
#             print(Mob_stats[0], ":", int(Mob_stats[5]), "pv", "                         ", Prince_stats[0], ":", int(prince_life), "pv")
#             print("                                                                 Mana :", Prince_stats[10])
#             mob_hp_remaining = action()
#             return mob_hp_remaining
#         else:
#             print("veuillez entrer un chiffre valide")
#             mob_hp_remaining = Magic_action(Prince_stats[12])
#             return mob_hp_remaining
#     elif nivatkmag == 2:
#         print("1. Rayon démoniaque mineur | coût : 7 mana")
#         print("2. Soif d'âme | coût : 15 mana")
#         print("3. retour au menu des actions")
#         rep = str(input())
#         if rep == "1":
#             if Prince_stats[10] >= 7:
#                 evil_beam_spell.play()
#                 Prince_stats[10] = Prince_stats[10] - 7
#                 magic_attack = 12 + Prince_stats[11]
#                 print("vous infligez", magic_attack, "dégats magiques !")
#                 mob_hp_remaining = Mob_stats[5] - magic_attack
#                 return mob_hp_remaining
#             else:
#                 Sentence("pas assez de mana")
#                 mob_hp_remaining = Magic_action(Prince_stats[12])
#                 return mob_hp_remaining
#         elif rep == "2":
#             if Prince_stats[10] >= 15:
#                 absorbtion_soundeffect.play()
#                 Prince_stats[10] = Prince_stats[10] - 15
#                 magic_attack = randint(8,10) + Prince_stats[11]
#                 print("vous absorbez", magic_attack, "dégats magiques !")
#                 sleep(1.0)
#                 recup = randint(9,11)
#                 Prince_stats[5] = Prince_stats[5] + recup
#                 absorbtion_gain_hp.play(3)
#                 print("vous récupérez" , recup , "points de vie !")
#                 sleep(1.0)
#                 mob_hp_remaining = Mob_stats[5] - magic_attack
#                 return mob_hp_remaining
#             else:
#                 Sentence("pas assez de mana")
#                 mob_hp_remaining = Magic_action(Prince_stats[12])
#                 return mob_hp_remaining
#         elif rep == "3":
#             os.system("cls")
#             print(Mob_stats[0], ":", int(Mob_stats[5]), "pv", "                         ", Prince_stats[0], ":", int(prince_life), "pv")
#             print("                                                                 Mana :", Prince_stats[10])
#             action()
#         else:
#             print("veuillez entrer un chiffre valide")
#             mob_hp_remaining = Magic_action(Prince_stats[12])
#             return mob_hp_remaining
#     elif nivatkmag == 3:
#         print("1. Rayon démoniaque mineur | coût : 7 mana")
#         print("2. Soif d'âme | coût : 15 mana")
#         print("3. ")
#         print("4. retour au menu des actions")
#         rep = str(input())
#         if rep == "1":
#             if Prince_stats[10] >= 7:
#                 evil_beam_spell.play()
#                 Prince_stats[10] = Prince_stats[10] - 7
#                 magic_attack = 12 + Prince_stats[11]
#                 print("vous infligez" , magic_attack , "dégats magiques !")
#                 mob_hp_remaining = Mob_stats[5] - magic_attack
#                 return mob_hp_remaining
#             else:
#                 Sentence("pas assez de mana")
#                 mob_hp_remaining = Magic_action(Prince_stats[12])
#                 return mob_hp_remaining
#         elif rep == "2":
#             if Prince_stats[10] >= 15:
#                 absorbtion_soundeffect.play()
#                 Prince_stats[10] = Prince_stats[10] - 15
#                 magic_attack = randint(8, 10) + Prince_stats[11]
#                 print("vous absorbez", magic_attack, "dégats magiques !")
#                 sleep(1.0)
#                 recup = randint(9, 11)
#                 Prince_stats[5] = Prince_stats[5] + recup
#                 absorbtion_gain_hp.play(3)
#                 print("vous récupérez", recup, "points de vie !")
#                 sleep(1.0)
#                 mob_hp_remaining = Mob_stats[5] - magic_attack
#                 return mob_hp_remaining
#             else:
#                 Sentence("pas assez de mana")
#                 mob_hp_remaining = Magic_action(Prince_stats[12])
#                 return mob_hp_remaining
#         elif rep == "3":
#             print("a compléter")
#         elif rep == "4":
#             os.system("cls")
#             print(Mob_stats[0], ":", int(Mob_stats[5]), "pv", "                         ", Prince_stats[0], ":", int(prince_life), "pv")
#             print("                                                                 Mana :", Prince_stats[10])
#             action()
#         else:
#             print("veuillez entrer un chiffre valide")
#             mob_hp_remaining = Magic_action(Prince_stats[12])
#             return mob_hp_remaining
#     elif nivatkmag == 4:
#         print("1. Rayon démoniaque mineur | coût : 7 mana")
#         print("2. Soif d'âme | coût : 15 mana")
#         print("3. ")
#         print("4. ")
#         print("5. retour au menu des actions")
#         rep = str(input())
#         if rep == "1":
#             if Prince_stats[10] >= 7:
#                 evil_beam_spell.play()
#                 Prince_stats[10] = Prince_stats[10] - 7
#                 magic_attack = 12 + Prince_stats[11]
#                 print("vous infligez", magic_attack, "dégats magiques !")
#                 mob_hp_remaining = Mob_stats[5] - magic_attack
#                 return mob_hp_remaining
#             else:
#                 Sentence("pas assez de mana")
#                 mob_hp_remaining = Magic_action(Prince_stats[12])
#                 return mob_hp_remaining
#         elif rep == "2":
#             if Prince_stats[10] >= 15:
#                 absorbtion_soundeffect.play()
#                 Prince_stats[10] = Prince_stats[10] - 15
#                 magic_attack = randint(8, 10) + Prince_stats[11]
#                 print("vous absorbez", magic_attack, "dégats magiques !")
#                 sleep(1.0)
#                 recup = randint(9, 11)
#                 Prince_stats[5] = Prince_stats[5] + recup
#                 absorbtion_gain_hp.play(3)
#                 print("vous récupérez", recup, "points de vie !")
#                 sleep(1.0)
#                 mob_hp_remaining = Mob_stats[5] - magic_attack
#                 return mob_hp_remaining
#             else:
#                 Sentence("pas assez de mana")
#                 mob_hp_remaining = Magic_action(Prince_stats[12])
#                 return mob_hp_remaining
#         elif rep == "3":
#             print("a compléter")
#         elif rep == "4":
#             print("a compléter")
#         elif rep == "5":
#             os.system("cls")
#             print(Mob_stats[0], ":", int(Mob_stats[5]), "pv", "                         ", Prince_stats[0], ":", int(prince_life), "pv")
#             print("                                                                 Mana :", Prince_stats[10])
#             action()
#         else:
#             print("veuillez entrer un chiffre valide")
#             mob_hp_remaining = Magic_action(Prince_stats[12])
#             return mob_hp_remaining
#
#
# def Fuite():
#     #définir la fonction de fuite, mais pour l'instant :
#     mob_hp_remaining = Mob_stats[5]
#     return mob_hp_remaining
#
#
# def low_blow(x):
#     if x == 1:
#         print("1. Coup derrière le genou")
#         rep = str(input())
#         if rep == "1":
#             rate = randint(1,10)
#             if rate < Prince_stats[6]:
#                 print("Vous vous placez derrière " + Mob_stats[0] + " et vous mettez un coup de pied derrière son genou !")
#                 print("Cela lui a fait perdre l'équilibre. " + Mob_stats[0] + " est moins précis !")
#                 Mob_stats[6] = Mob_stats[6] - 10
#                 finished = Mob_stats[5]
#                 return finished
#             else:
#                 print("raté")
#                 finished = Mob_stats[5]
#                 return finished
#         else:
#             while rep != "1":
#                 print("veuillez entrer un chiffre valide")
#                 rep = str(input())
#         finished = Mob_stats[5]
#         return finished
#     elif x == 2:
#         print("1. Coup derrière le genou")
#         print("2. Exploitation de faille")
#         rep = str(input())
#         if rep == "1":
#             print("action")
#             # action Coup derrière le genou
#         elif rep == "2":
#             print("action")
#            #  action Exploitation de faille
#         else:
#             while rep != "1" or rep != "2":
#                 print("veuillez entrer un chiffre valide")
#                 rep = str(input())
#     elif x == 3:
#         print("1. Coup derrière le genou")
#         print("2. Exploitation de faille")
#         print("3. Sable dans les yeux")
#         rep = str(input())
#         if rep == "1":
#             print("action")
#             # action Coup derrière le genou
#         elif rep == "2":
#             print("action")
#             # action Exploitation de faille
#         elif rep == "3":
#             print("action")
#             # action Sable dans les yeux
#         else:
#             while rep != "1" or rep != "2" or rep != "3":
#                 print("veuillez entrer un chiffre valide")
#                 rep = str(input())
#     elif x == 4:
#         print("1. Coup derrière le genou")
#         print("2. Exploitation de faille")
#         print("3. Sable dans les yeux")
#         print("4. Provocation")
#         rep = str(input())
#         if rep == "1":
#             print("action")
#             # action Coup derrière le genou
#         elif rep == "2":
#             print("action")
#             # action Exploitation de faille
#         elif rep == "3":
#             print("action")
#             # action Sable dans les yeux
#         elif rep == "4":
#             print("action")
#             # action Provocation
#         else:
#             while rep != "1" or rep != "2" or rep != "3" or rep != "4":
#                 print("veuillez entrer un chiffre valide")
#                 rep = str(input())
#
#
# def mob_action():
#     print(Mob_stats[0] , "attaque !")
#     sleep(1.0)
#     degats = attaque_mob(Mob_stats[0], Mob_stats[1], Mob_stats[2], Prince_stats[3], Mob_stats[4], Prince_stats[5])
#     fork_sound.play()
#     return degats
#
#
# def action():
#     Sentence("A votre tour :")
#     print("1. Attaquer")
#     print("2. Magie")
#     print("3. Coup bas")
#     print("4. Fuite")
#     rep = str(input())
#     if rep == "1":
#         Sentence("Vous attaquez !")
#         degats = attaque(Mob_stats[0], Prince_stats[1], Prince_stats[2], Mob_stats[3], Prince_stats[4], Mob_stats[5])
#         sword_sound.play()
#         return degats
#     elif rep == "2":
#         Sentence("Vous concentrez votre mana")
#         degats = Magic_action(Prince_stats[12])
#         return degats
#     elif rep == "3":
#         Sentence("Vous prenez un air sournois...")
#         degats = low_blow(Prince_stats[8])
#         return degats
#     elif rep == "4":
#         Sentence("Vous tentez de fuir")
#         #fly_chance = randint(1, 10)
#         #if fly_chance > 5:
#         degats = Fuite()
#         return degats
#         #else:
#             #Sentence("Votre fuite échoue")
#             #degats = Mob_stats[5]
#             #return degats
#     else:
#         while rep != "1" or rep != "2" or rep != "3" or rep != "4":
#             Sentence("veuillez entrer un chiffre valide")
#             sleep(1.5)
#             os.system("cls")
#             action()
#
#
# def combat(princes_stats, MobStats):
#     combat_music.play(-1)
#     print(princes_stats)
#     print(MobStats)
#     first = randint(1, 10)
#     prince_life = Prince_stats[5]
#     mob_life = Mob_stats[5]
#     os.system("cls")
#     if first < 5:
#         Sentence("Vous frappez en premier !")
#         print(Mob_stats[0], ":", int(Mob_stats[5]), "pv", "                         ", Prince_stats[0], ":", int(prince_life), "pv")
#         print("                                                                 Mana :" , Prince_stats[10])
#         mob_life = action()
#         sleep(1.5)
#         Mob_stats[5] = mob_life
#         os.system("cls")
#         while prince_life > 0 or mob_life > 0:
#             print(Mob_stats[0], ":", int(Mob_stats[5]), "pv", "                         ", Prince_stats[0], ":", int(prince_life), "pv")
#             print("                                                                 Mana :", Prince_stats[10])
#             prince_life = mob_action()
#             Prince_stats[5] = prince_life
#             sleep(1.5)
#             os.system("cls")
#             if prince_life < 0:
#                 print("Défaite")
#                 #la musique s'arrête
#                 #fonction défaite avec tp au sancturaire des démons
#                 victoire = False,
#                 return victoire
#
#             print(Mob_stats[0], ":", int(Mob_stats[5]), "pv", "                         ", Prince_stats[0], ":", int(prince_life), "pv")
#             print("                                                                 Mana :", Prince_stats[10])
#             mob_life = action()
#             Mob_stats[5] = mob_life
#             sleep(1.5)
#             os.system("cls")
#             if mob_life < 0:
#                 print(Mob_stats[0] , "est vaincu")
#                 enemy_death.play()
#                 sleep(4.0)
#                 # la musique s'arrête
#                 # fonction victoire avec musique de victoire + affichage du loot + xp
#                 # faire en sorte de return la vie restante et de la réattribuer à la liste Prince_Stats
#                 victoire = True
#                 return victoire
#     else:
#         Sentence(str(Mob_stats[0]) + " frappe en premier !")
#         print(Mob_stats[0], ":", int(Mob_stats[5]), "pv", "                         ", Prince_stats[0], ":", int(prince_life), "pv")
#         print("                                                                 Mana :", Prince_stats[10])
#         prince_life = mob_action()
#         Prince_stats[5] = prince_life
#         sleep(1.5)
#         os.system("cls")
#         while prince_life > 0 or mob_life > 0:
#             print(Mob_stats[0], ":", int(Mob_stats[5]), "pv", "                         ", Prince_stats[0], ":", int(prince_life), "pv")
#             print("                                                                 Mana :", Prince_stats[10])
#             mob_life = action()
#             Mob_stats[5] = mob_life
#             sleep(1.5)
#             os.system("cls")
#             if mob_life < 0:
#                 print(Mob_stats[0] , "est vaincu")
#                 enemy_death.play()
#                 sleep(4.0)
#                 #la musique s'arrête
#                 #fonction victoire avec musique de victoire + affichage du loot + xp
#                 # faire en sorte de return la vie restante et de la réattribuer à la liste Prince_Stats
#                 victoire = True
#                 return victoire
#
#             print(Mob_stats[0], ":", int(Mob_stats[5]), "pv", "                         ", Prince_stats[0], ":", int(prince_life), "pv")
#             print("                                                                 Mana :", Prince_stats[10])
#             prince_life = mob_action()
#             Prince_stats[5] = prince_life
#             sleep(1.5)
#             os.system("cls")
#             if prince_life < 0:
#                 print("Défaite")
#                 # la musique s'arrête
#                 # fonction défaite avec tp au sancturaire des démons
#                 victoire = False
#                 return victoire
#
#
#
# combat(Prince_stats, Mob_stats)