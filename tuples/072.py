numberText = (
    'zero','one','two','three','four','five',
    'six','seven','eight','nine','ten','eleven',
    'twelve','thirteen','fourteen','fifteen','sixteen','seventeen',
    'eighteen','nineteen','twenty'
)
while True:
    number = int(input("Insira um valor de (0 - 20): "))
    if(number <= 20 and number >= 0):
        break
    print("Tente novamente")
print(f"O número digitado é: {numberText[number]}")