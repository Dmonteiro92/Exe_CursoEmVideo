#Utilize o exercício anterior, mas dessa vez escolha uma ordem para os nomes.


import random
print(10* '=' + ' Desafio do nome aleatorio ' + 10 * '=')
print('Digite quatro nomes e iremos ordenar')
nome1 = input('Digite o primeiro nome: ')
nome2 = input('Digite o segundo nome: ')
nome3 = input('Digite o terceiro nome: ')
nome4 = input('Digite o quarto nome: ' )
lista = [nome1, nome2, nome3, nome4]
random.shuffle(lista)

for nome in lista:
    print(nome)