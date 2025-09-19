"""Programa que pergunta a distância de uma viagem em km calcule o preço da passagem,
cobrando 0.50 por km para viagens até 200km e 0,45 para viagens mais longas"""

distance = int(input("Digite a distância da viagem: "))
print(f"Passagem: {0.50*distance}" if distance <= 200 else f"Passagem: {0.45*distance}")