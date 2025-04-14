#Escreva um programa que convertar as temperaturas, CELSIUS, FAHRENHEIT e KEVIN

print('===== Desafio 013 - Temperaturas ======')
print('Vamos converter a temperatura, para você não queimar ou congelar :D ')

temp = float(input('Digite a temperatura em CELSIUS: '))
fah = (temp * 9/5) + 32
kev = temp+273.15

print('Nessa situação de {} celsius, temos o seguinte cenário: \n{} fahrenheit \n{} kevin'.format(temp,fah,kev))