"""
Wellington Pereira Luiz
Expressões Regulares (Regex)
Resumo prático de sintaxe para consulta rápida.
"""

import re

# ==========================================
# 1. ÂNCORAS (Travam o início ^ e o fim $)
# ==========================================
# Garante correspondência exata, sem sobras.
padrao_ancoras = r"^PROD-01$"

re.match(padrao_ancoras, "PROD-01")    # Match
re.match(padrao_ancoras, " PROD-01")   # None (Falha pelo espaço no início)
re.match(padrao_ancoras, "PROD-01XYZ") # None (Falha por ter texto no fim)


# ==========================================
# 2. METACARACTERES E CLASSES (Tipos de dados)
# ==========================================
# \d = Qualquer número (0-9). 
# Cada \d consome exatamente 1 caractere.
padrao_classes = r"^PROD-\d\d$"

re.match(padrao_classes, "PROD-42")  # Match
re.match(padrao_classes, "PROD-AB")  # None (AB não são números)
re.match(padrao_classes, "PROD-7")   # None (Falta o segundo número)


# ==========================================
# 3. QUANTIFICADORES (Repetições)
# ==========================================
# {min,max} = Controla a repetição do item anterior.
# Evita escrever \d repetidas vezes.
padrao_quantificadores = r"^WLP-\d{3,5}$"

re.match(padrao_quantificadores, "WLP-123")    # Match (3 números)
re.match(padrao_quantificadores, "WLP-12345")  # Match (5 números)
re.match(padrao_quantificadores, "WLP-12")     # None (Abaixo do mínimo)


# ==========================================
# 4. LOOKAHEAD (Validação Simultânea)
# ==========================================
# (?=...) = Espia a string à frente sem consumir os caracteres.
# Padrão abaixo: Exige 1 Maiúscula E 1 Número em qualquer posição.
padrao_lookahead = r"^(?=.*[A-Z])(?=.*\d).+$"

re.match(padrao_lookahead, "Senha1")  # Match (Tem maiúscula e número)
re.match(padrao_lookahead, "senha1")  # None (Falta a maiúscula)
re.match(padrao_lookahead, "SENHA")   # None (Falta o número)