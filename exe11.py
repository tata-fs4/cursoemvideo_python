# Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m²
largura = float(input("Digite a largura da parede: "))
altura = float(input("Digite a altura da parede: "))
area = largura*altura
tinta = area/2
print(f"Uma parede com {altura}m de altura e uma largura de {largura}m, possui {area}m² de área,sendo necessário adquirir {tinta}L de tinta")