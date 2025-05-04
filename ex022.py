# Crie um programa que leia o nome completo de uma pessoa e mostre: - O nome com todas as letras maiúsculas e minúsculas.
# Quantas letras ao todo (sem considerar espaços). - Quantas letras tem o primeiro nome.


print('==== Desafio 022 - Manipulando seu nome ====')

nome = input('Digite seu nome completo: ').strip()
nome1 = nome.split()[0]

#print(f'Seu nome todo maísculo:{nome.upper()}')
print(f'Seu nome maísculo {nome.upper()}')
print(f'Seu nome minusculo {nome.lower()}')
nome2 = nome.replace(" ", "")
print(f'Seu nome tem um total de {len(nome2)} letras')
print(f'Seu primeiro nome tem {len(nome1)} letras')