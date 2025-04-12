#Crie um programa que receba o valor em real e converta para dolar.

print('===== Desafio 010 - CONVERTER DOLAR =====')
real = (float(input('Quanto você quer converter hoje? ')))
dolar  = real / 5.87 

print('Nos dia de hoje seus {:.2f} reais convertidos seriam {:.2f} dolares '.format(real,dolar))