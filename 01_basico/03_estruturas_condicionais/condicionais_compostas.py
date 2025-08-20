"""
wellington pereira luiz - PtBr - 2025
Estruturas condicionais compostas em Python
Este exemplo demonstra o uso de estruturas condicionais compostas 'if', 'elif' e 'else' na recriação do calculo do IMC (Índice de Massa Corporal)
"""

# Recebe os dados do usuário
nome = input("Digite seu nome:")
altura = float(input("Digite sua altura(Metros):"))
peso = float(input("Digite seu peso(kg):"))

# Calcula o IMC
imc = peso / (altura ** 2)

# Exibe o resultado do IMC e a classificação
if imc < 18.5:
    print(f"Ola {nome}, seu IMC é de: {imc:.2f}. Você está abaixo do peso.")
elif 18.5 <= imc < 24.9:
    print(f"Ola {nome}, seu IMC é de: {imc:.2f}. Você está com peso normal.")
elif 25 <= imc < 29.9:
    print(f"Ola {nome}, seu IMC é de: {imc:.2f}. Você está com sobrepeso.")
elif 30 <= imc < 34.9:
    print(f"Ola {nome}, seu IMC é de: {imc:.2f}. Você está com obesidade grau 1.")
elif 35 <= imc < 39.9:
    print(f"Ola {nome}, seu IMC é de: {imc:.2f}. Você está com obesidade grau 2.")
else:
    print(f"Ola {nome}, seu IMC é de: {imc:.2f}. Você está com obesidade grau 3.")




