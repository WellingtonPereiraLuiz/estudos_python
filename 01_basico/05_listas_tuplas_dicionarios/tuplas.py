"""
wellington pereira luiz - PtBr - 2025
tuplas em Python
Este exemplo demonstra o uso de tuplas em Python
"""

# Definindo uma tupla
minha_tupla = (1, 2, 3, 4, 5)
print(f"Tupla: {minha_tupla}")


#tipo de dado tupla
print(f"Tipo: {type(minha_tupla)}")


# Acessando elementos da tupla
print(f"Primeiro elemento: {minha_tupla[0]}")
print(f"Último elemento: {minha_tupla[-1]}")


# Tuplas são imutáveis, então não podemos adicionar ou remover elementos
# minha_tupla[0] = 10  # Isso causará um erro


# Verificando o tamanho da tupla
print(f"Tamanho da tupla: {len(minha_tupla)}")


# Iterando sobre a tupla
for item in minha_tupla:
    print(item)


# Tuplas podem conter elementos de tipos diferentes
outra_tupla = (1, "dois", 3.0, True)
print(outra_tupla)


# Desempacotando tuplas
a, b, c, d = outra_tupla
print(f"a: {a}, b: {b}, c: {c}, d: {d}")


# Tuplas aninhadas
tupla_aninhada = (1, (2, 3), (4, 5))
print(tupla_aninhada)
print(tupla_aninhada[1])  # Acessando a segunda tupla
print(tupla_aninhada[1][0])  # Acessando o primeiro elemento da segunda tupla


# Métodos de tuplas
print(f"Contar 2 na tupla: {minha_tupla.count(2)}") 
print(f"Índice de 3 na tupla: {minha_tupla.index(3)}")


# Convertendo lista para tupla
lista = [6, 7, 8]
tupla_de_lista = tuple(lista)
print(tupla_de_lista)
