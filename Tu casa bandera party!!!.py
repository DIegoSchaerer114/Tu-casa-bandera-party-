import random
import imaplib
posR = 1
posB = 50
while True:
    if(posR>=196 or posB >=196):
       break
 
    dado= random.randint (1,6)
    dado2 = random.randint (1,6)
    DadoT = dado + dado2
    posR += DadoT

    dado= random.randint (1,6)
    dado2 = random.randint (1,6)
    DadoT = dado + dado2
    posB += DadoT
    print(f"A:{posR} B:{posB}")