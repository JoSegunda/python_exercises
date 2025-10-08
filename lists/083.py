openParenthesis = 0
closeParenthesis = 0

exp = input("Digite a sua expressão: ")

for i in exp:
    if i == "(":
        openParenthesis += 1
    elif i == ")":
        closeParenthesis += 1

print(f"A sua expressão ","é válida!" if openParenthesis == closeParenthesis else "não é válida")