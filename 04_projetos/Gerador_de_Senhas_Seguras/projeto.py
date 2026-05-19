# ✅ Definir tamanho da senha

# ✅ Incluir letras maiúsculas, minúsculas, números e símbolos

# ✅ Botão para copiar a senha gerada

# ✅ Interface simples (CLI ou Web)




n = "n"
while n == "n":
    senha = input("Digite uma senha:")

    if any(chr.isdigit() for chr in senha) and senha.isupper() and senha.islower():
        print("Senha cuiuda")
        n = input("Manter essa senha? S/N")
    else:
        print("Senha macia")



















































