from math import inf
pessoas = []
temp = []
countPeope = 0
maxPeso = 0
minPeso = inf
while True:
    temp.append(input("Nome: "))
    temp.append(float(input("Peso: ")))

    stop = input("Quer continuar? [S / N] ")

    if(temp[1] > maxPeso):
        maxPeso = temp[1]
    elif(minPeso > temp[1]):
        minPeso = temp[1]
    
    countPeope += 1
    pessoas.append(temp[:])
    temp.clear()
    if stop in "nN":
        break
print(f"O maior peso foi de {maxPeso}. Peso de ")
# for i in range(len(pessoas)):
#     if(pessoas[i][1] == maxPeso):
#         temp.append(pessoas[i][1])

print(f"Ao todo foram cadastrados {countPeope} pessoas. ")
print(max(pessoas))
