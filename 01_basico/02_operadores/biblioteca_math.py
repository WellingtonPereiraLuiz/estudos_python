"""
Wellington Pereira Luiz - PtBr - 2025
Trabalhando com operadores básicos em Python
Este exemplo iremos trabalhar com a biblioteca math
"""

from math import sqrt, pow, factorial


#Exemplo simples de raiz quadrada
num = int(input("Digite um número para saber sua raiz quadrada:"))
raiz_quadrada = sqrt(num)
print(f"A raiz quadrada de {num} é igual a: {raiz_quadrada}")


#Exemplo simples de potenciação
base = int(input("Digite a base:"))
expoente = int(input("Digite o expoente:"))
potenciacao = pow(base, expoente)
print(f"O resultado de {base} elevado a {expoente} é igual a: {potenciacao}")


#Exemplo simples de fatorial
num_fatorial = int(input("Digite um número para saber seu fatorial:"))
fatorial = factorial(num_fatorial)
print(f"O fatorial de {num_fatorial} é igual a: {fatorial}")
#Fatorial e o resultado da multiplicação de todos os números inteiros positivos menores ou iguais a um determinado número.
#Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120
#O fatorial de 0 é 1 por definição.
#O fatorial de números negativos não é definido.
#O fatorial cresce muito rápido, por isso é usado em várias áreas da matemática, como combinatória, probabilidade e estatística.