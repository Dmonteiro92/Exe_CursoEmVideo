#Escreva um programa que pergunte a quantidade de km percorrida pelo carro e a quantidade de dias usados.
#Sabendo que o carro custa 60 reais por dia e 0.15 centavos por KM rodado


print('===== Desafio 015 - Aluguel do carro =====')
dias = int(input('Quantos dias você alugou o carro? '))
km = float(input('Quantos km você rodou com o carro? '))

dias2 = dias*60
km2 =  km * 0.15
total = dias2+km2

print('Você usou o carro por {} dias, percorrendo {} km`s, portanto deve pagar um total de {:.2f} reais'.format(dias,km,total))