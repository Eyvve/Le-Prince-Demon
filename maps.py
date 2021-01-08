from intro import *
from combat import *
from about import *
from Music_sounds import *
from Statistics_Mobs import *
#from data import *

def skip_touch():
    while True:
        print("")
        print("Appuiez sur entrée pour passer.")
        skip = str(input())
        if skip == "":
            os.system("cls")
            break

def beginning():
    from intro import Sentence
    from combat import Prince_stats
    from combat import combat
    Prince_stats[0] = str(input("Quel est votre nom : "))
    validation_sound.play()
    sleep(2.0)
    os.system("cls")
    jingle.play()
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("""
                          ██████╗ ██████╗  ██████╗ ██╗      ██████╗  ██████╗ ██╗   ██╗███████╗          
                          ██╔══██╗██╔══██╗██╔═══██╗██║     ██╔═══██╗██╔════╝ ██║   ██║██╔════╝          
                █████╗    ██████╔╝██████╔╝██║   ██║██║     ██║   ██║██║  ███╗██║   ██║█████╗      █████╗
                ╚════╝    ██╔═══╝ ██╔══██╗██║   ██║██║     ██║   ██║██║   ██║██║   ██║██╔══╝      ╚════╝
                          ██║     ██║  ██║╚██████╔╝███████╗╚██████╔╝╚██████╔╝╚██████╔╝███████╗          
                          ╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚══════╝ ╚═════╝  ╚═════╝  ╚═════╝ ╚══════╝   
                                                 
                                                 Le prince exilé                                                                                       
    """)
    sleep(4.0)
    os.system("cls")
    beginning_music.play(-1)
    os.system("cls")
    print("")
    print("")
    Sentence("Vous êtes " + Prince_stats[0] + " , heritier du royaume des démons.")
    sleep(2.0)
    Sentence("Durant toute votre enfance, votre père, le roi démon, vous racontait des récits épiques sur les démons ")
    Sentence("et leurs prouesses au combat.")
    sleep(2.0)
    Sentence("Malgré toutes ces légendes invoquant la puissance légendaire de votre peuple,")
    Sentence("les histoires de votre père n'avaient rien à voir avec la réalité.")
    sleep(2.0)
    Sentence("Vous êtes né après la grande guerre, vous n'avez connu que la misère et le tabou.")
    sleep(2.0)
    Sentence("Les vieux démons de votre colonie sous-terraine en parlent sans arrêt, avec nostalgie et regret,")
    Sentence("de cette époque que vous avez du mal à imaginer...")
    skip_touch()
    print("")
    print("")
    print(Prince_stats[0], ":")
    Sentence("Une grande nation, vraiment ? Et vous ne faites rien pour changer ça ?")
    sleep(2.0)
    print("")
    Sentence(Prince_stats[0] + " n'arrêtait pas de poser cette question, mais les anciens étaient cyniques et les jeunes étaient lâches.")
    sleep(2.0)
    Sentence("Mais le roi démon finit par mourir...")
    sleep(2.0)
    Sentence("Et le jeune prince refusa le trône...")
    skip_touch()
    print("")
    print("")
    print(Prince_stats[0], ":")
    Sentence("A quoi bon accepter le trône et la couronne si ce n'est que pour gouverner sur un peuple fatigué et mourant ?")
    sleep(2.0)
    Sentence("Les humains mangent à leur faim et sont libres !")
    sleep(2.0)
    Sentence("Sans parler de leurs raids sur notre montagne ! Ils enlèvent nos femmes et nos enfants, ")
    Sentence("tuent nos frères et nos pères !")
    Sentence("ET NOUS ALLONS LES LAISSER FAIRE ?")
    sleep(2.0)
    Sentence("Je refuse de revoir mon peuple ainsi...")
    sleep(2.0)
    Sentence("Et je vous prouverai que nous pouvons regagner notre gloire passée...")
    sleep(3.0)
    skip_touch()
    print("")
    print("")
    Sentence("Personne ne répondit au jeune prince...")
    sleep(2.0)
    Sentence("Poussé par sa fierté, il prit donc la décision de s'exiler et ne revenir qu'une fois son objectif atteint...")
    sleep(2.0)
    Sentence("Il récupéra une vieille épée qui n'avait pas servi depuis la grande guerre.")
    Sentence("ainsi qu'une cape, pouvant dissimuler son apparence au besoin.")
    Sentence("Il mit aussi quelques potions de soin et de mana dans son sac en cas de danger.")
    Sentence("Il était prêt à commencer son voyage et se mit à partir...")
    skip_touch()
    print("")
    print("")
    print("??? :")
    Sentence("Attendez jeune prince !")
    print("")
    Sentence("C'était le vieux Zazranoth, un ancien guerrier de l'armée du roi...")
    Sentence("Probablement l'un des seuls de la colonie à vouloir s'opposer aux humains")
    skip_touch()
    print("")
    print("")
    print("Zazranoth :")
    Sentence("Jeune prince, vous ne pouvez pas partir comme ça, sans que je vous explique comment combattre les humains !")
    sleep(2.0)
    Sentence("J'ai beau avoir 350 années derrière moi, je n'ai pas pour autant oublié la fureur des combats.")
    sleep(2.0)
    print("")
    Sentence("C'est vrai qu'il est vieux et malade, mais beaucoup d'histoires de grandes victoires lui sont dédiées.")
    Sentence(Prince_stats[0] + " à toujours rit en imaginant ce vieux démon tout ratatiné combattre des centaines d'humains.")
    skip_touch()
    print("")
    print("")
    print(Prince_stats[0])
    Sentence("D'accord vieux guerrier, ça ne pourrait que m'aider, apprenez-moi.")
    sleep(2.0)
    print("")
    Sentence("Les deux démons se dirigèrent vers la vieille armurerie et se placèrent devant un mannequin de combat.")
    skip_touch()
    print("")
    print("")
    print("Zazranoth :")
    Sentence("Excuse-moi " + Prince_stats[0] + " mais vu ton nouveau statut je vais me permettre de te tutoyer.")
    Sentence("Tu vois ce mannequin, il représente un humain, tu vas le combattre.")
    sleep(2.0)
    Sentence("Mets ta garde !")
    print("")
    sleep(2.0)
    Sentence(Prince_stats[0] + " sortit l'épée de son foureau et fit face au mannequin, impatient de le détruire.")
    sleep(3.0)
    beginning_music.fadeout(1000)
    sleep(1.0)
    tutorial_music.play(-1)
    os.system("cls")
    print("")
    print( "Mannequin : 20 pv", "                         ", Prince_stats[0], ": 60 pv")
    print("                                                                 Mana : 15")
    print("")
    sleep(2.0)
    print("Zazranoth :")
    Sentence("Voici comment tu peux observer le cours du combat.")
    sleep(2.0)
    Sentence("En haut à gauche se trouve la vie de l'adversaire, si elle arrive à 0 il meurt et tu gagnes.")
    sleep(2.0)
    Sentence("En haut à droite se trouve ta vie à toi, si elle arrive à 0 tu meurs, mais on va éviter que ça arrive hein ?")
    sleep(2.0)
    Sentence("En bas à droite se trouve ta mana, elle te permet de lancer des sorts que nous verrons plus tard.")
    sleep(2.0)
    Sentence("Voyons maintenant les bases du combat jeune prince.")
    sleep(3.0)
    os.system("cls")
    print("")
    print("Mannequin : 20 pv", "                         ", Prince_stats[0], ": 60 pv")
    print("                                                                 Mana : 15")
    print("")
    print("1. Attaquer")
    print("2. Magie")
    print("3. Coup bas")
    print("4. Fuite")
    print("")
    sleep(2.0)
    print("Zazranoth :")
    Sentence("Voilà ton menu de combat, il faut être idiot pour ne pas le comprendre.")
    sleep(2.0)
    Sentence("'1' te permet d'attaquer. La suite, on la verra plus tard donc pas touche !")
    sleep(2.0)
    Sentence("L'attaque permet de frapper avec ton arme,")
    Sentence("tu infligeras des dégâts composés de ta puissance multipliée par le bonus que t'apporte ton arme,")
    Sentence("Mais le coup sera amorti par l'armure de ton adversaire.")
    sleep(2.0)
    Sentence("Pour une raison que j'ignore, tu as récupéré ce bout de métal rouillé, mais bref il t'apporte un bonus de 1.2 dégâts.")
    sleep(3.0)
    os.system("cls")
    print("")
    print("Mannequin : 30 pv", "                         ", Prince_stats[0], ": 60 pv")
    print("                                                                 Mana : 15")
    print("")
    print("1. Attaquer")
    print("2. Magie")
    print("3. Coup bas")
    print("4. Fuite")
    print("")
    print("Zazranoth :")
    Sentence("Essaye de l'attaquer ! Entre '1' !")
    rep = str(input("=> "))
    while rep != "1":
        if rep != "1":
            Sentence("Restez concentré ! On recommence !")
            rep = str(input())
        elif rep == "1":
            print("")
    sword_sound.play()
    Sentence("Vous mettez un coup d'épée rouillée au mannequin.")
    print("")
    print("vous infligez 9 dégâts au mannequin")
    sleep(2.0)
    os.system("cls")
    print("")
    print("Mannequin : 21 pv", "                         ", Prince_stats[0], ": 60 pv")
    print("                                                                 Mana : 15")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    sleep(2.0)
    print("Zazranoth :")
    Sentence("Ce n'est pas un mauvais coup, tu lui as retiré un peu moins d'un tiers de sa vie !")
    Sentence("Plus tu monteras de niveau, plus ta puissance de base augmentera !")
    sleep(2.0)
    Sentence("Je pense qu'il est inutile de recommencer, passons à présent à la magie.")
    sleep(3.0)
    os.system("cls")
    print("")
    print("Mannequin : 21 pv", "                         ", Prince_stats[0], ": 60 pv")
    print("                                                                 Mana : 15")
    print("")
    print("1. Attaquer")
    print("2. Magie")
    print("3. Coup bas")
    print("4. Fuite")
    print("")
    sleep(2.0)
    print("Zazranoth :")
    Sentence("'2' te permet d'utiliser la magie,")
    sleep(2.0)
    Sentence("Son utilisation est limitée car elle dépend de ta mana, mais elle à l'avantage d'ignorer l'armure.")
    sleep(2.0)
    Sentence("Entre '2' pour ouvrir le menu des sorts.")
    rep = str(input("=> "))
    while rep != "2":
        if rep != "2":
            Sentence("C'est pas difficile pourtant ! On recommence !")
            rep = str(input())
        elif rep == "2":
            print("")
    validation_sound.play()
    os.system("cls")
    print("")
    print("Mannequin : 21 pv", "                         ", Prince_stats[0], ": 60 pv")
    print("                                                                 Mana : 15")
    print("")
    print("1. Rayon démoniaque mineur | coût : 7 mana")
    print("2. Retour au menu des actions")
    sleep(2.0)
    print("Zazranoth :")
    Sentence("Pour l'instant tu ne disposes que de Rayon démoniaque mineur, autant te dire qu'il n'a de démoniaque que son nom.")
    Sentence("C'est le sort de base que tous les magiciens apprennent pour se défendre, il te coûte 7 de mana")
    Sentence("Si tu changes d'avis ou que tu n'as plus de mana, tu peux retourner dans le menu des actions.")
    sleep(2.0)
    Sentence("Il est temps de lui balancer ton Rayon démoniaque mineur !")
    Sentence("Appuie sur 1")
    rep = str(input("=> "))
    while rep != "1":
        if rep != "1":
            Sentence("Sérieusement ? On recommence !")
            rep = str(input("=>"))
        elif rep == "1":
            print("")
    print("Vous concentrez votre mana et vous envoyez un rayon de faible puissance.")
    evil_beam_spell.play()
    print("")
    print("Vous infligez 11 dégâts au mannequin")
    sleep(2.0)
    os.system("cls")
    print("")
    print("Mannequin : 10 pv", "                         ", Prince_stats[0], ": 60 pv")
    print("                                                                 Mana : 8")
    print("")
    print("")
    print("")
    print("")
    sleep(2.0)
    print("Zazranoth :")
    Sentence("HAHA joli coup gamin ! Excuse moi, la violence me manque...")
    sleep(3.0)
    Sentence("Voilà pour la magie ! Plus tu augmenteras de niveau,")
    Sentence("plus tu auras de mana et de sorts, et plus tes anciens sorts seront puissants.")
    sleep(2.0)
    Sentence("Il est temps pour toi de voir une dernière façon de combattre.")
    sleep(3.0)
    os.system("cls")
    print("")
    print("Mannequin : 10 pv", "                         ", Prince_stats[0], ": 60 pv")
    print("                                                                 Mana : 8")
    print("")
    print("1. Attaquer")
    print("2. Magie")
    print("3. Coup bas")
    print("4. Fuite")
    print("")
    sleep(2.0)
    print("Zazranoth :")
    Sentence("Ce dernier style est important car il pourra te sauver la mise plus d'une fois... ou bien causer ta perte.")
    sleep(2.0)
    Sentence("Tu vas t'aventurer seul dans un monde hostile, certains humains sont très forts ou très résistants,")
    Sentence("tu vas devoir faire preuve de ruse...")
    sleep(2.0)
    Sentence("La ruse s'illuste en combat par l'art du coup bas.")
    Sentence("Rien de mieux qu'un coup déshonorable pour prendre l'avantage sur l'adversaire.")
    Sentence("Elles sont très utiles mais ont peu de chance de réussir.")
    sleep(2.0)
    Sentence("Pour te parler de la ruse il faut que je te parle des statistiques de ton adversaire,")
    Sentence("elles se résument par l'armure, l'esquive et la précision.")
    Sentence("Les coups bas les affectent directement et indéfiniement.")
    sleep(2.0)
    Sentence("Entre '3' pour aller au menu des coups-bas.")
    rep = str(input("=> "))
    while rep != "3":
        if rep != "3":
            Sentence("Tu te moques de moi ?! On recommence")
            rep = str(input())
        elif rep == "3":
            print("")
    validation_sound.play()
    sleep(1.0)
    os.system("cls")
    print("")
    print("Mannequin : 10 pv", "                         ", Prince_stats[0], ": 60 pv")
    print("                                                                 Mana : 8")
    print("")
    print("1. Sable dans les yeux | 1 sur 2")
    print("2. retour au menu des actions")
    print("")
    sleep(2.0)
    print("Zazranoth :")
    Sentence("Pour l'instant tu ne disposes que d'assez d'imagination pour balancer du sable dans les yeux de l'adversaire.")
    sleep(2.0)
    Sentence("Et il t'en faut aussi pour imaginer des yeux à un mannequin...")
    Sentence("Bref, supposons que ce mannequin a des yeux, tu lui balances du sable !")
    sleep(2.0)
    Sentence("Malheureusement, les yeux c'est petit, donc peu de chance de réussir.")
    Sentence("Ta probabilité de toucher est située à côté du nom de l'attaque.")
    Sentence("Mais vas y tente ta chance !")
    sleep(2.0)
    rep = str(input("=> "))
    while rep != "1":
        if rep != "1":
            Sentence("On s'applique et on recommence !")
            rep = str(input())
        elif rep == "1":
            print("")
    Sentence("Vous jetez du sable sur ce qui semble être les yeux du mannequin.")
    sand_low_blow.play()
    print("")
    print("Coup-bas réussi !")
    sleep(2.0)
    print("Mannequin perd 10% de précision !")
    sleep(2.0)
    os.system("cls")
    print("")
    print("Mannequin : 10 pv", "                         ", Prince_stats[0], ": 60 pv")
    print("                                                                 Mana : 8")
    print("")
    print("")
    print("")
    print("")
    sleep(2.0)
    print("Zazranoth :")
    Sentence("Tu as réussi ! Mais tu n'auras pas toujours autant de chance !")
    sleep(2.0)
    Sentence("Pour débloquer des nouveaux coups bas il te faut augmenter ton niveau de filouterie.")
    sleep(2.0)
    Sentence("Je pourrais appeler ça autrement mais j'ai bien trop de respect pour feu la Reine.")
    Sentence("Ces niveaux augmentent si tu fais des actions déshonorables réussies au combat ou si tu es immoral.")
    sleep(2.0)
    Sentence("Au fil de ces niveaux tu débloqueras 3 autres techniques de l'école du Coup bas,")
    Sentence("Mais une légende raconte qu'au coeur de la forêt, une énigme se révèle à ceux qui ont maitrisé l'art du Coup bas...")
    sleep(2.0)
    Sentence("L'énigme du serpent tâcheté réussie permet d'apprendre un coup ultime, élaboré par le grand Sagzinoth lui-même.")
    sleep(2.0)
    Sentence("À toi de voir si tu souhaite suivre cette voie.")
    sleep(2.0)
    Sentence("Voilà pour les actions de combat.")
    Sentence("Il existe aussi la fuite mais elle n'est conseillée qu'en cas d'extrême urgence.")
    Sentence("Si tu fuis tu te retrouveras sur ta précédente position.")
    sleep(2.0)
    Sentence("Achève ce mannequin d'un coup d'épée.")
    sleep(2.0)
    os.system("cls")
    print("")
    print("Mannequin : 10 pv", "                         ", Prince_stats[0], ": 60 pv")
    print("                                                                 Mana : 8")
    print("")
    print("1. Attaquer")
    print("2. Magie")
    print("3. Coup bas")
    print("4. Fuite")
    print("")
    rep = str(input("=> "))
    while rep != "1" :
        if rep != "1":
            Sentence("Un coup d'épée, c'est simple non ? On recommence !")
            rep = str(input())
        elif rep == "1":
            print("")
    sword_sound.play()
    print("D'un dernier coup d'épée, vous tranchez le mannequin de combat en deux.")
    sleep(1.5)
    os.system("cls")
    print("")
    print("vous infligez 11 dégats au mannequin")
    os.system("cls")
    tutorial_music.fadeout(1000)
    sleep(1.0)
    beginning_music.play()
    print("")
    print("")
    sleep(2.0)
    print("Zazranoth :")
    Sentence("Félicitations, tu as tué un mannequin mais sache que les humains riposteront et useront parfois de sorts.")
    sleep(2.0)
    Sentence("Je suis rassuré quant à ta survie, tu n'es pas mauvais du tout.")
    sleep(2.0)
    Sentence("Je pense que tu sais tout ce qu'il y a à savoir pour survivre...")
    sleep(0.5)
    print(".")
    sleep(0.5)
    print(".")
    sleep(0.5)
    print(".")
    Sentence("Ah oui, j'oubliais !")
    Sentence("Tu ne peux regarder et utiliser ton sac uniquement hors des combats,")
    Sentence("donc prépare toi bien avant chaque déplacement.")
    sleep(2.0)
    Sentence("Et il est facile de se perdre sans carte,")
    Sentence("je te conseille vivement de dessiner une carte sur du papier ou tout ce qui pourra te servir.")
    sleep(3.0)
    Sentence("...")
    print("")
    Sentence("En tout cas, je te souhaite du courage jeune prince...")
    sleep(1.5)
    Sentence("Si tu réussis, il se peut que tu inspires les jeunes démons de ta génération.")
    Sentence("Alors une nouvelle ère commencera, celle du retour des démons.")
    sleep(2.0)
    Sentence("Notre avenir t'appartient à présent...")
    Sentence("Va, et montre aux humains que nous n'avons pas dit notre dernier mot.")
    skip_touch()
    print("")
    Sentence("Le vieux Zazranoth posa alors sa main sur l'épaule du jeune prince puis s'en alla...")
    Sentence("laissant le jeune " + Prince_stats[0] + " face à son destin.")
    sleep(3.0)
    #Exit_Mountain()


#def Exit_Mountain():























