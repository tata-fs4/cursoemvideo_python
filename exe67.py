# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
n = 0
print("--"*20)
while True:
    n= int(input("Quer ver a tabuada de qual valor? "))
    if n < 0:
        break
    print("--"*20)
    for count in range(1, 11):
        print(f"{n} x {count} = {n*count}")
    print("--"*20)    

print("PROGRAMA TABUADA ENCERRADO. Volte sempre!")