values = []
added = True
for i in range(5):
    n = int(input("Digite um valor: "))
    if i == 0 or n > values[-1]:
        values.append(n)
        print(f"Adicionado no final da lista")
    else:
        for c in range(len(values)):
            if n < values[c]:
                values.insert(values.index(values[c]), n)
                print(f"Adicionado na posição {values.index(n)} da lista...")
                break
        
print(f"Valores digitados em ordem: {values}")