from random import *
floor = 0
roof = 101
nbr_to_guess = randint(floor,roof)

print(nbr_to_guess)

liste_joueur = []
liste_bot = []

nombre_de_joueur = int(input("Entrez le nombre de joueur : "))
nombre_de_bot = int(input("Entrez le nombre de Bot : "))
for x in range(nombre_de_joueur) :
    liste_joueur.append(str(input("Entrez votre nom : "))) 

for y in range(nombre_de_bot) :
    liste_bot.append(str(input("Entrez un nom : ")))


print("Voici la liste des joueurs :",*liste_joueur, sep="\n")  
print("Voici la liste des Bots :" ,*liste_bot, sep='\n')


for z in liste_joueur:
    
    while z != nbr_to_guess:
        z=input("Joueur "+ z +" Saisissez un nombre : ")
        if z == "":
            exit()
        if int(z) < nbr_to_guess:
            print ("plus haut")        
        elif int(z) > nbr_to_guess:
            print("plus bas")
        else:
            print("-" * 20)
            print("Joueur "+z+" l'emporte")
            break
