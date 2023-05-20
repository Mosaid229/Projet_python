import math
import random
def gagner(nbr1) :
    gagne=(nbr1*3)+nbr1
    return gagne
def gains(nbr2) :
    nbre=nbr2/2 + nbr2
    gain=math.ceil(nbre)
    return gain
def Couleur(nbr3) :
    couleur="rouge"
    if (nbr3%2)==0 :
        couleur="noir"
    return couleur
print("\t\t\tBienvenue au Casino !!!\n")
def Numero() :
    numero=input("Veuillez choisir un numéro compris entre 0 et 49 : ")
    try :
        numero=int(numero)
        assert numero>=0
        assert numero<50 
    except ValueError :
        numero=input("Veuillez entrer un vrai numéro :")
        numero=int(numero)
    except AssertionError :
        numero=input("Veuillez entrer un numero compris entre 0 et 49: ")
        numero=int(numero)
    return numero
def Mise() :
    mise=input("Combien voulez vous miser ?? ")
    try :
        mise=int(mise)
        assert mise>0
    except ValueError :
        mise=input("Veuillez entrer un vrai nombre pour miser: ")
        mise=int(mise)
    except AssertionError :
        mise=input("Veuillez entrer un nombre supérieure à 0: ")
        mise=int(mise)
    return mise
def Jeu(num , mis, revenu) :
    print("Votre mise est de {} $".format(mis))
    print("\tC'est parti, Je lance le jeu !!")
    jeu=random.randrange(50)
    print("\tLe numéro gagnant est :",jeu)
    if num==jeu :
        print("\tVous avez gagner !!!\n")
        revenu=gagner(mis)
        print("\tVotre revenu est :",revenu,"$")
    elif Couleur(num)==Couleur(jeu) :
        print("\tVotre numéro est de la même couleur que le numéro gagnant !!!\n")
        revenu=gains(mis)
        print("\tVotre revenu est :",revenu,"$")
    else :
        print("\tVous avez perdu {} !!!".format(mis))
        revenu=revenu - mis
        print("\tVotre revenu est :",revenu,"$")
    return revenu
numero1=Numero()
mise1=Mise()
jeu1=Jeu(numero1 , mise1, mise1)
i=int()

conti=str()

if jeu1 > 0:
    while i<3:
        conti=input("Voulez-vous continuer (O/N) :")

        if conti=="O" :
            Nnumero=Numero()
            Nmise=Mise()
            t=0
            while (Nmise > jeu1 and t < 3):
                print("Vous n'avez plus assez d'argent pour miser aussi tant !!")
                Nmise=Mise()
                t += 1
            if Nmise<=jeu1:
                Jeu(Nnumero , Nmise, jeu1)
            else:
                print("Désolé vous n'avez pas assez de sous")

        elif conti=="N" :
            print("Merci d'avoir jouer à notre jeu et rensez-vous à très bientôt !!")

        elif conti != "O" and conti != "N" :
            print("Veuillez choisir O pour oui et N pour non")
            conti=input("Voulez-vous continuer (O/N) :")
        i+=1

    if i>3:
        print("Vous avez deja joué 3 fois de suite! Revenez apres")