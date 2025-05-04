#Faça um programa que abra e reproduza um arquivo em mp3.


print(10*'= ' + 'Vamos ouvir música' + 10*'= ' )

''''
Importado a biblioteca PYGAME, cujo qual tem uma função para executar o mp3.

'''
import pygame
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('/Users/dmonteiro/Downloads/Mp3/paper-planes-chill-future-beat-283956.mp3')
pygame.mixer.music.play()

# Esperar terminar
while pygame.mixer.music.get_busy():
    continue