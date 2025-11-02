def maior(*numbers):
    n = 0
    for number in numbers:
        if number > n:
            n = number
    print(f"Maior número: ")
    
