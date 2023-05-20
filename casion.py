import math
import random
def gagner(nbr1) :
    gagne=(nbr1*3)+nbr1
    return gagne
def gains(nbr2) :
    nbre=nbr2/2
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
    return Mise
def Jeu(num , mis) :
    print("Votre mise est de",mis,"$\n")
    print("\tC'est parti, Je lance le jeu !!")
    #jeu=random.randrange(50)
    jeu=44
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
        print("\tVous avez perdu !!!")
        revenu=0
    return revenu
numero1=Numero()
mise1=Mise()
jeu1=Jeu(numero1 , mise1)
i=0
#while jeu1!=0 and i<=3:
 #   conti=input("Voulez-vous continuer (O/N) :")
  #  if conti=="O" :
   #     Nnumero=Numero()
    #    Nmise=Mise()
     #   t=0
      #  while Nmise>jeu1 :
       #     print("Vous n'avez plus assez d'argent pour miser aussi tant !!")
        #    Nmise=Mise()
        #    t+=1
        #Jeu(Nnumero , Nmise)
    #elif conti=="N" :
     #       print("Merci d'avoir jouer à notre jeu et rensez-vous à très bientôt !!")
    #elif conti!="O" and conti!="N" :
     #   print("Veuillez choisir O pour oui et N pour non") 
      #  Nnumero=Numero()
       # Nmise=Mise()
        #t=0
        #while Nmise>jeu1 :
         #   print("Vous n'avez plus assez d'argent pour miser aussi tant !!")
          #  Nmise=Mise()
           # t+=1
        #Jeu(Nnumero , Nmise) 
    #i+=1        



