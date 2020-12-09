from time import sleep

def choixportes():
    print("Sonner la retraite ou tenter d'abattre les portes")
    print("1. Sonner la retraite")
    print("2. Assaillir les portes")
    choix = str(input())
    while True:
          if choix == "1":
              print("retraite")
              break
          elif choix == "2":
              print("assautportes")
              break
          else:
            print("")
          print("Choix indisponnible.")
          sleep(1.0)
          final = choixportes()
          return final

