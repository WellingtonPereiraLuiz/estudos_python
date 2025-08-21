"""
wellington pereira luiz - PtBr - 2025
Decoradores em Python
Este exemplo demonstra como criar e usar decoradores para modificar o comportamento de funções.
"""
# Porque usamos decoradores?
# - Reutilização de código
# - Separação de responsabilidades
# - Adicionar funcionalidades sem modificar o código original




# Como criar um decorador simples
def meu_decorador(func):
    def wrapper():
        print("Antes da função ser chamada.")
        func()
        print("Depois da função ser chamada.")
    return wrapper  
@meu_decorador
def diz_ola():
    print("Olá!")
diz_ola()

