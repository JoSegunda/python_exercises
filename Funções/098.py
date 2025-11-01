from time import sleep

def contador(start, end, step):
    if(start > end):
        step = -step
        end -= 2
    print("=="*20)
    for i in range(start, end+1,step):
        print(i, end=" ")
        sleep(1)
    print("=="*20)
    print("FIM")

contador(1,10,1)
contador(10,0,2)

print("Agora é sua vez de personalizar a contagem:")
start = int(input("Início"))
end = int(input("Fmm:"))
passo = int(input("Passo:"))
contador(start,end,passo)