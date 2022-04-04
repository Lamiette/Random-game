from random import *
floor = 0
roof = 101
nbr_to_guess = randint(floor,roof)

print(nbr_to_guess)

joueur_un = 0
compteur_joueur_un = 0

joueur_deux = 0
compteur_joueur_deux = 0

joueur_bot = randint(floor,roof)
compteur_joueur_bot = 0

# z = int(input("Tentative max : "))
while joueur_un != nbr_to_guess or joueur_deux != nbr_to_guess or joueur_bot != nbr_to_guess:

    joueur_un = input("Joueur 1 saisis un nombre : ")
    compteur_joueur_un += 1

    if joueur_un == "":
        exit()
    if int(joueur_un) < nbr_to_guess:
        print ("plus haut")        
    elif int(joueur_un) > nbr_to_guess:
        print("plus bas")
    else:
        print("-" * 20)
        print("Joueur 1 l'emporte")
        break
       


    joueur_deux = input("Joueur 2 saisie un nombre : ")
    compteur_joueur_deux += 1

    if joueur_deux == "":
        exit()
    if int(joueur_deux) < nbr_to_guess:
        print("Plus haut")
    elif int(joueur_deux) > nbr_to_guess:
        print("Plus bas")
    else:
        print("-" * 20)
        print("Joueur 2 l'emporte")
        break

    
    compteur_joueur_bot += 1
    print("-" *20)
    
    print(joueur_bot)
    historique_bot=[]
    historique_bot.append(joueur_bot)
    if compteur_joueur_un == 1 or compteur_joueur_deux == 1:
        continue
        compteur_joueur_bot += 1

    elif joueur_bot != nbr_to_guess:
        if int(joueur_bot) < nbr_to_guess:
            print("Plus haut")
            floor = joueur_bot
            joueur_bot = randint(floor,roof)
            historique_bot.append(joueur_bot)
            print(joueur_bot)
        else:
            print("Plus bas")
            roof = joueur_bot
            joueur_bot = randint(floor,roof)
            historique_bot.append(joueur_bot)
            print(joueur_bot)
    else :
         print("Le bot l'emporte")
         break


        
    
# if y == z:         
#    print("nombre essai dépassé")       

print("-" * 20)
print ("La réponse était : ", nbr_to_guess)
print("-" * 20)
print("Nombre essai joueur 1 :", compteur_joueur_un)
print("-" * 20)
print("Nombre essai joueur 2 :", compteur_joueur_deux)
print("-" * 20)
print("Nombre essai Bot :", compteur_joueur_bot)
print("-" * 20)

print(historique_bot)
