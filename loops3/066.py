"""Crie um programa que leia vários números e sópare quando digitar 999"""
sum = count = 0
while True:
    value = int(input("Insira um valor (999 para parar): "))
    if (value == 999):
        break
    sum += value
    count += 1
print(f"Foram digitados {count} números\nA soma foi {sum}")