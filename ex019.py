#Faça um programa que leia 4 nomes  e escolha um aleatório. 



import random
print(10* '=' + ' Desafio do nome aleatorio ' + 10 * '=')
print('Digite quatro nomes e iremos sortear 1')
nome1 = input('Digite o primeiro nome: ')
nome2 = input('Digite o segundo nome: ')
nome3 = input('Digite o terceiro nome: ')
nome4 = input('Digite o quarto nome: ' )
lista = [nome1, nome2, nome3, nome4]

print('O nome escolhido foi : {}' .format(random.choice(lista)))