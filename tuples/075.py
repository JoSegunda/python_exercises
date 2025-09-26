
listOfNumbers = []
evenNumbers = []
n = 0
while n != 4:
    temp = int(input("Digite um valor: "))
    listOfNumbers.append(temp)
    if(temp%2==0):
        evenNumbers.append(temp)
    n += 1

tupleOfNumbers = tuple(listOfNumbers)
print(f"O valor 9 ocorreu {tupleOfNumbers.count(9)} vezes")
try:
    print(f"O primeiro valor 3 aparece na {tupleOfNumbers.index(3)}ª posição.")
except:
    print("Valor não 3 está presente.")

print(f"Números pares: {evenNumbers}")
