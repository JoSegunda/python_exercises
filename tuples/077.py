palavras = (
    "casa", "mesa", "livro", "porta", "janela",
    "carro", "rua", "bola", "tempo", "pessoa",
    "animal", "planta", "rio", "cidade", "escola",
    "computador", "telefone", "chave", "papel", "amigo"
)

for word in palavras:
    print(f" Na palavra {word} temos: ",end="")

    for n in word:
        if(n in "aeiou"):
            print(n, end=" ")
    
    print("\n")