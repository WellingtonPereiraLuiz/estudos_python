

total_dia = 0
for i in range(1, 6):
    valor = float(input(f"Digite o valor da {i}ª venda: "))
    total_dia += valor
print(f"Total de vendas do dia: R${total_dia:.2f}")