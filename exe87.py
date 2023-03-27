# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados. B) A soma dos valores da terceira coluna. C) O maior valor da segunda linha.
matriz = [[],[],[]]
par = 0
terccoluna = 0
maiorsegunda = 0
for i in range(0,3):
    for c in range(0,3):
        matriz[i].append(int(input(f'Digite um valor para [{i},{c}]: ')))
print(matriz)
print('-='*30)
for i in range (0,3):
    for c in range (0,3):
        print(f'[{matriz[i][c]:^5}]', end='')
        if matriz[i][c] % 2 ==0:
            par += matriz[i][c] 
        if c == 2:
            terccoluna += matriz[i][c]
        if i == 1 and maiorsegunda == 0:
            maiorsegunda = matriz[i][c]
        if i == 1 and matriz [i][c] > maiorsegunda:
            maiorsegunda = matriz [i][c]
    print()

print('-='*20)
print(f'A soma dos valores pares é {par}.')
print(f'A soma dos valores da terceira  coluna é {terccoluna}.')
print(f'O maior valor da segunda linha é {maiorsegunda}.')