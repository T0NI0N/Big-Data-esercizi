import matplotlib 


elo_A = 1580
elo_B = [1700, 1577, 1388, 1620, 1710]

K = 32
Sa = [0, 1, 0.5, 1, 0]


for i in range(len(elo_B)):
    print("Player A di rank: ",int(round(elo_A, 0)), " sfida player B di rank: ", elo_B[i])
    Ea = 1 / (1 + pow(10, ((elo_B[i] - elo_A) / 400)))
    print("Valore Ea partita: ", round(Ea, 3))
     
    if Sa[i] == 0:
        print("Sconfitta")
    if Sa[i] == 0.1:
        print("Pareggio")
    if Sa[i] == 1:
        print("Vince")
    elo_A = elo_A + K * (Sa[i] - Ea)
    print("Nuovo Elo-Ranking player A: ", int(round(elo_A,0)))