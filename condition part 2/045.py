"""Faça Jokenpô com o computador"""
from time import sleep
from random import randint
print("+_"*20)
print("Jogo Pedra papel e tesoura\n Siga as instruções para jogar")
print("+_"*20)
print("""Siga os seguintes passos:
      Pressione [1] para jogar pedra
      Pressione [2] para jogar papel
      pressione [3] para jogar tesoura""")
print("+_"*20)
print("Sua vez:")

user = int(input("É a sua vez: "))
pc = randint(1,3)

if (pc == 1): print("O computador jogou Pedra")
elif (pc == 2): print("O computador jogou Papel")
if (pc == 3): print("O computador jogou Tesoura")

print("Jo")
sleep(1)
print("Ken")
sleep(1)
print("Po")

if((pc == 1 and user == 1) or (pc == 2 and user == 2) or (pc == 3 and user ==3)): print("É um Empate!")
elif((pc == 3 and user == 1) or (pc == 2 and user == 3) or (pc == 1 and user == 2)): print("Você venceu")
elif((pc == 1 and user == 3) or (pc == 3 and user == 2) or (pc == 2 and user == 1)): print("Você Perdeu!")