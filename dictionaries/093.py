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

show = int(input("Mostrar dados de qual jogador? "))
while show != 999:
    
    if(show > len(player)):
        print("Tente Novamente")
    else:
        name = list(player.keys())[0]
        print(f"--Levantamento do jogador {player[name]}")
        for i in range(player[name]):
            print(f" No jogo {i+1} fez {player[name][i]} gols.")
    
    show = int(input("Mostrar dados de qual jogador? "))

print("<<   VOLTE SEMPRE     >>")