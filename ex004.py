### Faça um programa que leia algo e passe as informações

print('==== Desafio 04 - Informações do input ====')
dados = input('Digite algo aqui: ')

print('Você digitou : {}'.format(dados))
print(type(dados))
print('O que você digitou é um número:', dados.isnumeric())
print('O que você digitou é uma letra:', dados.isalpha())