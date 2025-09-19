"""leia 3 lados de um triângulo e diga que tipo de triângulo é"""

a = int (input("Valor do primeiro lado: "))
b = int (input("Valor do segundo lado: "))
c = int (input("Valor do terceiro lado: "))

if (a + b > c and b + c > a and c + a > b):
    print("Podemos formar um triângulo")

    if((a==b and a!=c) or (b==c and b!=a) or (a==c and a != b)):
        print("O triângulo é isósceles")
    elif(a!=b and a!=c and b!=c):
        print("O triângulo é escaleno")
    elif(a==b==c):
        print("O triângulo é equilátero.")
else:
    print("Não pode formar um triângulo")