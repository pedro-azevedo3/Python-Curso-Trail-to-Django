"""
Faça um programa que peça ao usuário para digitar um número inteiro, informe se este número é
par ou ímpar. Caso o usuário não digite um número inteiro, informe que não é um número inteiro.
"""

numero = float(input('Digite um número inteiro: '))

try: 
    if (numero%2) == 0:
        print("Este número é par")
    elif (numero%2) == 1:
        print("Este número é impar")
    else:
        print("Nem inteiro o número é.")
except:
    print('O número não é inteiro.')
