"""Um programa que recebe um inteiro e pede para o usuário escolher a base de conversão"""

numberToConvert = int(input("Digite o número a se converter: "))
print("+_"*20)
print("Escolha a conversão desejada\n[1] Para binário\n[2]Para octal\n[3]Para hexadecimal")
print("+_"*20)

base = int(input("Digite o valor: "))

if(base == 1):
    print(f"Valor em binário: {bin(numberToConvert)}")
elif(base == 2):
    print(f"Valor na base octal: {oct(numberToConvert)}")
else:
    print(f"Valor em hexadecimal: {hex(numberToConvert)}")