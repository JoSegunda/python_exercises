"""Programa que leia idade e sexo de várias pessoas
A cada pessoa devemos perguntar se desja continuar ou não
No fina mostre quantos têm > 18, quantos homens foram inseridos e quantas mulheres com <20"""

maiorDeIdade = 0
numeroHomens = 0
mulher = 0
idade = 0
while True:
    result = " "
    sexo = "7"
    print("--"*20)
    print("     CADASTRE UMA PESSOA")
    print("--"*20)

    
    idade = int(input("Idade: "))
    while not(sexo.isalpha()):
        sexo = str(input("Sexo [M / F]: "))

    if(idade > 18):
        maiorDeIdade += 1
    if(sexo in "Mm"):
        numeroHomens += 1
    if(sexo in "Ff" and idade < 20):
        mulher += 1
    while result not in "SsnN":
        result = str(input("Quer continuar? [S / N]"))
    if result in "Nn": break

print(f"Total de pessoas com mais de 18 anos: {maiorDeIdade}")
print(f"Ao todo temos {numeroHomens} homens cadastrados.")
print(f"E temos {mulher}"," mulheres" if mulher > 1 else "mulher"," Com menos de 20 anos.")