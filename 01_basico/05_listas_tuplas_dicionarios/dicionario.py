"""
wellington pereira luiz - PtBr - 2025
Dicionários em Python
Este exemplo demonstra o uso de dicionários em Python
"""

# Criando um dicionário
meu_dicionario = {
    "nome": "Wellington",
    "idade": 30,
    "cidade": "São Paulo"
}


# Acessando valores
print(f"Nome: {meu_dicionario['nome']}")
print(f"Idade: {meu_dicionario['idade']}")
print(f"Cidade: {meu_dicionario['cidade']}")


# Adicionando um novo par chave-valor
meu_dicionario["profissao"] = "Desenvolvedor"


# Imprimindo o dicionário atualizado
print("Dicionário atualizado:", meu_dicionario)


# Verificando se uma chave existe
if "idade" in meu_dicionario:
    print("A chave 'idade' existe no dicionário.")  
else:
    print("A chave 'idade' não existe no dicionário.")


# Removendo um par chave-valor
del meu_dicionario["cidade"]


# Imprimindo o dicionário após remoção
print("Dicionário após remoção da chave 'cidade':", meu_dicionario)


# Iterando sobre chaves e valores
for chave, valor in meu_dicionario.items():
    print(f"{chave}: {valor}")


# Verificando o tamanho do dicionário
print("Tamanho do dicionário:", len(meu_dicionario))


# Dicionários podem conter diferentes tipos de valores
outra_dict = {
    "nome": "Maria",
    "idade": 25,
    "ativo": True,
    "notas": [8.5, 9.0, 7.5]
}


# Acessando valores de tipos diferentes
print(f"Nome: {outra_dict['nome']}")
print(f"Idade: {outra_dict['idade']}")
print(f"Ativo: {outra_dict['ativo']}")
print(f"Notas: {outra_dict['notas']}")


# Dicionários aninhados
dicionario_aninhado = {
    "pessoa1": {
        "nome": "João",
        "idade": 28
    },
    "pessoa2": {
        "nome": "Ana",
        "idade": 22
    }
}


# Acessando valores em dicionários aninhados
print(f"Nome da pessoa1: {dicionario_aninhado['pessoa1']['nome']}")
print(f"Idade da pessoa2: {dicionario_aninhado['pessoa2']['idade']}")


# Métodos úteis
print("Chaves do dicionário:", meu_dicionario.keys())
print("Valores do dicionário:", meu_dicionario.values())
print("Itens do dicionário:", meu_dicionario.items())


# Convertendo dicionário para lista de tuplas
lista_tuplas = list(meu_dicionario.items())
print("Lista de tuplas:", lista_tuplas)


# Convertendo lista de tuplas para dicionário
lista_de_tuplas = [("chave1", "valor1"), ("chave2", "valor2")]
dicionario_de_tuplas = dict(lista_de_tuplas)

