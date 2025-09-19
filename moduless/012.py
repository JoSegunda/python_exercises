#Faça um algoritmo que leia o salário de um funcionário e 
#Mostre o seu novo salário com 15% de aumento

salary = float(input("Digite o seu salário: "))
print(f"O seu novo salário é: {salary +(0.15*salary) :.2f}")