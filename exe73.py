# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times. b) Os últimos 4 colocados. c) Times em ordem alfabética. d) Em que posição está o time da Chapecoense.
def linha():
    print("="*30)
linha()
times = ("Atlético-MG", "Palmeiras","Fortaleza","Red Bull Bragantino","Flamengo","Corinthians","Athletico","Fluminense",
         "Atlético-GO","Ceará","Cuiabá","Internacional","Juventude","Santos","São Paulo","Bahia",
         "América-MG","Sport","Grêmio","Chapecoense")
linha()
print(f"Lista de times do Brasileirão: {times}")
linha()
print(f"Os 4 primeiros são {times[:5]}")
linha()
print(f"Os 4 últimos são {times[-4:]}")
linha()
print(f"Times em ordem alfabética: {sorted(times)}")
print(f'Posição do time Chapecoense: {times.index("Chapecoense")+1}')