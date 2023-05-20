annee = input("Veuillez entrer une année dont vous voulez savoir si c'est bissextile ou pas :")
while type(annee) is not int :
    try :
        annee = int(annee)
        assert annee > 0
    except ValueError :
        annee = input("Veuillez saisir une année correcte :")
        annee = int(annee)
    except AssertionError :
        annee = input("Veuillez saisir une année supérieure à 0 :")
        annee = int(annee)
if (annee%4) != 0 :
    print("Cette année n'est pas bissextile")
elif (annee%100) == 0 :
    if (annee%400) == 0 :
        print("Cette année est bissextile")
    else :
        print("Cette année n'est pas bissextile")
else : 
    print("Cette année est bissextile")        