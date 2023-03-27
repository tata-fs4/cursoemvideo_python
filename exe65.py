# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
n=0
list= []
cancel = ""
while cancel != "N":
    print("-="*20)
    n= int(input("Digite um número: "))
    list.append(n)
    cancel = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
sorted(list)
print(f"A média entre os valores deu: {sum(list)/len(list)} .")
print(f"O menor valor lido foi {list[0]} e o maior {list[-1]}.")