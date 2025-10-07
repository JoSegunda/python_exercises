numbers = []
numbersCount = 0
while True:
    numbers.append(int(input("DIgite um número: ")))
    answer = input("Quer continuar [S / N]")

    if answer in "nN":
        break
    
    numbersCount += 1

print(f"Foram digitados {numbersCount} números.")
print(f"Valores em ordem decrescente: {numbers.reverse()}")
print("O valor 5 ","está na lista" if 5 in numbers else "não está na lista")