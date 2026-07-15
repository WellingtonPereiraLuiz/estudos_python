# Leia preço e quantidade de trufas e imprima o total da venda.

preco = float(input("Digite o valor de venda: "))
quantidade = int(input("Digite a quantidade de trufas vendidas: "))

if preco <= 0 or quantidade <= 0:
    print("Valor inválido, digite novamente.")
else:
    total_venda = preco * quantidade
    print(f"Foram vendidas {quantidade} trufas por R${preco:.2f}, obteve um total de vendas: R${total_venda:.2f}")
