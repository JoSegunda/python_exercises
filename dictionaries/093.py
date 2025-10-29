player = dict()
players= list()
goals = []
stopCondition = "y"
print("=="*20)






while stopCondition not in "nN":
    name = input("Nome do Jogador: ")
 
    n = int(input(f"Quantas partidas {name} jogou: "))
    for i in range(n):
        goals.append(int(input(f"Quantos gols na partida {i+1}? ")))

    stopCondition = input("Quer continuar? [S / N]: ")
    player[name] = goals[:]
    goals.clear()

print("=="*20)
print("Cod      Nome      golos       total")
print("--"*20)

i = 1
for k,v in player.items():
    print(f"{i:<9}{k:<9} {v} {sum(v):>10}")
    i += 1

# for j in range(len(player['Goals'])):
#     print(f"    Na partida {j+1}, fez {player['Goals'][j]} gols.")

# print(f"Foi um total de {player['Total']} gols.")