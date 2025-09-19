"""Program que calcula a soma dos números ímpares que são múltiplos de 3 no intervalo de 1 a 500"""
count = 0
values = 0
for i in range(3,501,3):
    if(i%2!=0):
        count += i
        values += 1

print(f"A soma dos {values} valores é {count}")