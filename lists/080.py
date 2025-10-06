values = []
added = True
for i in range(5):
    n = int(input("Digite um valor: "))
    if i == 0:
        values.append(n)
    
    for c in range(len(values)):
    
        if n < values[c] and n < values[c]+1:
            values.insert(values.index(values[c]), n)
            break
    
    if n > values[-1]:
        values.append(n)
    print(f"Adicionado na posição {values.index(n)} da lista...")
        

print(values)