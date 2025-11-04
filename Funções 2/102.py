from time import sleep

def fatorial(num, show=False):
    result = 1
    print("=="*20)
    for i in range(num,0,-1):
        result *= i
        if(show and i != 1):
            sleep(0.5)
            print(i,"x ", end="", flush=True)
        elif(i == 1 and show):
            print(i, " = ", end=" ")
    
    return result


print(fatorial(5, False))