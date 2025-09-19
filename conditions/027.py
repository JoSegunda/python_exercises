"""Escreva um program que leia a velocidade de um carro se > 80km diz que
ele foi multado 7R$ porcada km acima"""

km = float(input("Digite a velocidade do seu carro: "))

print(f"Limite de velocidade excedido, multa de R$ {(km-80)*7}" if km >80 else "Você está salvo")