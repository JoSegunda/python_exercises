def maior(*numbers):
    print("=="*20)
    print("Analisando valores processados...")
    n = 0
    for number in numbers:
        print(number, end=" ", flush=True)
        if number > n:
            n = number
    print(f"Foram informados {len(numbers)} valores")
    print(f"Maior valor: {n}")
    

maior(2,9,4,5,7,1)
maior(4, 7,0)
maior(1,2)
maior(6)