"""Programa que mostra os n primeiros termos de uma sequência de fibonacci"""
print("*-"*20)
print("Sequência de Fibonacci")
print("*-"*20)

n = int(input("Quantos termos deseja mostrar? "))
atual = 1
before = 1
count = 0
print("0 -> 1",end=" -> ")
while count != n-2:
    print(f"{atual}", end=" -> ")
    temp = atual
    atual = atual + before
    before = temp   

    count += 1

print("Fim.")