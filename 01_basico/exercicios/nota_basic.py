# Leia uma nota (0–10): ≥7 Aprovado, 5–6.9 Recuperação, <5 Reprovado. (Sem olhar o antigo!)
                                                                     
nota = float(input("Digite a sua nota: "))

if nota >= 7 and nota <= 10:
    print("Aprovado!")
elif nota < 7 and nota >= 5:
    print("Recuperação")
elif nota < 5 and nota >= 0:
    print("Reprovado")
else:
    print("Nota invalida!")