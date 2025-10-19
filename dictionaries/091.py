from random import randint
from time import sleep
jogadores = dict()
playerOrdered = dict()
maxVal = 0
playerKey = ""
print("Valores sorteados:")
for i in range(1, 5):
    n = randint(1,6)
    print(f"    O jogador{i} tirou {n}")
    sleep(1)
    jogadores[f"jogador{i}"] = n

for j in range(1,5):
    maxVal = 0
    for k in jogadores:
        if (k in jogadores) and (jogadores[k] > maxVal) :
            maxVal = jogadores[k]
            playerKey = k
    
    playerOrdered[playerKey] = maxVal
    if(playerKey in jogadores):
        jogadores.pop(playerKey)


print("Ranking dos jogadores:")
maxVal = 1
for player in playerOrdered:
    sleep(1)
    print(f"    {maxVal}º lugar: {player} com {playerOrdered[player]}")
    maxVal += 1
