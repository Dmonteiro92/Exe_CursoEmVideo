#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retânuglo
#Calcule e mostre o comprimento da hipotenusa

import math
print('===== Desafio 017 - CALCULANDO O TRIÂNGULO =====')
print('Vamos calcular a hipotenusa')

cate_oposto = float(input('Digite o valor do cateto oposto: '))
cate_adjacente = float(input('Digite o valor do cateto adjacente: '))

hipotenusa = math.sqrt(cate_oposto**2 + cate_adjacente**2)

hipotenusa2 = math.hypot(cate_oposto,cate_adjacente)

print('Sabendo que seu cateto oposto é {} e seu cateto adjacente é {} seu triângulo possuí a seguinte hipotenusa: {}'.format(cate_oposto, cate_adjacente, hipotenusa))
print('O mesmo resultado, porém com outro método {}'.format(hipotenusa2))