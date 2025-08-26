# # Exercício: Abstração, Herança e Polimorfismo em Python

# ## Descrição

# Crie um sistema simples de gerenciamento de funcionários para uma empresa usando programação orientada a objetos.  
# Seu objetivo é praticar os conceitos de **abstração**, **herança** e **polimorfismo**.

# ## Requisitos

# 1. **Classe Abstrata:**  
#    - Crie uma classe abstrata chamada `Funcionario` usando o módulo `abc`.
#    - Ela deve possuir pelo menos um método abstrato chamado `calcular_salario`.

# 2. **Herança:**  
#    - Crie duas subclasses: `FuncionarioCLT` e `FuncionarioPJ`, ambas herdando de `Funcionario`.
#    - Cada subclasse deve implementar o método `calcular_salario` de acordo com regras diferentes:
#      - `FuncionarioCLT`: recebe salário fixo + benefícios.
#      - `FuncionarioPJ`: recebe valor por hora trabalhada.

# 3. **Polimorfismo:**  
#    - Crie uma função que recebe uma lista de funcionários (CLT e PJ misturados) e imprime o salário de cada um usando o método `calcular_salario`.

# 4. **Extras (opcional):**  
#    - Adicione atributos relevantes às classes (nome, cargo, etc).
#    - Implemente métodos para exibir informações dos funcionários.

# ## Observações

# - Não é necessário implementar o código neste arquivo, apenas a descrição.
# - Use comentários e docstrings nos seus arquivos de código para explicar suas escolhas.
# - Teste seu código criando instâncias de cada tipo de funcionário e usando a função polimórfica.

# ---

# **Boa prática! Use este exercício para revisar e consolidar os conceitos de


"""
wellington pereira luiz - PtBr - 2025
Programação Orientada a Objets (POO) em Python
Este exemplo demonstra os conceitos básicos de POO, incluindo classes, objetos, atributos e métodos.
"""
from abc import ABC, abstractmethod

class Funcionario(ABC):
    @abstractmethod
    def calcularsalario(self):
        pass

class FuncionarioCLT(Funcionario):
    def __init__(self, nome, cargo):
        self.nome = nome
        self.cargo = cargo
       
    def calcularsalario(self):
        return f"O funcionario {self.nome} com o cargo de {self.cargo} recebe salário fixo + benefícios."
        


class FuncionarioPJ(Funcionario):
    def __init__(self, nome, cargo,):
        self.nome = nome
        self.cargo = cargo
       
    def calcularsalario(self):
        return f"O funcionario {self.nome} com o cargo de {self.cargo} recebe valor por hora trabalhada."
  

joao = FuncionarioCLT(nome= 'Joao', cargo='Faxineiro')
print(joao.calcularsalario())

Joaquin = FuncionarioPJ(nome="joaquin", cargo="ADM")
print(Joaquin.calcularsalario())