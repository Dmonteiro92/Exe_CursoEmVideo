#Escreva um programa que mostre o tamanho em metros, converta em centimetros e melimetros.

print('==== Desafio 08 - Medidas em METRO-CENTIMETORS-MELIMETROS')

metros = float(input('Qual é o valor em metros? '))
cent =  metros*100
meli = metros*1000

print('Você digitou {} metros, vamos converter. \nIsso vale: {} centimetros. \nE vale: {} melimetros.'.format(metros,cent, meli))