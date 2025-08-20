"""
wellington pereira luiz - PtBr - 2025
Trabalhando com operadores básicos em Python
Este exemplo iremos fazer um caculo simples de IMC (Índice de Massa Corporal)
"""

nome = input("Digite seu nome:")
altura = float(input("Digite sua altura(Metros):"))
peso = float(input("Digite seu peso(kg):"))

imc = peso / (altura ** 2)

print(f"Ola {nome} o seu imc é de: {imc:.2f}")