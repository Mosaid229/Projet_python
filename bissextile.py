annee = input("Veuillez entrer une année dont vous voulez savoir si c'est bissextile ou pas :")
annee = int(annee)
if (annee%4) != 0 :
    print("Cette année n'est pas une année bissextile")
elif (annee%100) == 0 :
    if (annee%400) == 0 :
        print("Cette année est bissextile")
    else :
        print("Cette année n'est pas bissextile")
else : 
    print("Cette année est bissextile")        