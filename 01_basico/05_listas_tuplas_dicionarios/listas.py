"""
wellington pereira luiz - PtBr - 2025
listas em Python
Este exemplo demonstra o uso de listas em Python
"""

# Criando uma lista
frutas = ["maçã", "banana", "laranja", "uva"]   

# Acessando elementos da lista
print(frutas[0])  
print(frutas[2])  
print(frutas[-1]) 


# Adicionando elementos à lista
frutas.append("manga")
print(frutas)  
frutas.insert(1, "abacaxi")
print(frutas)  


# Removendo elementos da lista
frutas.remove("banana")
print(frutas)  
frutas.pop()   # Remove o último elemento
print(frutas)  


# Verificando o tamanho da lista
print(len(frutas))  


# Iterando sobre a lista
for fruta in frutas:
    print(fruta)    


# Verificando se um elemento está na lista
if "laranja" in frutas:
    print("Laranja está na lista!")
else:
    print("Laranja não está na lista.")


# Ordenando a lista
frutas.sort()
print(frutas)
frutas.sort(reverse=True)
print(frutas)


# Invertendo a lista
frutas.reverse()
print(frutas)


# Copiando a lista
nova_lista = frutas.copy()
print(nova_lista)


# Limpando a lista
frutas.clear()
print(frutas)

