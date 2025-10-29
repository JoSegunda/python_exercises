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
    player[name] = goals.copy()
    goals = []

print("==="*20)
print("Cod  Nome         golos              total")
print("---"*20)

i = 1
for k,v in player.items():
    print(f"{i:<5}{k:<12}{str(v):<20}{sum(v):>5}")
    i += 1
print("---"*20)
# for j in range(len(player['Goals'])):
#     print(f"    Na partida {j+1}, fez {player['Goals'][j]} gols.")

# print(f"Foi um total de {player['Total']} gols.")