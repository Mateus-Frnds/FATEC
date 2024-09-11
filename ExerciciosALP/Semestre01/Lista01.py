"""
#1. Faça um programa que peça dois números inteiros e imprima a soma desses dois números

x = int((input('Primeiro número: ')))
y = int(input('Segundo número: '))
print(f'Soma dos dois números = {x + y}')
"""
#---------------------------------------------------------------------------------------------------------------------------
"""
#2. Escreva um programa que leia um valor em metros e o exiba convertido em milímetros

print ('Bem vindo ao conversor de metros em milimetros')
metros = float((input('Insira o número em metros: ')))
print(f'Seu resultado é: {metros * 1000}')
"""
#---------------------------------------------------------------------------------------------------------------------------
"""
#3. Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total em segundos.
#OBS: 'Reval' pode ser usado para receber e printar os dados em ordem reval(input a, b, c, d)

print ('Bem vindo ao conversor de tempo em segundos')
dias = int(input('Insira um número de dias: '))
horas = int(input('Insira um número de horas: '))
minutos = int(input('Insira um número de minutos: '))
segundos = int(input('Insira um número de segundos: '))

dias_convertido = float(dias * 86400)
horas_convertido = float(horas * 3600)
minutos_convertido = float(minutos * 60)
total = (dias_convertido + horas_convertido + minutos_convertido + segundos)

print (f'Seu total é:  {total}')
"""
#---------------------------------------------------------------------------------------------------------------------------
"""
#4. Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a porcentagem do aumento. 
# Exiba o valor do aumento e do novo salário

print ("Bem vindo ao calculo de aumento de salário")
salario = float(input('Insira seu salário: '))
aumento = int(input('insira a porcentagem do aumento: '))

aumento_final = float(aumento * 0.01)
salario_final = float(salario * aumento_final)
total = float(salario + salario_final)

print ('Seu aumento foi de: ', salario_final) 
print ('Seu total é: ', total) 
"""
#---------------------------------------------------------------------------------------------------------------------------
"""
#5. Solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar

valor = float (input("Digite o valor da mercadoria: "))
desconto = float (input("Digite o percentual de desconto: "))
desconto_final = float(desconto * 0.01)
valor_final = float(valor * desconto_final)
total = float(valor - valor_final)

print ('Seu desconto foi de: ', valor) 
print ('Seu total é: ', total) 
"""
#---------------------------------------------------------------------------------------------------------------------------
"""
#6. Calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média esperada para a viagem

distancia = int (input('Digite a distancia percorrida em km: '))
velocidade_media = int(input('Digite o número da velocidade média em km do percurso: '))
tempo_trajeto = float (distancia / velocidade_media)

print ('Seu tempo de trajeto é: ', tempo_trajeto, 'hora(s)')
"""
#---------------------------------------------------------------------------------------------------------------------------
"""
#7.Converta uma temperatura digitada em Celsius para Fahrenheit. Formula: F = 9*C/5 + 32

temperatura = float (input('Insira a temperatura em Celsius para converter em Fahrenheit: '))
temperatura_convertida = float ((9 * temperatura) / 5 + 32)

print (temperatura_convertida)
"""
#---------------------------------------------------------------------------------------------------------------------------
"""
#8. Faça agora o contrário, de Fahrenheit para Celsius.

temperatura = float (input('Insira a temperatura em Fahrenheit para converter em Celsius: '))
temperatura_convertida = float((temperatura - 32) * 5 / 9)

print (temperatura_convertida)
"""
#---------------------------------------------------------------------------------------------------------------------------
"""
#9. Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim como a 
# quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e 
# R$ 0,15 por km rodado

km_percorridos = int (input('Insira a quantidade de km percorridos pelo carro: '))
dias_alugados = int (input('Agora insira a quantidade de dias em que o carro foi alugado: '))

valor_total = float((km_percorridos * 0.15) + (dias_alugados * 60))

print ('O valor total a ser pago pela locação é de R$', valor_total)
"""
#---------------------------------------------------------------------------------------------------------------------------
"""
#10. Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a quantidade de cigarros fumados 
# por dia e quantos anos ele já fumou. Considere que um fumante perde 10 minutos de vida a cada cigarro, calcule quantos 
# dias de vida um fumante perderá. Exiba o total de dias

cigarros_por_dia = int (input('Insira a quantidade de cigarros que você fuma por dia: '))
anos_fumando = int (input('Insira a quantidade de anos em que você fuma: '))
cigarros_fumados = int (cigarros_por_dia * (anos_fumando * 365))
tempo_perdido = float ((cigarros_fumados * 10) / 1440)

print(f'Você perdeu {tempo_perdido:.2f} dias de vida por conta do cigarro')
"""
#---------------------------------------------------------------------------------------------------------------------------
"""
#11. Sabendo que str( ) converte valores numéricos para string, calcule quantos dígitos há em 2 elevado a um milhão.

import sys
sys.set_int_max_str_digits(10**6)

total = 2 ** 1_000_000
digitos = len(str(total))

print('O número tem um total de ', digitos, ' dígitos.')
"""