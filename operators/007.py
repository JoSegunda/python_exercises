#Program que lê um valor em metros e converte em cm e ml

num = int(input("digite o valor em metros: "))
print(f"{num/1000}km")
print(f"{num/100}hm")
print(f"{num/10}dam")
print(f"{num*10}dm")
print(f"{num *100}cm")
print(f"{num *1000} mm")