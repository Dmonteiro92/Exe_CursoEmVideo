#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

print('==== Desafio 023 - Unidade - Dezena - Centena - Milhar ====')

numero = input('Digite um número de 1 a 9999: ')
numero = numero.zfill(4)


print(f'A unidade: {numero[3]}')
print(f'A dezena: {numero[2]}')
print(f'A centena: {numero[1]}')
print(f'A milhar: {numero[3]}')