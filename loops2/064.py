"""Programa que lê vários números do teclado e para quando digita-se 999"""

n = 0
sum = 0
count = 0
while n != 999:
    n = int(input("Digite um valor: "))
    if (n != 999):  
        sum += n
        count += 1
print(f"Foram digitados {count} números.")
print(f"A soma total de todos os valores é {sum}")