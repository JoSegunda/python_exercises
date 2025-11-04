from datetime import datetime


def voto(data):
    ano = datetime.now().year - data
    print(ano,"anos:",end=" ")
    
    if(ano > 18 and ano < 65): return ("Voto obrigatório")
    elif(ano > 65): return ("Voto opcional")
    else: return ("Não vota")


ano = int(input("Ano de nascimento: "))
print(voto(ano))