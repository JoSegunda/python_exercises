"""Tabuada"""

value = int(input("Insira o valor da tabuada a calcular: "))
stop = int(input("Até que número deseja multiplicar?"))

for i in range(1, stop+1):
    print(f"{value} X {i} = {value * i}")