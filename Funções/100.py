from random import randint
from time import sleep
def sorteia():
    nums = list()
    print("Sorteando os valores: ")
    for i in range(5):
        n = randint(1, 10)
        print(n, end=" ", flush=True)
        nums.append(n)
    return nums
    
def SomaPar(soma):
    print(f"Somando os valores pares {soma}, temos {sum(soma)}")




numbers = sorteia()

print(numbers)