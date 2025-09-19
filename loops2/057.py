"""Programa que lê o sexo mas só aceita M of F"""

gender = " "

while gender not in "FfmM":
    gender = str(input("Digite o seu sexo: ")).lower()
print(f"Sexo feminino registrado com sucesso" if gender in "fF" else "Sexo Masculino registrado com sucesso")