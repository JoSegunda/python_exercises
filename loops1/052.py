"""Programa que lê um número inteiro e diz se é primo ou não"""

num = int(input("Digite um número: "))
isPrime = True

for i in range(1, num+1):
    if(num%i==0):   print(f"\033[92m {i}", end=" ")
    else: print(f"\033[91m{i}", end=" ")
    
    if(num%i==0 and (i != 1 and i != num)):
        isPrime = False
print("\033[0m")
print("\nO número é primo" if isPrime else "\nO número não é primo")