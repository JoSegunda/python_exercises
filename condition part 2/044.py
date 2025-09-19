"""Programa que calcula o valor a considerando o seu preço e tipo de pagamento"""

price = float(input("Preço do produto: "))

print("+-"*20)
print("""Escolha o tipo de pagamento:
      [1] pagamento à vista.
      [2] pagamento à vista por cartão.
      [3] Pagamento parcelado 2X no cartão.
      [4] Pagamento parcelado 3X no cartão""")
print("+-"*20)

metodoDePagamento = int(input("Digite a opção pretendida: "))

if(metodoDePagamento == 1): print(f"Valor a pagar: {price - (0.1*price)}, 10% de desconto.")
elif(metodoDePagamento == 2): print(f"Valor a pagar: {price - (0.05*price)}, 5% de desconto")
elif(metodoDePagamento == 3): print(f"Mensalidade: {(price - (0.1*price)) / 2}")
elif(metodoDePagamento == 4): 
      parcelas = int(input("QUantas parcelas vão ser? "))
      print(f"Prestação: {(price + (0.2*price))/parcelas}")
