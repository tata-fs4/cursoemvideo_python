# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros
dist = float(input("Digite a distância: "))
cm = dist*100
mm = dist*1000
print(f"A medida de {dist}m corresponde a {cm:.0f}cm e {mm:.0f} mm")