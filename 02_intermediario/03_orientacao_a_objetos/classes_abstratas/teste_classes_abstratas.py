"""
wellington pereira luiz - PtBr - 2025
Programação Orientada a Objetos (POO) em Python
Este exemplo demonstra o conceito de classes abstratas
"""

from abc import ABC, abstractmethod
# Classe abstrata
class Forma(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimetro(self):
        pass
# Classe concreta que herda de Forma
class Retangulo(Forma):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
    def area(self):
        return self.largura * self.altura
    def perimetro(self):
        return 2 * (self.largura + self.altura)
# Classe concreta que herda de Forma
class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio
    def area(self):
        return 3.14 * (self.raio ** 2)
    def perimetro(self):
        return 2 * 3.14 * self.raio
# Criando instâncias das classes concretas
retangulo = Retangulo(5, 10)
circulo = Circulo(7)
# Usando os métodos das classes concretas
print(f"Retângulo - Área: {retangulo.area()}, Perímetro: {retangulo.perimetro()}")
print(f"Círculo - Área: {circulo.area()}, Perímetro: {circulo.perimetro()}")
# Demonstrando polimorfismo
def exibir_forma_info(forma):
    print(f"Área: {forma.area()}, Perímetro: {forma.perimetro()}")
exibir_forma_info(retangulo)
exibir_forma_info(circulo)
