# Leia preço e quantidade de trufas e imprima o total da venda.

preco = float(input("Digite o valor de venda: "))
quantidade = int(input("Digite a quantidade de trufas vendidas: "))

total_venda = preco * quantidade

print(f"Foram vendidas {quantidade} de trufas por R${preco}, obteve um total de vendas: R${total_venda}")