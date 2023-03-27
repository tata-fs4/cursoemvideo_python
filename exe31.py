# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando 0,50 reais por Km para viagens de até 200Km e 0,45 reais para viagens mais longas
dist = float(input("Digite a distância da viagem: "))
if dist <= 200:
    preço= dist*0.50
else:
    preço= dist*0.45
print(f"O preço da viagem de {dist}km, irá custar R${preço:.2f}!")