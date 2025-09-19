# Faça um programa que leia um número de 0 9999 e mostra na tela
#Cada um dos dígitos separados

num = ['0','0','0','0']
value = str(input("Digite um valor: "))
value.split()
num.extend(value)
new = ' '.join(num).replace(" ",'')
print(f"Unidade: {new[-1]}")
print(f"Dezena: {new[-2]}")
print(f"Centena: {new[-3]}")
print(f"Milhar: {new[-4]}")