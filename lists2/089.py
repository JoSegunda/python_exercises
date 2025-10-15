
students = []
studentTemp = []
notasTemp = []
answer = 's'
c = 0
while answer in "sS":
    nome = input("Nome: ")
    studentTemp.append(nome)
    for i in range(2):
        notasTemp.append(float(input(f"Nota {i+1}: ")))

    studentTemp.append(notasTemp[:])
    students.append(studentTemp[:])
    
    studentTemp.clear()
    notasTemp.clear()
    answer = input("Quer continuar [S / N]? ")
    
    c+=1
print("=="*20)
print("Nº   Nome    Média")
print("-" * 20)
for i, student in enumerate(students):
    nome = student[0]
    avg = (student[1][0] + student[1][1]) / 2
    print(f"{i+1:<5}{nome:<10}{avg:>5.1f}")
print("-" * 20)

while True:
    show = int(input("Mostrar notas de qual aluno? (999 interrompe): "))

    if (show == 999):
        break
    print("Notas de ",students[show-1][0],"são", students[show-1][1])

print("Saindo.....")
print("Obrigado..........")