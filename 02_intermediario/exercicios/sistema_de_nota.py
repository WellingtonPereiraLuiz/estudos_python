"""
Wellington Pereira Luiz - PtBr - 2025
Irei praticar fazendo um sistema simples de notas
"""
import os

#Requisitos

#Condicoes basicas
#Armazenamento de notas
#remover nota
#Adicionar nota
#Alterar nota

#Sobre a nota
#Deve possuir titutos curtos e com caracteres limitados(25)
#Ja o conteudo da nota pode ser ilimitado

#Sistema simples de limpar terminal
def clear_terminal():
    # Verifica o sistema operacional
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Linux ou macOS
        os.system('clear')

def linha():
    print('---------------------------------------------------')


notas_titulo = ['teste', 'segundo teste']
notas_conteudo = ['ifdfsfs', 'fsgsogosdk']

notas_pessoais = {}

c = -1
while c != 0:
    print('Seja muito bem vindo ao sistema de notas.')
    print('Escolha uma das opções do menu.')
    print('1 - Ver notas')
    print('2 - Adicionar notas.')
    print('0 - sair.')
    c = int(input('Escolha:'))

    if c == 1:
        clear_terminal()
        tamanho = len(notas_titulo)
        for i in range(tamanho):
            print(f"Nota {i+1}.")
            print(f"Titulo {notas_titulo[i]}")
            print(f"Conteudo: {notas_titulo[i]}")
            
        print('1 - voltar ao menu')
        print('2 - Alterar nota')
        print('0 - Sair')
        t = int(input("Escolha:"))
        if t == 1:
            clear_terminal()

            continue
        elif t == 2:
            for i in range(tamanho):
                print("Qual nota deseja alterar?")
                print(f"Nota {i+1}.")
                print(f"Titulo {notas_titulo[i]}")
                linha()
            g = int(input("Digite o numero da nota."))
            clear_terminal()
            print("Oque deseja alterar?")
            print("1 - titulo.")
            print("2 - Conteudo.")
            print("3 - voltar ao menu.")
            print("0 - Sair.")

                
        elif t == 0:
            c = 0
        else:
            clear_terminal()
            print("Opcao invalida, por favor escolha uma opcao valida.")
            print(input())
            clear_terminal()
            continue
            
    elif c == 2:
        pass
    elif c == 3:
        pass
    elif c == 0:
        c = 0
    else:
        clear_terminal()
        print("Opcao invalida, por favor escolha uma opcao valida.")
        print(input())
        clear_terminal()
        continue
clear_terminal()
print("Obrigado por usar nosso sitema, ate mais!")