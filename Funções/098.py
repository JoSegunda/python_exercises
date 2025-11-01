from time import sleep

def contador(start, end, step):
    print("=="*20)
    if(start > end) or (step < 0):
        step = -step
        end -= 2
    
    for i in range(start, end+1,step):
        sleep(0.5)
        print(i, end=" ", flush=True)
    print("FIM")
    print("=="*20)
    

contador(1,10,1)
contador(10,0,2)

print("Agora é sua vez de personalizar a contagem:")
start = int(input("Início: "))
end = int(input("Fmm: "))
passo = int(input("Passo: "))
contador(start,end,passo)