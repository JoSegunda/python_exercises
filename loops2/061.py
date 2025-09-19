"""Prgrama que calcula uma PA"""
termo1 = int(input("Digite o primeiro termo: "))
step = int(input("Insira a razão: "))
n = 0
while n != 10:
    print(f"{termo1} -> " if n != 9 else f"{termo1}",end=" -> ")
    termo1 += step
    n += 1
print("Fim.")