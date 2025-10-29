player = dict()
players= list()
goals = []
print("=="*20)
for i in range():
    player['Nome'] = input("Nome do Jogador: ")
    n = int(input(f"Quantas partidas {player['Nome']} jogou: "))
    goals.append(int(input(f"Quantos gols na partida {i}? ")))

    players.append()

player['Goals'] = goals
player['Total'] = sum(goals)
print("=="*20)

for k,v in player.items():
    print(f"{k}: {v}")
print("=="*20)
print(f"O jogador {player['Nome']} jogou {n} partidas.")

for j in range(len(player['Goals'])):
    print(f"    Na partida {j+1}, fez {player['Goals'][j]} gols.")

print(f"Foi um total de {player['Total']} gols.")