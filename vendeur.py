from mob import *
from index import *
from inventaire import *


def sell():
    print(char['gold'])
    print("Vous voulez vendre quoi ?")
    print_objet_sell()
    Kinv = char['inv'].keys()
    Kinv_list = list(Kinv)
    while True:
        Ninv = int(input("Quelle objet :"))
        if Ninv < 1 or Ninv > len(index_objet):
            print("Choix indisponnible.")

        else:
            objet = Kinv_list[Ninv - 1]
            char['gold']['Argent'] += index_objet[str(objet)][0]
            print("Vous avez maintenant", char['gold']['Argent'],"d'or")
            break

sell()