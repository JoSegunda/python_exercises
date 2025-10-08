numbersEven = []
numbers = []
numbersOdd = []

while True:
    n = int(input("Digite um número: "))
    numbers.append(n)
    numbersEven.append(n) if n%2==0 else numbersOdd.append(n)
    
    ans = input(("Quer continuar? [S / N]: "))
    if ans in "nN": break
    
print(f"Lista com todos os valores: {numbers}")
print(f"Lista com todos os valores pares: {numbersEven}")
print(f"Lista com todos os valores ímpares: {numbersOdd}")


