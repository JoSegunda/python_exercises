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

    Pessoas.append(person)
    pessoasCadastradas += 1

    stop = input("Quer continuar? [s / n]: ")

    if stop in "nN":
        break
avgIdade = avgIdade / pessoasCadastradas
idadeAcima = [Pessoas[i]['Nome'] for i in range(len(Pessoas)) if Pessoas[i]['Idade'] > avgIdade ]
print(f"Foram Cadastradas {pessoasCadastradas} pessoas")
print(f"Média de idade: {avgIdade}")
print(f"Mulheres {mulheres}")
print(f"idades acima da média: {idadeAcima}")