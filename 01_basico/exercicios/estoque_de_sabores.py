

estoque = {"brigadeiro":10,"ninho":5, "maracuja":88, "beijinho":23} 

print(f"Temos um total de {estoque['brigadeiro']} de brigadeiros")
print(f"{estoque.get('cupuacu', 'Nao encontrado')}")

estoque['beijinho'] = 55
print(f"Temos um total de {estoque['beijinho']} de beijinhos")
print(f"{estoque}")