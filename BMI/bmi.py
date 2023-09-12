import numpy as np
import random as rn
import matplotlib.pyplot as plt

# Blocco generazione cittadini ed elaborazione di tali dati

# Questo piccolo array contiene una media approssimativa di cittadini normopeso, sovrappeso e obeso su un campione di circa 1000 persone
indiciObesita = [493,361,115]

popolAltezza = []
popolPeso = []

# indice obesità (normo = 0, sovra = 1, obeso = 2)
io = 0 
for i in range(len(indiciObesita)):
    for n in range(indiciObesita[io]):
        raltezza = rn.uniform(1.50,2.10)
        if io == 0:
            bmi = rn.uniform(18.5,24.99)
            rpeso = bmi*(raltezza*raltezza)
        elif io == 1:
            bmi = rn.uniform(25,29.99)
            rpeso = bmi*(raltezza*raltezza)
        elif io == 2:
            bmi = rn.uniform(30,40)
            rpeso = bmi*(raltezza*raltezza)
        popolAltezza.append(raltezza)
        popolPeso.append(rpeso)
    io=io+1

f = plt.figure()
f.set_figwidth(10)
f.set_figheight(5)

Ax1 = plt.subplot(1,2,1)
Ax2 = plt.subplot(1,2,2)

# Elaborazione e stampa dello scatter del BMI sui cittadini italiani
Ax1.scatter(popolPeso[:indiciObesita[0]],popolAltezza[:indiciObesita[0]],c = "red", label = "normopeso")
Ax1.scatter(popolPeso[indiciObesita[0]+1:indiciObesita[0]+indiciObesita[1]],popolAltezza[indiciObesita[0]+1:indiciObesita[0]+indiciObesita[1]],c = "green", label = "sovrappeso")
Ax1.scatter(popolPeso[indiciObesita[0]+indiciObesita[1]+1:],popolAltezza[indiciObesita[0]+indiciObesita[1]+1:], c = "blue", label = "obeso")
Ax1.set_xlabel("Peso (Kg)")
Ax1.set_ylabel("Altezza (m)")
Ax1.set_title("Distribuzione italiani su base BMI")
Ax1.legend()

# Elaborazione dati sui giocatori della squadra nazionale di rugby
playersAltezza = [1.83,1.95,1.83,1.89,1.90,1.96,1.78,1.84,1.80,1.77,1.98,1.85,1.81,1.78,1.89,1.78,1.81,1.84,1.82,1.91,1.95,1.93,1.76,1.87,1.76,1.83,1.95,1.83,1.91,1.92,1.90,1.86,1.98,1.85,1.98,1.74,1.83,1.80,1.88,1.91,1.84,1.84,1.88,1.86,1.86]
playersPeso = [93,115,93,90,102,117,73,124,84,98,108,111,107,85,99,90,105,90,95,106,122,112,80,100,86,102,112,107,99,106,107,125,108,90,121,83,90,94,100,115,111,110,104,90,98]

playersNormoPeso, playersNormoAltezza, playersSovraPeso, playersSovraAltezza, playersObesoPeso, playersObesoAltezza = [],[],[],[],[],[]

for n in range(len(playersAltezza)):
    t = playersPeso[n]/(playersAltezza[n]*playersAltezza[n])
    if t<25:
        playersNormoPeso.append(playersPeso[n])
        playersNormoAltezza.append(playersAltezza[n])
    elif t < 30:
        playersSovraPeso.append(playersPeso[n])
        playersSovraAltezza.append(playersAltezza[n])
    elif t > 30:
        playersObesoPeso.append(playersPeso[n])
        playersObesoAltezza.append(playersAltezza[n])

# Elaborazione e stampa dello scatter del BMI sui giocatori di rugby
Ax2.scatter(playersNormoPeso,playersNormoAltezza, c = "red", label = "normopeso")
Ax2.scatter(playersSovraPeso,playersSovraAltezza, c = "green", label = "sovrappeso")
Ax2.scatter(playersObesoPeso,playersObesoAltezza, c = "blue", label = "obeso")
Ax2.set_xlabel("Peso (Kg)")
Ax2.set_ylabel("Altezza (m)")
Ax2.set_title("Distribuzione giocatori squadra rugby su base BMI")
Ax2.legend()

plt.show()