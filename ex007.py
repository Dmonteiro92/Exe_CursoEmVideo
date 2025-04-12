#Um programa que leia duas notas de aluno, calcule e mostre sua média.

print('===== Desafio 07 - Média de notas')

nota =  float(input('Qual foi a nota da sua primeira prova? '))
nota2 = float(input('Qual foi a nota da sua segunra prova? '))

media = (nota+nota2)/2

print('Sua média de nota foi de: {}'.format(media))