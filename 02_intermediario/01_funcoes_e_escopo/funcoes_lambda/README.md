# Funções Lambda em Python: Um Guia Detalhado

Este diretório contém anotações e exemplos aprofundados sobre o uso de **funções lambda**, também conhecidas como **funções anônimas**, em Python.

## 1. O que é e por que usar uma Função Lambda?

Em Python, uma função `lambda` é uma forma de criar pequenas funções anônimas. A principal característica é sua simplicidade: ela pode ter múltiplos argumentos, mas **somente uma única expressão**.

A ideia principal é usar uma `lambda` quando você precisa de uma função simples por um curto período, e não quer se preocupar em nomeá-la formalmente com `def`. Elas são frequentemente chamadas de "funções descartáveis".

### Anatomia: `def` vs `lambda`

Para entender melhor, vamos comparar uma função padrão com sua equivalente em `lambda`.

**Função Padrão (`def`):**
```python
# Define uma função chamada 'soma' que aceita dois argumentos
def soma(a, b):
  return a + b

resultado = soma(5, 3) # resultado = 8 