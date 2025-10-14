numbers = [[],[]]

for i in range(7):
    n = int(input("Digite um número: "))

    if n%2==0:
        numbers[0].append(n)
    else:
        numbers[1].append(n)

print("=="*20)
print(f"Valores Pares: {sorted(numbers[0])}")
print(f"Valores Ímpares: {sorted(numbers[1])}")