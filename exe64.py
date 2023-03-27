# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
n=0
list= []
while n != 999:
    print("-="*20)
    n= int(input("Digite um número: [999] para parar: "))
    list.append(n)
list.pop()
print(f"Foram digitados {len(list)} números. A soma entre eles deu {sum(list)}.")