"""
wellington pereira luiz - PtBr - 2025
Lambda em Python
Este exemplo demonstra como usar funções lambda para criar funções anônimas e simples.
"""

# # Como criar uma função lambda simples
# soma_lambda = lambda x, y: x + y
# resultado_lambda = soma_lambda(5, 3)
# print(f"A soma usando lambda é: {resultado_lambda}")


# # Como usar uma função lambda com lista
# x = [1, 2, 3, 4, 5]
# a = lambda lista: (x + 1 if x >= 3 else x for x in lista)
# print(list(a(x)))


# Como usar uma função lambda com map
numeros = [1, 2, 3, 4, 5]
numeros_incrementados = list(map(lambda x: x + 1, numeros))
print(f"Números incrementados: {numeros_incrementados}")
