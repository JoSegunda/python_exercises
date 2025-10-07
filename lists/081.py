numbers = []
numbersCount = 0
while True:
    numbers.append(int(input("Digite um número: ")))
    answer = input("Quer continuar [S / N]: ")
    numbersCount += 1

    if answer in "nN":
        break

numbers.sort()
numbers.reverse()
print(f"Foram digitados {numbersCount} números.")
print(f"Valores em ordem decrescente: {numbers}")
print("O valor 5 ","está na lista" if 5 in numbers else "não está na lista")