def contador(start, end, step):
    if(start > end):
        step = -step
    for i in range(start, end,step):
        print(i)

contador(1,10,1)