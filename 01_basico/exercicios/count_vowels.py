quantia_vogal = 0

palavra = input("Digite uma palavra: ")

for letra in palavra:
    if letra in "aeiouAEIOU":
        print(f"Possui vogal. Vogal encontrada: {letra}")
        quantia_vogal += 1

print(f"A palavra {palavra} contem {quantia_vogal} vogal(s)")