"""
Wellington Pereira Luiz - PtBr - 2025
Programação Orientada a Objetos (POO) em Python
Este exemplo demonstra os conceitos básicos de POO, incluindo classes, objetos, atributos e métodos.
"""

#Pilares Da programação Orientada a Objetos(POO)
#1. Abstração
    # Exemplo: Criar uma classe "Carro" que abstrai os detalhes de um carro real, como marca, modelo e ano.
#2. Encapsulamento
    # Exemplo: Usar métodos getters e setters para controlar o acesso aos atributos de uma classe. Basicamente é esconder os detalhes internos de uma classe e expor apenas o necessário.
#3. Herança
    # Exemplo: Criar uma classe "Veículo" e depois criar subclasses como "Carro" e "Moto" que herdam os atributos e métodos da classe "Veículo".
#4. Polimorfismo
    # Exemplo: Criar um método "fazer_som" em uma classe base "Animal" e sobrescrevê-lo em subclasses como "Cachorro" e "Gato" para que cada animal faça um som diferente.




# # Definindo uma classe simples
# class Pessoa:
#     def __init__(self, nome, idade):
#         self.nome = nome  # Atributo de instância
#         self.idade = idade  # Atributo de instância

#     def apresentar(self):  # Método de instância
#         return f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos."
# # Criando um objeto (instância) da classe Pessoa
# pessoa1 = Pessoa("Wellington", 30)
# print(pessoa1.apresentar())



# # Definindo uma classe abstrata com atributos e métodos
# class Carro:
#     def __init__(self, marca, modelo, ano):
#         self.marca = marca  # Atributo de instância
#         self.modelo = modelo  # Atributo de instância
#         self.ano = ano  # Atributo de instância

#     def exibir_informacoes(self):  # Método de instância
#         return f"Carro: {self.marca} {self.modelo}, Ano: {self.ano}"

# uno = Carro("Fiat", "Uno", 2020)
# print(uno.exibir_informacoes())



# # Definindo uma classe com encapsulamento
# class ContaBancaria:
#     def __init__(self, titular, saldo_inicial=0):
#         self.titular = titular
#         self.__saldo = saldo_inicial  # Atributo privado

#     def depositar(self, valor):
#         if valor > 0:
#             self.__saldo += valor
#             print(f"Depósito de {valor} realizado. Novo saldo: {self.__saldo}")
#         else:
#             print("Valor de depósito deve ser positivo.")

#     def sacar(self, valor):
#         if 0 < valor <= self.__saldo:
#             self.__saldo -= valor
#             print(f"Saque de {valor} realizado. Novo saldo: {self.__saldo}")
#         else:
#             print("Saldo insuficiente ou valor inválido.")

#     def obter_saldo(self):
#         return self.__saldo
# # Criando um objeto (instância) da classe ContaBancaria
# conta = ContaBancaria("Wellington", 1000)
# conta.depositar(500)
# conta.sacar(200)
# print(f"Saldo atual: {conta.obter_saldo()}")



# # Definindo uma classe base e uma subclasse (herança)
# class Animal:
#     def fazer_som(self):
#         raise NotImplementedError("Subclasses devem implementar este método.")
    
# class Cachorro(Animal):
#     def fazer_som(self):
#         return "Au Au!"
    
# class Gato(Animal):
#     def fazer_som(self):
#         return "Miau!"
# # Criando objetos (instâncias) das subclasses
# cachorro = Cachorro()
# gato = Gato()
# print(cachorro.fazer_som())
# print(gato.fazer_som())

# # Demonstrando polimorfismo
# def emitir_som(animal):
#     print(animal.fazer_som())
# emitir_som(Cachorro())
# emitir_som(Gato())

