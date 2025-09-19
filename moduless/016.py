#Faça um comprimeto de um cateto oposto e de um triangulo retângulo
#Calcule e mostre o comprimento da hipotenusa
from math import pow, sqrt
catetoOp = float(input("Digite o tamanho do cateto oposto: "))
catetoAd = float(input("Digite o tamanho do cateto adjacente: "))

comprimento = sqrt(pow(catetoOp,2) + pow(catetoAd, 2))

print(f"O hipotenusa é {comprimento :.2f}")