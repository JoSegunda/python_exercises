"""Programa que lê dois valores e mostra um menu"""

n = 4

while n!= 5:
    if(n == 1):
        print(f"{a} + {b} = {a+b}")
    elif(n == 2):
        print(f"{a} x {b} = {a*b}")
    elif(n == 3):
        print(f"{a} é maior" if a > b else f"{b} é maior")
    elif(n == 4):
        a = int(input("Insira um valor: "))
        b = int(input("Insira outro valor: "))
    else:
        print("Opção Inválida, tente outra vez.")

    print("-"*20)
    print("""[1] Somar\n[2] Multiplicar\n[3] Maior
[4] Novos números\n[5] Sair do programa""")
    print("-"*20)

    n = int(input("O que deseja fazer? "))
    
print("Fim do programa.")
    