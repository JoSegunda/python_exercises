player = dict()
players= list()
goals = []
print("=="*20)

player['Nome'] = input("Nome do Jogador: ")
n = int(input(f"Quantas partidas {player['Nome']} jogou: "))
for i in range(n):
    goals.append(int(input(f"Quantos gols na partida {i+1}? ")))

player['Goals'] = goals
player['Total'] = sum(goals)
print("=="*30)
print(player)
print("=="*30)

for j in range(len(player['Goals'])):
    print(f"    Na partida {j+1}, fez {player['Goals'][j]} gols.")

print(f"Foi um total de {player['Total']} gols.")