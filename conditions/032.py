"""Programa que calcula o aumento de um funcionário com base no salário"""

salary = float(input("Digite o seu salário: "))
print(f"Aumento salarial: {(0.10*salary) + salary}" if salary > 1250 else f"Aumento salarial: {(0.15*salary)+salary}")