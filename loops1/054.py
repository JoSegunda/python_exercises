""" Programa que lê o ano de nascimento de 7 pessoas
e mostre quantas ainda não atingiram a maior idade"""
from datetime import datetime
idade = 0
maiorIdade = 0
menorIdade = 0
for i in range(1,8):
    ano = int(input("Digite o seu ano de nascimento: "))
    idade = datetime.now().year - ano
    if(idade > 18):
        maiorIdade += 1
    else:
        menorIdade += 1
print(f"""Destas 7 pessoas, {maiorIdade} atingiram a maior idade,
e {menorIdade} ainda não atingiram a maior idade. """)