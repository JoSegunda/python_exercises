Pessoas = list()
person = dict()
pessoasCadastradas = 0
avgIdade = 0
mulheres = list()
stop = ""
while True:
    nome = input("Nome: ")
    sexo = " "
    while(sexo not in "fFmM"):
        sexo = input("Sexo: ")
    if sexo in "fF":
        mulheres.append(nome)
    
    idade = int(input("Idade: "))
    avgIdade += idade

    person['Nome'] = nome
    person['Sexo'] = sexo
    person['Idade'] = idade

    Pessoas.append(person.copy())
    pessoasCadastradas += 1

    stop = input("Quer continuar? [s / n]: ")

    if stop in "nN":
        break
avgIdade = avgIdade / pessoasCadastradas
print("=="*20)
print(f"Foram Cadastradas {pessoasCadastradas} pessoas")
print(f"Média de idade: {avgIdade}")
print(f"Mulheres {mulheres}")
print(f"Pessoas com idade acima da média:")

for pessoa in Pessoas:
    if (pessoa['Idade'] > avgIdade):
        print(pessoa)