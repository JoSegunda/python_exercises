player = dict()
players= list()
goals = []
stopCondition = "y"
print("=="*20)






while stopCondition not in "nN":
    name = input("Nome do Jogador: ")
 
    n = int(input(f"Quantas partidas {player[name]} jogou: "))
    for i in range(n):
        goals.append(int(input(f"Quantos gols na partida {i+1}? ")))

    player[name] = goals[:]
    del goals

# player['Goals'] = goals
# player['Total'] = sum(goals)
# print("=="*20)

# for k,v in player.items():
#     print(f"{k}: {v}")
# print("=="*20)
# print(f"O jogador {player['Nome']} jogou {n} partidas.")

# for j in range(len(player['Goals'])):
#     print(f"    Na partida {j+1}, fez {player['Goals'][j]} gols.")

# print(f"Foi um total de {player['Total']} gols.")