"""
Wellington Pereira Luiz - PtBr - 2025
Um teste com um sistema de falso e verdadeiro
Usarei um exemplo de primeira habilitacao mas irei viajar bastante hahahaha
"""

import os

#Preciso verificar a idade da pessoa 
#Se tiver mais que 18 anos fazer as seguintes verifcacoes
    #Possui RH atualizado nos ultimos 5 anos?
        #Se sim prossiga, senao peca para o usuario ir atras disso e reinicie todo o sistema
    #Possui foto 4x4?
        #Mesma situacao do RH

def clear_terminal():
    # Verifica o sistema operacional
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Linux ou macOS
        os.system('clear')
        
c = -1
while c != 0:
    print("Seja muito bem vindo ao Detran!")
    print("Escolha uma das opcoes:")
    print("1 - Primeira CNH.")
    print("2 - Renovação.")
    print("3 - Reciclagem.")
    print("0 - Sair.")
    c = int(input("Opcao:"))

    if c == 1:
        print("Voce escolheu a opcao de Primeira CNH.")
        print("Para prossseguir com o cadastro precisamos de algumas informações basicas.")
        idade = int(input("Digite sua idade:"))
        if idade >= 18 and idade < 80:
            print("Idade valida, prossiga com o cadastro.")
            validar = input("Voce possui RG atualizado nos ultimos 5 anos? (S/N):").upper()
            if validar == "S":
                print("Otimo, prossiga.")
                validar = input("Voce possui foto 4x4? (S/N):").upper()
                if validar == "S":
                    print("Otimo, prossiga com o cadastro.")
                else:
                    print("Por favor providencie uma foto 4x4 e volte aqui depois.")
                    continue
            else:
                print("Por favor providencie um RG atualizado e volte aqui depois.")
                continue
        else:
            print("Idade invalida para primeira habilitacao. Voce precisa ter entre 18 e 80 anos.")
            continue

    elif c == 2:
        print("Voce escolheu a opcao de Renovacao.")
        print("Para prossseguir com o cadastro precisamos de algumas informacoes basicas.")
        idade = int(input("Digite sua idade:"))
        if idade >= 18 and idade < 80:
            print("Idade valida, prossiga com o cadastro.")
            validar = input("Voce possui CNH vencida a menos de 30 dias? (S/N):").upper()
            if validar == "S":
                print("Otimo, prossiga.")
                validar = input("Voce possui foto 4x4? (S/N):").upper()
                if validar == "S":
                    print("Otimo, prossiga com o cadastro.")
                else:
                    print("Por favor providencie uma foto 4x4 e volte aqui depois.")
                    continue
            else:
                print("Por favor providencie uma CNH vencida a menos de 30 dias e volte aqui depois.")
                continue
        else:
            print("Idade invalida para renovacao de habilitacao. Voce precisa ter entre 18 e 80 anos.")
            continue

    elif c ==3:
        print("Voce escolheu a opcao de Reciclagem.")
        print("Para prossseguir com o cadastro precisamos de algumas informacoes basicas.")
        idade = int(input("Digite sua idade:"))
        if idade >= 18 and idade < 80:
            print("Idade valida, prossiga com o cadastro.")
            validar = input("Voce possui CNH suspensa? (S/N):").upper()
            if validar == "S":
                print("Otimo, prossiga.")
                validar = input("Voce possui foto 4x4? (S/N):").upper()
                if validar == "S":
                    print("Otimo, prossiga com o cadastro.")
                else:
                    print("Por favor providencie uma foto 4x4 e volte aqui depois.")
                    continue
            else:
                print("Por favor providencie uma CNH suspensa e volte aqui depois.")
                continue
        else:
            print("Idade invalida para reciclagem de habilitacao. Voce precisa ter entre 18 e 80 anos.")
            continue
    elif c == 0:
        print("Saindo do sistema. Ate mais!")
    else:
        print("Opcao invalida, por favor escolha uma opcao valida.")
        clear_terminal()
        continue







# Exemplo de uso

