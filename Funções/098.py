def contador(start, end, step):
    if(start > end):
        step = -step
        end -= 2
    for i in range(start, end+1,step):
        print(i)

contador(10,0,2)