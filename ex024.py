#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

print('==== Desafio 024 - Sua cidade começa com SANTO? ====')
cidade = input("Digite o nome de uma cidade: ").strip()
if cidade.upper().startswith("SANTO"):
    print("A cidade começa com 'SANTO'.")
else:
    print("A cidade não começa com 'SANTO'.")