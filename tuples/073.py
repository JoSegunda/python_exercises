
times = (
    "Flamengo","Palmeiras","Cruzeiro","Botafogo","Mirasol","Bahia","São Paulo",
    "Fluminense","Red Bull bragantino","Corithians","Ceará","Internacional","Atlético-MG","Grêmio",
    "Vasco da gama","Santos","Vitória","Juventude","Fortaleza","Sport"
)
timesEmOrdem = list(times)
print(f"Lista de times {times}")
print("=-"*20)
print("Primeiros 5 colocados: ",(times[0:5]))
print("=-"*20)
print("Últimos 4 colocados: ", times[-4:])
print("=-"*20)
print("Times em ordem: \n", sorted(timesEmOrdem))
print("=-"*20)
print(f"O Botafogo está {times.index("Botafogo")}ª posição: ")