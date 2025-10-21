import datetime
Person = dict()
x = datetime.datetime.now()

Person['Nome'] = input("Nome: ")
anoNascimento = int(input("Ano de nascimento: "))
Person['Idade'] = x.year - anoNascimento
Person['ctps'] = int(input("carteira de trabalho (0 não tem): "))

if(Person['ctps'] != 0):
    Person['Contratação'] = int(input("Ano de contratação: "))
    Person['salário'] = float(input("salário kz: "))
    aposentar = (Person['Contratação'] - anoNascimento) + (x.year - Person['Contratação'])
    Person['Aposentadoria'] = (Person['Contratação'] - anoNascimento) + 35

print("=="*20)
for k, v in Person.items():
    print(f"{k}: {v}")
