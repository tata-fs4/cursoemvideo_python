# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
def maior(* núm):
    print('-='*20)
    for c in range(0, len(núm)):
        print(f'{núm[c]}', end= ' ')
    print(f'Foram informados {len(núm)} valores ao todo.')
    if not núm:
        print(f'O maior valor informado foi 0.')
    else: 
        print(f'O maior valor informado foi {max(núm)}.')
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()