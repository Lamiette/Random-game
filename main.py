import random
test = random.randrange(101)

print(test)

joueur_un = 0
compteur_joueur_un = 0
joueur_deux = 0
compteur_joueur_deux = 0
# z = int(input("Tentative max : "))
while joueur_un != test or joueur_deux != test:

    joueur_un = input("Joueur 1 saisis un nombre : ")
    compteur_joueur_un = compteur_joueur_un + 1

    if joueur_un == "":
        exit()
    if int(joueur_un) < test:
        print ("plus haut")        
    elif int(joueur_un) > test:
        print("plus bas")
    else:
        print("-" * 20)
        print("Joueur 1 l'emporte")
        break
       


    joueur_deux = input("Joueur 2 saisie un nombre : ")
    compteur_joueur_deux = compteur_joueur_deux + 1

    if joueur_deux == "":
        exit()
    if int(joueur_deux) < test:
        print("Plus haut")
    elif int(joueur_deux) > test:
        print("Plus bas")
    else:
        print("-" * 20)
        print("Joueur 2 l'emporte")
        break
        
    
# if y == z:         
#    print("nombre essai dépassé")       

print("-" * 20)
print ("La réponse était : ", test)
print("-" * 20)
print("Nombre essai joueur 1 :", compteur_joueur_un)
print("-" * 20)
print("Nombre essai joueur 2 :", compteur_joueur_deux)
print("-" * 20)
