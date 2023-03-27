# Escreva um programa que leia a velocidade de um carro.
# - Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
# - A multa vai custar 7 reais por cada km acima do limite.
vel = int(input("Digite a velocidade atual do carro: "))
if vel>80:
    print(f"Você foi multado por estar a {vel}km/h. Velocidade máxima da via: 80km/h!")
    print(f"O valor da multa será de R${(vel-80)*7}!")
print("Tenha um bom dia! Dirija com segurança!")