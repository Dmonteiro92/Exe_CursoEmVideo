#Faça um programa que receba o valor do produto e conceda 5% de desconto.

print('===== Desafio 012 - DESCONTO 5% ======')

produto =  float(input('Qual o valor do produto? '))
produto2 = produto -(produto * 0.05) 

print('O valor do produto é {} reais, com 5% de desconto você paga {} reais.' .format(produto, produto2))