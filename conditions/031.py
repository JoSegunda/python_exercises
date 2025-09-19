"""Program que lê 3 números e mostre qual é o maior e qual o menor"""
a = int(input("Digite primeiro valor: "))
b = int(input("Digite o segundo valor: "))
c = int(input("Digite o terceiro valor: "))

maior = 0
menor = 0

if (a > b and a > c):
    maior = a
    menor = c if b > c else b
elif(b > a and b > c):
    maior = b
    menor = c if a > c else a
elif (c > b and c > a):
    maior = c
    menor = a if b > a else b

print(f"Maior:{maior}\nmenor: {menor}")