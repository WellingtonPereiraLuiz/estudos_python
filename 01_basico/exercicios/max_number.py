contador = 0
max_number = 0
while contador < 3:
    number_entry = float(input("Digite um number aleatorio: "))
    contador += 1
    if number_entry > max_number:
        print(f"O numero digitado e maior ao anterior Digitado: {number_entry} | Anterior: {max_number}")
        max_number = number_entry
    else:
        print(f"O numero digitado e inferior ao anterior digitado: {number_entry} | Anterior: {max_number}")

   