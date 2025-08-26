"""
wellington pereira luiz - PtBr - 2025
Programação Orientada a Objets (POO) em Python
Este exemplo demonstra o conceito de metaclasses em Python.
"""

# Definindo uma metaclasse
class Meta(type):
    def __new__(cls, name, bases, attrs):
        print(f"Criando a classe {name} com a metaclasse Meta")
        return super().__new__(cls, name, bases, attrs)
# Definindo uma classe que usa a metaclasse Meta
class MinhaClasse(metaclass=Meta):
    def __init__(self, valor):
        self.valor = valor
    def mostrar_valor(self):
        return f"O valor é: {self.valor}"
# Criando uma instância de MinhaClasse
obj = MinhaClasse(42)
print(obj.mostrar_valor())
# Verificando o tipo da instância e da classe
print(f"Tipo da instância: {type(obj)}")
print(f"Tipo da classe: {type(MinhaClasse)}")
