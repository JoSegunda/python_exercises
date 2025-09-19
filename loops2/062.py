"""Prgrama que calcula uma PA pede o número de termos a mostrar"""

termo1 = int(input("Digite o primeiro termo: "))
step = int(input("Insira a razão: "))
stop = 10
n = 0
while n != stop:
    print(f"{termo1}", end=" -> ")
    termo1 += step
    n += 1
    if (n == stop):
        print("PAUSA")
        stop = int(input("\nQuantos mais termos deseja mostrar? "))
        n = 0

print("\nFim do programa.")