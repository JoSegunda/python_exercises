from random import choices, randint
from math import inf
def sorteia():
    nums = list()
    print("Sorteando os valores: ")
    for i in range(5):
        nums.append(randint(1, 10))
    return nums
    




numbers = sorteia()

print(numbers)