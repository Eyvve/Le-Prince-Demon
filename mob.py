from random import *
import combat
from index import *

###"""Inventaire du Hero ne pas toucher
char = {
    'xp' : {
        "lvl": 1,
        "xp" : 0,
        "lvlnext": 25,
    },
    'hands' :{
        'hand1' : 'épée rouillé',
        'head' : None,
        'torso' : None,
        'leg' : None,
        'foot' : None,
    },
    'gold' : {
        'Argent' : 10,
    },
    'inv' : {
        'Potion de soin n1' : 2,
        'Potion de mana n1' : 1,
        },
    'equipement' : {
        'épée rouillé' : 0,
    },
    'armor' :{
        'cape noir' : 0,
    }
}
###"""Inventaire du Hero ne pas toucher"""




#mobs
fermier = {
    'nom' : "Fermier",
    'xp' : {
        "xp" : randint(10, 12),
    },
    'gold' : {
        'Argent' : randint(5, 7),
    },
    'inv': {
        "Oeil humain": randint(1,2),
        "Bouse de vache" : randint(2,4)
    }
}

chevalier = {
    'nom' : "Chevalier",
    'xp' : {
        "xp" : randint(25, 30),
    },
    'gold' : {
        'Argent' : randint(10, 13),
    },
    'inv': {
        "Armoirie de chevalier": randint(0,1)
    }
}

vendeur = {
    'nom' : "Vendeur",
    'xp' : {
        "xp" : randint(15, 20),
    },
    'gold' : {
        'Argent' : randint(50, 55),
    },
    'inv': {
        'Potion de soin n1': 1
    }
}


gobelin = {
    'nom' : "Gobelin",
    'xp' : {
        "xp" : randint(20, 25),
    },
    'gold' : {
        'Argent' : randint(5, 7),
    },
    'inv': {
        'slipe de gobelin': randint(1,2)
    }
}
