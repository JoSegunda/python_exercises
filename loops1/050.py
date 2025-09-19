"""Programa que lê 6 números inteiros e mostra a soma dos pares """

sum = 0
for i in range(0,6):
    value = int(input("Digite um número: "))
    if(value%2==0):
        sum += value
print(f"Resultado final da soma {sum}")