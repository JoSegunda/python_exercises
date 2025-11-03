from random import randint
from time import sleep
def sorteia():
    nums = list()
    print("Sorteando os valores: ", end=" ")
    for i in range(5):
        n = randint(1, 10)
        sleep(0.5)
        print(n, end=" ", flush=True)
        nums.append(n)
        print()
    return nums
    
def SomaPar(soma):
    add = 0
    for valor in soma:
        if valor %2==0:
            add += valor
    print(f"Somando os valores pares {soma}, temos {add}")




numbers = sorteia()
SomaPar(numbers)