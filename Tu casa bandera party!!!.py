import random
import imaplib
posR = 1
posB = 50
while True:
    if(posR>=196):
       posR=50
    if(posB >=1000):
       break
    
    dado= random.randint (1,6)
    dado2 = random.randint (1,6)
    DadoT = dado + dado2
    posR += DadoT

    dado= random.randint (1,6)
    dado2 = random.randint (1,6)
    DadoT = dado + dado2
    posB += DadoT
    print (f"A:{posR} B:{posB}")


    if posR == 12:
        print("bloqueo")
    if posR == 151:
        print("bloqueo")
    if posR == 166:
        print("bloqueo")
    if posR == 70:
        print("bloqueo")
    if posR == 38:
        print("bloqueo")
    if posR >= 196:
        posR = 50+(posR-196)

    if posR==151:
        print =input("Seguir adelande o cambiar de dirección")
    if (posR == "Seguir adelante"):
        posR+0
    if (posR == "Cambiar de dirección"):
        posR-134 and posB-134
    
        