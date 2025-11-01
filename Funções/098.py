from time import sleep

def contador(start, end, step):
    if(start > end):
        step = -step
        end -= 2
    print("=="*20)
    for i in range(start, end+1,step):
        print(i, sep=" ")
        sleep(1)
    print("FIM")

contador(10,0,2)
contador(10,0,2)