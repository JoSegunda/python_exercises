numbers = []

while True:
    numbers.append(int(input("DIgite um número: ")))
    answer = input("Quer continuar [S / N]")

    if answer in "nN":
        break