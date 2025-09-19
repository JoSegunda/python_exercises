# Escreva um programa para aprovar um empréstimo bancário para uma casa

housePrice = float(input("Digite o valor da casa: "))
salary = float(input("Digite o seu salário: "))
months = int(input("Digite o número de meses para fazer o pagamento: "))

monthlyPayment = housePrice / months
# 0.3 because it cnnot exceed 30% of the salary
rejectionValue = 0.3 * salary

print(f"Valor da prestação: Kz{monthlyPayment :.2f}" if monthlyPayment <= rejectionValue else f"\033[0;31;40mEmpréstimo Recusado, prestação: R${monthlyPayment :.2f}" )