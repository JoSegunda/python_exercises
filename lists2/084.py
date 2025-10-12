from math import inf
pessoas = []
maxPesoList = []
minPesoList = []
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
for i in range(len(pessoas)):
    if pessoas[i][1] == maxPeso:
        maxPesoList.append(pessoas[i][0])
    elif pessoas[i][1] == minPeso:
        minPesoList.append(pessoas[i][0])

print(f"Ao todo foram cadastrados {countPeope} pessoas. ")
print(f"O maior peso foi de {maxPeso}. Peso de {maxPesoList}")
print(f"O menor peso foi de {minPeso}. Peso de {minPesoList}")
