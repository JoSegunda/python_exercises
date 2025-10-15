from random import sample
from time import sleep
palpite = int(input("Quantos jogos serão jogados? "))
storeValues = []
tempList = []
print("=-"*4,f"Sorteando {palpite} jogos", "=-"*4)

for i in range(palpite):
    print(f"Jogo {i+1}: ", end=" ")
    storeValues.append(sorted(sample(range(1, 61), 6)))
    print(storeValues[i])
    sleep(1)
print("-="*5,"< BOA SORTE > ","-="*5)
