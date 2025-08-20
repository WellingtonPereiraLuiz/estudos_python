"""
wellington pereira luiz - PtBr - 2025
estruturas de repetição em Python
Este exemplo demonstra o uso de estruturas de repetição  'while'
Iremos fazer um exemplo de validação de idade para primeira habilitação
"""

idade = 0
while idade < 18:
    idade = int(input("Digite sua idade: "))
    if idade >= 0 and idade < 18:
        print("Você ainda não pode tirar a habilitação.")
    elif idade >= 18:
        print("Você pode tirar a habilitação.")
    else:
        print("Idade inválida. Por favor, digite uma idade válida.")


