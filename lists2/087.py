matrix = [[],[],[]]
maxv = 0
evenSum = 0
row3sum = 0
for i in range(3):
    for n in range(3):
        num = int(input(f"Digite um valor para [{i}, {n}]:"))
        matrix[i].append(num)
        if num%2==0:
            evenSum += num
        if n == 2:
            row3sum += num

print("=="*20)
for i in range(3):
    for n in range(3):
        print(f"[ {matrix[i][n]} ]", end="")
        # Encontrar maior valor da segunda linha
        if i == 1:
            if matrix[i][n] > maxv:
                maxv = matrix[i][n]
        
    print() 

print(f"=-"*20)
print(f"A soma dos valores pares é {evenSum}.")
print(f"A soma dos valores da terceira coluna é {row3sum}.")
print(f"O maior valor da segunda linha é {maxv}.")