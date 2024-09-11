"""
#1. Faça um Programa que peça os três lados de um triângulo. O programa deverá informar se os valores podem ser
# um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

a = int(input('menor numero: '))
b = int(input('segundo menor: '))
c = int(input('maior: '))

if (a+b) > c:
    if a == b and b == c:
        print('equilatero')
        
    if a != b and b != c and c != a:
        print('escaleno')
        
    else:
        print('isoceles')
        
else: 
    print('invalido')
"""
#---------------------------------------------------------------------------------------------------------------------------
"""
#2. Determine se um ano é bissexto. Verifique no Google como fazer isso...

ano = int(input('ano: '))
ano_quatro = (ano % 4)
ano_cem = (ano % 100)
ano_quatrocentos = (ano % 400)

if ano_quatro > 0 and ano_cem > 0 and ano_quatrocentos:
    print('não é bisexto')
    
else:
    print('bisexto')
"""
#---------------------------------------------------------------------------------------------------------------------------
"""
#3. João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. 
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 
# quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável 
# peso (peso de peixes) e verifique se há excesso. Se houver, gravar na variável excesso e na variável multa o valor da 
# multa que João deverá pagar. Caso contrário mostrar tais variáveis com o conteúdo ZERO
    
peso = int(input('peso: '))

if peso > 50:
    peso = peso - 50
    multa = peso * 4
    print('multa: ', multa)
    
else:
    print('limite não excedido')
"""
#---------------------------------------------------------------------------------------------------------------------------
"""
#4. Faça um Programa que leia três números e mostre o maior deles

x = int(input('x: '))
y = int(input('y: '))
z = int(input('z: '))

if x > y and x > z:
    print(x)
elif y > x and y > z:
    print(y)
else:
    print(z)
"""
#---------------------------------------------------------------------------------------------------------------------------
"""
#5. Faça um Programa que leia três números e mostre o maior e o menor deles

x = int(input('x: '))
y = int(input('y: '))
z = int(input('z: '))

print(max([x,y,z]))
print(min([x,y,z]))
"""
#---------------------------------------------------------------------------------------------------------------------------
"""
#6. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o 
# total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,8% para o INSS e 5% para
# o sindicato, faça um programa que nos dê o salário bruto, quanto pagou ao INSS, quanto pagou ao sindicato e o salário 
# líquido. Observe que Salário Bruto - Descontos = Salário Líquido. Calcule os descontos e o salário líquido, conforme a 
# tabela abaixo:
# a. + Salário Bruto : R$
# b. - IR (11%) : R$
# c. - INSS (8%) : R$
# d. - Sindicato ( 5%) : R$
# e. = Salário Liquido : R$

salario_hora = float(input('salário / hora: '))
horas = int(input('horas / mês: '))

salario_bruto = salario_hora * horas
imposto_renda = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05
salario_liquido = salario_bruto - (imposto_renda + inss + sindicato)

print(salario_bruto)
print(inss)
print(sindicato)
print(salario_liquido)
"""
#---------------------------------------------------------------------------------------------------------------------------
"""
#7. Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 
# litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
# Obs. : somente são vendidos um número inteiro de latas

area = int(input('Área a ser pintada em m2: '))
litros = area / 3
latas = int(litros / 18)

if latas % 18 != 0:
    latas += 1

preco = latas * 80
print ('valor total: ', preco, ' latas: ', latas)
"""