# Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada
tabuada=int(input("Tabuada do numero: "))
print('-'*10)
for count in range(11):
    print(f'{tabuada} x {count} = {tabuada*count}')
    count=+1
print('-'*10)