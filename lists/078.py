newList = [int(input(f"Digite um valor: ")) for c in range(0, 5)]
print(f"Maior: {max(newList)}, Posição {newList.index(max(newList))}")
print(f"Menor: {min(newList)}, Posição {newList.index(min(newList))}")