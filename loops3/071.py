"""Programa que simula o funcionamento de um caixa eletrônico
Pergunta qual valor levantar"""

print("=="*20)
print("     BANCO CALLIDIUM")
print("=="*20)

montante = int(input("Montante a levantar: "))
valor = 0
count = 0
ced = 0
while True:
    count = 0
    if(valor+50 <= montante): ced = 50
    elif(valor+20 <= montante): ced = 20
    elif(valor+10 <= montante): ced = 10
    elif(valor+1 <= montante): ced = 1

    while (valor+ced) <= montante:
        valor += ced
        count += 1
    print(f"Total de {count} cédulas de R${ced}")

    if(valor == montante):
        break

print("=="*20)
print(f"Volte Sempre ao BANCO CALLIDIUM! Tenha um bom dia!")