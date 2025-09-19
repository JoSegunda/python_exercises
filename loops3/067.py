"""Programa que mostra a tabuada de vários números 1 de cada vez para cada 
valor digitado, o programa é interrompido quando o nº é negativo"""


while True:
    n = 1
    tab = int(input("Quer ver a tabuada de qual valor? "))
    if(tab < 0):
        break
    print("_"*20)
    while n <= 10:
        print(f"{tab} x {n} = {tab * n}") 
        n += 1
    print("_"*20)

print("Fim do programa.")