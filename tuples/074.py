from random import randint

listOfNumbers = []
n = 0

while n != 5:

    listOfNumbers.append(randint(0,100)) 
    n += 1

tupleOfNumbers = tuple(listOfNumbers)
print(f"Tupla: {tupleOfNumbers}")
print(f"Maior número: {max(tupleOfNumbers)}")
print(f"Menor número: {min(tupleOfNumbers)}")