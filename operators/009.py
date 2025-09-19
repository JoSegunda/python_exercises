#program que lê quanto dinheiro alguém tem na 
# carteira e mostra quantos dolares ela pode comprar

money = float(input("Quanto dinheiro você tem na carteira? "))

print(f"Voçê pode comprar {'%.2f' % (money/3.27) } US$")