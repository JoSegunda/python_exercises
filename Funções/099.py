from time import sleep

def maior(*numbers):
    print("=="*20)
    print("Analisando valores processados...")
    n = 0
    for number in numbers:
        sleep(1)
        print(number, end=" ", flush=True)
        if number > n:
            n = number
    print(f"Foram informados {len(numbers)} valores")
    print(f"Maior valor: {n}" if n > 0 else "O maior valor não existe")
    

maior(2,9,4,5,7,1)
maior(4, 7,0)
maior(1,2)
maior(6)
maior(0)