#Faça um algoritmo que mostre seu dobro, triplo e raiz quadrada.

print('===== Desafio 06 - Dobro, Triplo e Raiz =====')

nu1 = int(input('Digite um número que irei calcular: '))
nu2 = nu1*2
nu3 = nu1*3
nu4 = nu1**0.5

print('O número em questão é o {}\nO dobro desse número é {} \nJá o triplo é {}, \nPor fim sua raiz quadrada é {:.2f}'. format(nu1,nu2,nu3,nu4))
