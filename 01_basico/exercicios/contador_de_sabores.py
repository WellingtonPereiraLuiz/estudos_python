sabores_repetidos = ["brigadeiro", "ninho", "brigadeiro", "maracuja", "ninho", "brigadeiro"]
carrinho = {}
for item in sabores_repetidos:
    carrinho[item] = carrinho.get(item, 0) + 1
print(carrinho) 