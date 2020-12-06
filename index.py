from random import *
from mob import *


index_wapone = {
    'épée rouillé' : [1.2],#multiplicateur d'atk
    "épée en fer" : [1.4],
    "rapière" : [1.8],
    "épéee obscur" : [2]
}
index_armor = {
    #'armure'  :  [multiplicateur de def, emplacement] 1 = head / 2 = torso / 3 = leg / 4 = foot
    #cape de départ
    'cape noir' : [1.2, 2],
    #armure cuir
    'casque en cuir' : [1.2, 1],
    'plastron en cuir' : [1.4, 2],
    'jambière en cuir' : [1.4, 3],
    'botte en cuir' : [1.2, 4],
}

index_objet = {
    #'nom de l'objet'   : [Prix, effet donné]
    #objet de soin
    #Potion
    'Potion de soin n1' : [50, 18,1],#[Prix, PV,gagne des pv]
    'Potion de soin n2' : [150, 50,1],
    'Potion de soin n3' : [300, 90,1],
    'Potion de mana n1' : [150, 10,2],#[Prix, PM,gagne des pm]
    'Potion de mana n2' : [300, 25,2],
    'Potion de mana n3' : [600, 50,2],
    #Herbe
    'Herbe des âmes' : [20, 10,1],
    'Herbe de luimière' : [5, -18,1],
    #objet a vendre
    "Armoirie de chevalier": [43],#[Prix]
    "Bouse de vache": [2],
    "Brochure en papier": [10],
    "Morceau de minerai" : [24],
    "Oeil humain" : [3],
    "Pot de terre" : [6],
    'Slip de Gobelin': [5],

}


defeated =  {
    'gold' : {
        'Argent' : randint(10, 15),
    }}

chest1 = {
'gold' : {
        'Argent' : 30,
    },
    "inv": {
        "épée_en_fer" : 1}
}
chest2 = {
    "inv": {
        "Argent": -10}
}

