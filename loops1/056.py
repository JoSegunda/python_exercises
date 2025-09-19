"""Programa que lê nome, idade e sexo de 4 pessoas e mostre
a média de idade do grupo """
avg = 0
oldest = 0
oldestname = ""
womenCOunt = 0
for i in range(0, 4):
    nome = str(input("Qual o seu nome? "))
    idade = int(input("Digite a sua idade: "))
    sexo = str(input("Qual o seu sexo[M/F]? ")).lower()
    print("\n")
    avg += idade
    if(idade > oldest and sexo == "m"):
        oldest = idade
        oldestname = nome
    if(idade < 20 and sexo == "f"):
        womenCOunt += 1
print(f"Média de idade do grupo: {avg / 4}")
print(f"O {oldestname} é o homem mais velho do grupo")
print(f"{womenCOunt} mulher com menos de 20 anos" if womenCOunt<=1 else f"{womenCOunt} mulheres com menos de 20 anos")