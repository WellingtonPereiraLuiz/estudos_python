"""
Wellington Pereira luiz - PtBr - 2025
Abstração em Python
Este exemplo demonstra o conceito de abstração na programação orientada a objetos (POO).
"""

# Definindo uma classe abstrata com atributos e métodos
class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca  # Atributo de instância
        self.modelo = modelo  # Atributo de instância
        self.ano = ano  # Atributo de instância

    def exibir_informacoes(self):  # Método de instância
        return f"Carro: {self.marca} {self.modelo}, Ano: {self.ano}"
# Criando um objeto (instância) da classe Carro
uno = Carro("Fiat", "Uno", 2020)
print(uno.exibir_informacoes())







# Definindo uma classe abstrata com métodos abstratos usando abc. Aqui irei deixar com comentarios mais detalhados
# para que você possa entender melhor o funcionamento do abc
# Aqui nos usamos abstracao, heranca e polimorfismo
from abc import ABC, abstractmethod # Importando ABC e abstractmethod do módulo abc

# Classe abstrata Animal, serve como base para outras classes
class Animal(ABC):
    @abstractmethod # Decorador que indica que o método é abstrato
    def fazer_som(self):
        # Método abstrato, deve ser implementado pelas subclasses
        pass

# Cachorro herda de Animal e implementa o método fazer_som
class Cachorro(Animal): # Aplicacao da heranca
    def fazer_som(self):
        return "Au Au!"

# Gato herda de Animal e implementa o método fazer_som
class Gato(Animal): # Aplicacao da heranca
    def fazer_som(self):
        return "Miau!"

# Criando objetos (instâncias) das subclasses
cachorro = Cachorro()  # Instância de Cachorro
gato = Gato()          # Instância de Gato

# Polimorfismo: cada animal faz seu som característico
# Uso direto dos métodos das classes
print(cachorro.fazer_som())
print(gato.fazer_som())

# Demonstrando polimorfismo
# Uso de uma função que aceita qualquer objeto do tipo Animal tornando mais generico e flexivel
def emitir_som(animal):
    print(animal.fazer_som())
emitir_som(Cachorro())
emitir_som(Gato())