# ✅ Definir tamanho da senha

# ✅ Incluir letras maiúsculas, minúsculas, números e símbolos

# ✅ Botão para copiar a senha gerada


import re
import random
import string
import pyperclip

print("Seja muito bem vindo ao seu gerador de senhas automaticos!")
maiuscula = random.choice(string.ascii_uppercase)
minuscula = random.choice(string.ascii_lowercase)
numero = random.choice(string.digits)
simbolo = random.choice(string.punctuation)

caracteres = string.digits + string.ascii_lowercase + string.ascii_uppercase + string.ascii_letters + string.punctuation

senha = ''.join(random.choices(caracteres, k=4))

senha_lista = [maiuscula, minuscula, numero, simbolo]

random.shuffle(senha_lista)

senha_final = "".join(senha_lista)

print(senha_final)

# Copiando para o sistema
pyperclip.copy(senha_final)
print("Senha copiada para a área de transferência! (Clipboard updated)")




