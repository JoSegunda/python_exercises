#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto

price = float(input("digite o preço: "))
print(f"Produto com desconto: {price - (0.05*price) :.2f}")