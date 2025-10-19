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
    for k in range(1,len(jogadores)+1):
        val = f'jogador{k}'
        if (val in jogadores) and (jogadores[val] >= maxVal) :
            maxVal = jogadores[val]
            playerKey = val
    
    playerOrdered[playerKey] = maxVal
    if(playerKey in jogadores):
        jogadores.pop(playerKey)

print(playerOrdered)

# print("Ranking dos jogadores:")
# for n in range(1,5):
#     print(f"{n}º lugar: {playerOrdered[n]} com {playerOrdered[playerOrdered[n]]}")
    
