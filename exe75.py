# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9. B) Em que posição foi digitado o primeiro valor 3. C) Quais foram os números pares.
valores = tuple(int(input("Digite um valor: ")) for i in range(1, 5))
print(f"O numero nove aparece {valores.count(9)} vezes") 
if 3 in valores:
    print(f"Valor 3 foi digitado pela primeira vez na {valores.index(3)+1}º posição") 
else:
    print("Não foi digitado valor 3")
print("Valores pares digitados foram", end=" ")
for n in valores:
    if n % 2 ==0:
        print(n, end= " ")