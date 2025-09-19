#Faça um programa que leai a altura e largura de uma parede
#e calcule  a sua área e a quantidade de tinta necessária para pintá-la
#Sabendo que cada litro de tinta pinta uma área de 2m²

largura = float(input("Digite a largura: "))
altura = float(input("Digite a altura: "))

area = altura * largura

print(f"Área: {area}m²")
print(f"Será necessário {'%.2f' % (area/2)}L para pintar esta área.")

