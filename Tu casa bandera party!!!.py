import random
import imaplib
posR = 1
posB = 50
#Bandera posicion rojo
BP=[1, 176]
#BAndera posicion Azul
BB=[50, 100]
#Puntos de bandera roja
PR = 0
#Puntos de bandera Blue
PB = 0

ubr=BB[0]
#Ubi de bandera Blue
ubb=BP[0]

#El dado
def tirarDados():
    dado= random.randint (1,6)
    dado2 = random.randint (1,6)
    DadoT = dado + dado2   
    return DadoT


while True:  

    posR += tirarDados()
    posB += tirarDados()

    if(posR>=196):
       posR=50+(posR-196)
  
    if(posB >=196):
       posB=50+(posB-196)

    
    print(f"A:{posR} B:{posB}")
    print(f"puntos de A:{PR} puntos de B:{PB}")
       
    #Se utiliza para bloquear lugares que no se puede acceder tan facilmente
    if posR == ubb:
        PR+=1
        ubb=BB[1]
    if posB == ubr:
        PB+=1
        ubr=BP[1]

    if PB>4 or PR>4:
        break

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

    #Te pregunta para ver si vas a cambiar de dirrección
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
    
        #las posiciones de los jugadores
    

 