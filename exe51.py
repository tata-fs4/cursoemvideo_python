# Desenvolva um programa que leia o primeiro termo e a razão de um Progressão Aritmética. No final, mostre os 10 primeiros termos dessa progressão.
#Entrada
termo = int(input("Digite o termo: "))
razao = int(input("Razão: "))
dez = termo + (10 - 1) * razao
#condição
print("="*20)
print("(",end="")
for c in range(termo, dez + razao, razao):#Está multiplicado a razão pra da um PA de 10 primeiros
    print(f"{c}", end="-> ")
print("FIM)",end="")