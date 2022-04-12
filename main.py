import random
from random import randint
floor = 0
roof = 101
nbr_to_guess = randint(floor,roof)

print(nbr_to_guess)

liste_joueur = []
liste_bot = []
prenom_bot = ['Giovanni','Marcelo','Thibaut','Idefix','Tartuffe','Gontrand','Jean']

while True:
    try:
        nombre_de_joueur = int(input("Entrez le nombre de joueur : "))
        break
    except ValueError:
        print("-"*27)
        print("Veuillez entrer un nombre !")
        print("-"*27)

while True:
    try:
        nombre_de_bot = int(input("Entrez le nombre de Bot : "))
        break
    except ValueError:
        print("-"*27)
        print("Veuillez entrer un nombre !")
        print("-"*27)


for x in range(nombre_de_joueur) :
    liste_joueur.append(str(input("Entrez votre nom : "))) 


for y in range(nombre_de_bot) :
    liste_bot = random.sample(prenom_bot, nombre_de_bot)
    
    

print("-"*25)
print("Voici la liste des joueurs :","\n",*liste_joueur, sep="\n")
print("-"*25)  
print("Voici la liste des Bots :","\n",*liste_bot, sep='\n')
print("-"*25)


for z in liste_joueur:
    y = ""
    cpt_joueur=0
    while y != nbr_to_guess:
        cpt_joueur += 1
        y=input("Joueur "+ z +" Saisissez un nombre : ")
        if y == "":
            exit()
        if int(y) < nbr_to_guess:
            print ("Plus haut")        
        elif int(y) > nbr_to_guess:
            print("Plus bas")
        else:
            print("-" * 20)
            if cpt_joueur < 2:
                print("Joueur "+z+" l'emporte en",cpt_joueur,"coup")
            else:
                print("Joueur "+z+" l'emporte en",cpt_joueur,"coups")
            break

joueur_bot = 0

for x in liste_bot:

    while joueur_bot != nbr_to_guess:
        
        if int(joueur_bot) < nbr_to_guess:
            print("Plus haut")
            floor = joueur_bot +1
            joueur_bot = randint(floor,roof)            
            print(joueur_bot)
            
        else:
            print("Plus bas")
            roof = joueur_bot -1
            joueur_bot = randint(floor,roof)
            print(joueur_bot)
            
    else :
         print("Le bot l'emporte")
         break


