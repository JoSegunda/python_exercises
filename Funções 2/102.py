def fatorial(num, show=False):
    result = 1

    for i in range(num,-1):
        result *= i
        if(show):
            print(i," x ")
    
    if(not(show)):
       return result



fatorial(5, False)