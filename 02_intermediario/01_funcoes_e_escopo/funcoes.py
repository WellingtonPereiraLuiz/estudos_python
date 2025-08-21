"""
wellington pereira luiz - PtBr - 2025
Funções e escopo em Python
Este exemplo demonstra como definir e chamar funções, além de entender o escopo de variáveis.
"""


#Como criar uma função
def saudacao():
    print("Olá, bem-vindo ao Python!")

saudacao()



# Como definir uma função com parâmetros
def saudacao_nome(nome):
    """
    Função que recebe um nome e exibe uma saudação.
    """
    print(f"Olá, {nome}! Bem-vindo ao Python!")

saudacao_nome("Wellington")



# Como definir uma função com retorno
def soma(a, b):
    """
    Função que recebe dois números e retorna a soma deles.
    """
    return a + b
resultado = soma(5, 3)
print(f"A soma é: {resultado}")



# Como definir uma função com parâmetros padrão
def saudacao_padrao(nome="Visitante"):
    """
    Função que recebe um nome com valor padrão e exibe uma saudação.
    """
    print(f"Olá, {nome}! Bem-vindo ao Python!")

saudacao_padrao()  # Chamada sem argumento, usa o padrão
saudacao_padrao("Maria")  # Chamada com argumento



# Como definir uma função com múltiplos parâmetros
def saudacao_multiplos(nomes):
    """
    Função que recebe uma lista de nomes e exibe uma saudação para cada um.
    """
    for nome in nomes:
        print(f"Olá, {nome}! Bem-vindo ao Python!")
saudacao_multiplos(["Ana", "João", "Pedro"])



# Como definir uma função com argumentos variáveis
def saudacao_variavel(*nomes):
    """
    Função que recebe um número variável de nomes e exibe uma saudação para cada um.
    """
    for nome in nomes:
        print(f"Olá, {nome}! Bem-vindo ao Python!")
saudacao_variavel("Ana", "João", "Pedro", "Maria")



# Como definir uma função com escopo de variável
def escopo_variavel():
    """
    Função que demonstra o escopo de variáveis.
    """
    variavel_local = "Eu sou local"
    print(variavel_local)   
escopo_variavel()
# Tentativa de acessar a variável local fora da função
try:
    print(variavel_local)  # Isso causará um erro, pois variavel_local não está definida no escopo global   
except NameError as e:
    print(f"Erro: {e}")



# Como definir uma função que modifica uma variável global
variavel_global = "Eu sou global"   
def modifica_variavel_global():
    """
    Função que modifica uma variável global.
    """
    global variavel_global
    variavel_global = "Eu fui modificada"
    print(variavel_global)
modifica_variavel_global()
print(variavel_global)  # A variável global foi modificada



# Como definir uma função lambda (função anônima)
soma_lambda = lambda x, y: x + y
resultado_lambda = soma_lambda(10, 5)
print(f"A soma usando lambda é: {resultado_lambda}")



# Como usar funções como argumentos
def aplicar_funcao(func, a, b):
    """
    Função que aplica uma função passada como argumento a dois números.
    """
    return func(a, b)
resultado_aplicar = aplicar_funcao(soma, 7, 3)
print(f"O resultado da aplicação da função é: {resultado_aplicar}")
resultado_aplicar_lambda = aplicar_funcao(soma_lambda, 7, 3)
print(f"O resultado da aplicação da função lambda é: {resultado_aplicar_lambda}")
