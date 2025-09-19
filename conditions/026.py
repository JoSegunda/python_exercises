# escreva um programa que gere um número aleatório entre 0-5
# e o user tenta adivinhar se acertou ou não

from random import randint

print("="*20)
print("|Vou pensar num número entre 0 e 5. Tente adinvinhar|")
print("="*20)
rand = randint(0, 5)
userGuess = int(input("Em que número estou pensando? "))
print("Você acertou!" if userGuess == rand else f"Você errou, pensei no {rand}")
