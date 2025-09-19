"""Programa que leia o nome de preços de vários produtos e pergunta se o usuário
deseja continuar, no final mostre, total gasto, qauntos produto > 1000 nome do produto mais barato"""
from math import inf
print("     LOJA SUPER BARATÃO")
print("=="*20)
sum = 0
nomeBarato = ""
priceCheap = inf
n = 0
while True:
    go = " "
    nome = str(input("Nome do produto: "))
    price = float(input("Preço: R$"))

    sum += price
    if(price > 1000):
        n += 1
    if(price < priceCheap):
        priceCheap = price
        nomeBarato = nome

    while go not in "SsNn":
        go = str(input("Quer continuar? [S / N]"))
    if go in "Nn":
        break
print(f"O total da compra foi R$ {sum}")
print(f"Temos {n} produtos custando mais de R$1000.00")
print(f"O produto mais barato foi a {nomeBarato} que custa R${priceCheap}")