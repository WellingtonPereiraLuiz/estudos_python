vendas = [14, 25, 6, 42, 18]
maior_number = float('-inf')

for i in vendas:
    if i > maior_number:
        maior_number = i
        print(f"O {maior_number} é o maior numero")
        
    else:
        print(f"O {maior_number} continua sendo o maior numero")





"""Modelo da IA"""
# vendas = [14, 25, 6, 42, 18]

# if not vendas:
#     print("A lista de vendas está vazia!")
# else:
#     maior_number = float('-inf')
#     for i in vendas:
#         if i > maior_number:
#             maior_number = i

#     print(f"O maior número da lista é: {maior_number}")