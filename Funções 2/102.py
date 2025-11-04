from time import sleep

def fatorial(num, show=False):
    result = 1

    for i in range(num,-1):
        result *= i
        if(show):
            sleep(0.5)
            print(i," x ", end="", flush=True)
    
    if(not(show)):
       return result



fatorial(5, False)