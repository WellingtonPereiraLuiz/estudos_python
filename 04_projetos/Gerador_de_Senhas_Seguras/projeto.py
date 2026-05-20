# ✅ Definir tamanho da senha

# ✅ Incluir letras maiúsculas, minúsculas, números e símbolos

# ✅ Botão para copiar a senha gerada


import re
import random
import string
# import pyperclip

tamanho = int(input("Qual o tamanho da senha?"))

print("Seja muito bem vindo ao seu gerador de senhas automaticos!")
maiuscula = random.choice(string.ascii_uppercase)
minuscula = random.choice(string.ascii_lowercase)
numero = random.choice(string.digits)
simbolo = random.choice(string.punctuation)

caracteres = string.digits + string.ascii_lowercase + string.ascii_uppercase + string.ascii_letters + string.punctuation

senha = (random.choices(caracteres, k=tamanho - 4))

senha_lista = [maiuscula, minuscula, numero, simbolo, senha]

random.shuffle(senha_lista)
senha_final = "".join(str(item) for sublista in senha_lista for item in sublista)

print(f"Senha gerada: {senha_final}")

# # Copiando para o sistema
# pyperclip.copy(senha_final)
# print("Senha copiada para a área de transferência! (Clipboard updated)")




