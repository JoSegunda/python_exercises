"""leia o comprimento de 3 retas e diga se podem formar um triângulo"""

a = int(input("Digite o valor da primeira reta: "))
b= int(input("Digite o valor da segunda reta: "))
c = int(input("Digite o valor da terceira reta: "))

if((a+b)>c and (a+c)>b and (b+c)>a):
    print(f"Podem formar um triângulo") 
else:
    print("\033[4;31;40mNão podem formar um triângulo")
