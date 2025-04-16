#Crie um programa que leia um número real e mostre sua parte inteira. Dica: import math

import math
print('===== Desafio 016 - PARTE INTEIRA =====')
numero=float(input('Digite um número real qualquer: '))
print('Legal o número que você digitou foi {}, a parte inteira dele é {}.'.format(numero, math.floor(numero)))