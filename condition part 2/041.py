"""Leia o ano de atleta e diga a sua classificação"""
from datetime import datetime

ano = int(input("Digite o seu ano de nascimento: "))
idade = datetime.now().year - ano

print(f"O atleta tem {idade} anos")
if(idade <= 9): print("Mirim")
elif(idade <= 14): print("Infantil")
elif(idade <= 19): print("Junior")
elif(idade <= 25): print("Sênior")
else: print("Master")