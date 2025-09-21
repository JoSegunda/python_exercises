
times = (
    "Flamengo","Palmeiras","Cruzeiro","Botafogo","Mirasol","Bahia","São Paulo",
    "Fluminense","Red Bull bragantino","Corithians","Ceará","Internacional","Atlético-MG","Grêmio",
    "Vasco da gama","Santos","Vitória","Juventude","Fortaleza","Sport"
)
timesEmOrdem = list(times)

print("Primeiros 5 colocados: ",(times[0:5]))
print("Últimos 4 colocados: ", times[16:20])
print("Times em ordem: \n", sorted(timesEmOrdem))
print("O Botafogo está na posição: ", times.index("Botafogo"))