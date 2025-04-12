#Faça um programa que leia largura e altura de uma parede, calcule sua área e quantidade de tinta necessária pra pintar
#Sendo que cada litro de tinta pinta 2metros quadrado.

print('===== Desafio 011 -  Pintando a parede =====')

largura = float(input('Qual é a largura da sua parede? '))
altura = float(input('Qual é a altura dessa parede? '))

metros = largura * altura
tinta = metros / 2

print('Essa parede tem um total de {} metros quadrados'.format(metros))
print('Nesse caso precisamos de {}, litros de tinta'.format(tinta))

