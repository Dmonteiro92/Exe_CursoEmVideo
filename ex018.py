#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math 
print('===== DESAFIO 018 - SENO, COSSENO E TANGENTE =====')
angulo = float(input('Digite o ângulo que vamos trabalhar: '))

radiano = math.radians(angulo)
seno = math.sin(radiano)
consseno = math.cos(radiano)
tangente = math.tan(radiano)

print(f'Seu angulo é de {angulo} com isso temos:')
print(f'Um radiano no valor de {radiano}')
print(f'Um seno de: {seno}')
print(f'Um consseno de: {consseno}')
print(f'Uma tangente de: {tangente}')