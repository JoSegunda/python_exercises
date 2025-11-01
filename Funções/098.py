from time import sleep

def contador(start, end, step=1):
    print("=="*20)
    if(start > end):
        if (step > 0):
            step = -step
        end = end - 2
    for i in range(start, end+1,step):
        sleep(0.5)
        print(i, end=" ", flush=True)
    print("FIM")   

contador(1,10,1)
contador(10,0,2)

print("Agora é sua vez de personalizar a contagem:")
start = int(input("Início: "))
end = int(input("Fmm: "))
passo = int(input("Passo: "))
contador(start,end,passo)