
newList = []
while True:
    n = int(input("Digite um valor: "))
    if(n not in newList):
        newList.append(n)
    elif n in newList:
        print("Valor duplicado! não vou adicionar")
    
    val = str(input("Quer continuar? [S / N] "))
    if(val in "nN"):
        break
print(f"Valores digitados: {sorted(newList)}")