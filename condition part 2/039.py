"""Programa que lê a idade de um jovem e informe se pode se alistar no exército"""
import datetime
year = int(input("Digite o seu ano de nascimento: "))
currentYear = datetime.datetime.now().year
age =  currentYear - year

if(age < 18): print(f"Ainda vai se alistar, faltam {18 - age} anos.")
elif(age == 18): print("É hora de se alistar.")
else: print(f"Já passou da idade de se alistar,passou {age - 18} anos desde o alistamento obrigatório.")