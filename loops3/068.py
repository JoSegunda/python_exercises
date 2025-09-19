"""Programa que jogue par ou ímpar com o computador"""
from random import randint
print("Vamos jogar para ou ímpar")
print("=="*20)
result = ""
won = True
wins = 0
while True:
    value = int(input("Diga um valor: "))
    choice = str(input("Par ou ímpar? [P/I]: "))
    pcChoice = randint(1, 10)
    sum = value + pcChoice
    result = "Ímpar" if sum%2!=0 else "PAR"
    if((sum%2==0 and choice in "iI") or (sum%2!=0 and choice in "pP")):
        won = False
    elif((sum%2!=0 and choice in "Ii") or (sum%2==0 and choice in "pP")):
        won = True
    print("--"*20)
    print(f"Você jogou {value} e o computador {pcChoice}. Total de {sum} DEU {result}")
    
    if won:
        print("--"*20)
        wins += 1
        print("Você Venceu!\nVamos jogar novamente...\n","=="*20)
    else:
        print("--"*20,"\nVocê PERDEU!\n","=="*20)
        break
    
print(f"GAME OVER! você venceu {wins} vezes")