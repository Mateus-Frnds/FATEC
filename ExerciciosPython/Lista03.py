"""
#1. Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo 
# até que o usuário informe um valor válido.

nota = int(input('numero de 0 - 10: '))

while not (0 <= nota <= 10):
    print('invalido.')
    nota = int(input('numero de 0 - 10: '))

print('valido')
"""
#---------------------------------------------------------------------------------------------------------------------------
"""
#2. Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma 
# mensagem de erro e voltando a pedir as informações.

usuario = (input('usuario: '))
senha = (input('senha: '))

while usuario == senha:
    print ('Erro. Usuario deve ser diferente de senha')
    usuario = (input('usuario: '))
    senha = (input('senha: '))

print ('usuario cadastrado')
"""
#---------------------------------------------------------------------------------------------------------------------------
"""
#3. Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a 
# população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o 
# número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas 
# de crescimento
    
cidade_a = 80000 
cidade_b = 200000
anos = 0

while cidade_a < cidade_b:
    cidade_a += cidade_a * 0.03
    cidade_b += cidade_b * 0.015
    anos += 1

print ('serao necessarios', anos, 'anos')
"""
#---------------------------------------------------------------------------------------------------------------------------
"""
#4. A seqüência de Fibonacci é a seguinte: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ... Sua regra de formação é simples: os dois 
# primeiros elementos são 1; a partir de então, cada elemento é a soma dos dois anteriores. Faça um algoritmo que leia um 
# número inteiro calcule o seu número de Fibonacci. F1= 1, F2= 1, F3= 2, etc.

n = int(input('n: '))

if n == 1 or n == 2:
    fibonacci = 1
else:
    n1, n2 = 1, 1
    for _ in range(3, n + 1):
        n1, n2 = n2, n1 + n2

fibonacci = n2
print(fibonacci)
"""
#---------------------------------------------------------------------------------------------------------------------------
"""
#5. Dados dois números inteiros positivos, determinar o máximo divisor comum entre eles usando o algoritmo de Euclides

def mdc(a, b):
    while b != 0:
        a, b = b, a % b
    return a

x = int(input('x: '))
y = int(input('y: '))

resultado = mdc(x, y)
print(f'O Máximo Divisor Comum entre {x} e {y} é {resultado}.')
"""