import random
import imaplib
posR = 1
posB = 50

def tirarDados():
    dado= random.randint (1,6)
    dado2 = random.randint (1,6)
    DadoT = dado + dado2   
    return DadoT

while True:
    if(posR>=196):
       posR=50
    if(posB >=1000):
       break
    

    posR += tirarDados()

    dado= random.randint (1,6)
    dado2 = random.randint (1,6)
    DadoT = dado + dado2
    posB += DadoT
    print(f"A:{posR} B:{posB}")


    if posR == 12:
        print("bloqueo")
    if posR == 166:
        print("bloqueo")
    if posR == 70:
        print("bloqueo")
    if posR == 38:
        print("bloqueo")
    if posR >= 196:
        posR = 50+(posR-196)

    if(posR>150 and posR<=162):
        direc =input("Seguir adelande o cambiar de dirección")
        if (direc == "S" or direc == "Seguir adelante"):
            pass
        if (direc == "N" or direc == "Cambiar de dirección"):
            posR = (posR-151)+16
            print (f"A:{posR} B:{posB}")

    if(posR>96 and posR<=109):
        direc =input("Seguir adelande o cambiar de dirección")
        if (direc == "S" or direc == "Seguir adelante"):
            pass
        if (direc == "N" or direc == "Cambiar de dirección"):
            posR = (posR-97)+16
            print (f"A:{posR} B:{posB}")

    if(posR>166 and posR<=178):
        direc =input("Seguir adelande o cambiar de dirección")
        if (direc == "S" or direc == "Seguir adelante"):
            pass
        if (direc == "N" or direc == "Cambiar de dirección"):
            posR = (posR-167)+44
            print (f"A:{posR} B:{posB}")
    
    if(posR>79 and posR<=92):
        direc =input("Seguir adelande o cambiar de dirección")
        if (direc == "S" or direc == "Seguir adelante"):
            pass
        if (direc == "N" or direc == "Cambiar de dirección"):
            posR = (posR-80)+44
            print (f"A:{posR} B:{posB}")