import random
from random import randint


class joueur:
    def __init__(self,prenom,score) -> None:
        self.prenom = prenom
        self.score = score

        
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


for joueurs in range(nombre_de_joueur) :
    prenom = input("Entrez votre nom :")
    score = 0
    liste_joueur.append(joueur(prenom, score)) 


for bots in range(nombre_de_bot) :
    prenom = random.choice(prenom_bot)
    score = 0
    liste_bot.append(joueur(prenom, score))
    
    

print("-"*25)
print("Voici la liste des joueurs : ","\n")
for joueur in liste_joueur:
    print(joueur.prenom)

print("-"*25) 
print("Voici la liste des Bots ","\n") 
for joueur in liste_bot:
    print(joueur.prenom)
print("-"*25)


for joueur in liste_joueur:
    tentative_joueur = ""
    joueur.score=0
    while tentative_joueur != nbr_to_guess:
        joueur.score += 1
        tentative_joueur=input("Joueur "+joueur.prenom+" Saisissez un nombre : ")
        if tentative_joueur == "":
            exit()
        if int(tentative_joueur) < nbr_to_guess:
            print ("Plus haut")        
        elif int(tentative_joueur) > nbr_to_guess:
            print("Plus bas")
        else:
            print("-" * 20)
            print("Partie Finit !")
            print("-" * 20)
            break


for joueur in liste_bot:
    tentative_bot = 0
    joueur.score=0
    while tentative_bot != nbr_to_guess:
        joueur.score += 1
        if int(tentative_bot) < nbr_to_guess:
            print("Plus haut")
            floor = tentative_bot +1
            tentative_bot = randint(floor,roof)            
            print(tentative_bot)
            
        elif int(tentative_bot) > nbr_to_guess:
            print("Plus bas")
            roof = tentative_bot -1
            tentative_bot = randint(floor,roof)
            print(tentative_bot)
            
        elif int(tentative_bot) == nbr_to_guess:
            print("-" * 20)
            print("Partie Finit !")
            print("-" * 20)
            break



liste_joueur.sort(key=lambda joueur: joueur.score)

print("Le joueur",liste_joueur[0].prenom,"remporte la partie en",liste_joueur[0].score,"tentatives")
print("Le joueur",liste_joueur[1].prenom,"termine 2ème en",liste_joueur[1].score,"tentatives")
print("Le joueur",liste_joueur[2].prenom,"termine 3ème en",liste_joueur[2].score,"tentatives")

liste_bot.sort(key=lambda joueur: joueur.score)

print("-" * 20)
print("Le joueur",liste_bot[0].prenom,"remporte la partie en",liste_bot[0].score,"tentatives")
print("Le joueur",liste_bot[1].prenom,"termine 2ème en",liste_bot[1].score,"tentatives")
print("Le joueur",liste_bot[2].prenom,"termine 3ème en",liste_bot[2].score,"tentatives")
