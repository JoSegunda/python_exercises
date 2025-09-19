#Um programa que leia algo pelo teclado e mostra o seu tipo primitivo e todas informações sobre ele

var = input("Digite alguma coisa: ")
print(f'Tipo: {type(var)}')
print(f'É alfa númerico: {var.isalnum()}')
print(f'É alfabético: {var.isalpha()}')
print(f'É ASCII: {var.isascii()}')
print(f'É decimal: {var.isdecimal()}')
print(f'É maiúscula: {var.isupper()}')
print(f'É minúscula: {var.islower()}')
print(f'É digito: {var.isdigit()}')
print(f'É número: {var.isnumeric()}')
print(f'É Título: {var.istitle()}')
print(f'É Espaço: {var.isspace()}')