matrix = [[],[],[]]

for i in range(3):
    for n in range(3):
        num = int(input(f"Digite um valor para [{i, n}]:"))
        matrix[i].append(num)

print("=="*20)
for linha in matrix:
    for numero in linha:
        print(f"[ {numero} ]", end="")
    print() 