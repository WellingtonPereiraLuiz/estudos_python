contador = 0
max_number = float('-inf')
while contador < 3:
    number_entry = float(input("Digite um number aleatorio: "))
    contador += 1
    if number_entry > max_number:
        print(f"O numero digitado e maior ate o momento. Maior numero: {number_entry}")
        max_number = number_entry
    else:
        print(f"O numero digitado não e o maior numero: Numero digitado {number_entry} | Maior numero: {max_number}")

   