"""Program que faz uma contagem regressiva de 10 a 0 com um segundo de pausa"""
from time import sleep
for c in range(10,0,-1):
    sleep(1)
    print(c)
print("Booommmmm")