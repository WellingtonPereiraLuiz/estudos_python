from tkinter import *
import random
# Configuração principal da janela
root = Tk()
root.geometry('700x500')
root.title('app de motivacao diaria')
root.config(bg='lightblue')

frame_texto = Frame(root)
frame_texto.pack(side=BOTTOM)

# Configurações globais
fonte = ('Arial', 14)
letra = 'white'

# Estrutura de layout
frame = Frame(root, bg='lightblue')
frame.pack(pady=20, padx=20)

frases = ["rtyuil","ertfygjuhkj","exrdt,k"]
contador = 0
def mostrar_frase():
    global contador
    try:
      
        tamanho = len(frases)
        if contador < tamanho and contador >=0:
         
            resultado_mostrar.config(text=f'{frases[contador]}')  
           
            contador += 1
        else: 
            resultado_mostrar.config(text='Voce ja viu todas as frases, clique denovo para recomecar')
            contador = 0
    except ValueError:
        resultado_mostrar.config(text='Por favor, insira valores válidos.', fg='red')


def  adicionar_frase():
    try:
        frases.append(entrada_frase.get())
        resultado.config(text=f'Voce adicionou uma frase: {entrada_frase.get()}')
    
    except ValueError:
        resultado_adicionado.config(text='Por favor, insira valores válidos.', fg='red')

def aleatorio_frase():
    global contador
    try:
      
        tamanho = len(frases)
        if contador < tamanho and contador >=0:
            x = random.choice(frases)
            resultado_mostrar.config(text=f'{x}')  
           
            contador += 1
        else: 
            contador = 0
    except ValueError:
        resultado_mostrar.config(text='Por favor, insira valores válidos.', fg='red')


def clear_placeholder(event, entry):
    if entry.get() in ('Digite a nova frase'):
        entry.delete(0, 'end')

# Widgets
#apresentacao
Label_apresentacao = Label(frame, text='Seja bem vindo ao seu app de motivacao', fg=letra, bg='lightblue', font=fonte)
Label_apresentacao.grid(row=0, column=0, pady=10, padx=20)

#Adicionar novas frases na lista.
label_frase = Label(frame, text='Nova frase:', fg=letra, bg='lightblue', font=fonte)
label_frase.grid(row=1, column=0, pady=10, padx=20)


entrada_frase = Entry(frame, font=fonte)
entrada_frase.grid(row=1, column=1, pady=10, padx=20)
entrada_frase.insert(0, 'Digite a nova frase')
entrada_frase.bind('<FocusIn>', lambda event: clear_placeholder(event, entrada_frase))

botao_adicionar = Button(frame, text="Adicionar frase", command=adicionar_frase, bg='blue', fg=letra, font=fonte)
botao_adicionar.grid(row=2, column=0, columnspan=2, pady=20)


resultado_adicionado = Label(frame, text='', fg=letra, bg='lightblue', font=fonte)
resultado_adicionado.grid(row=3, column=0, columnspan=2, pady=10)

# #Visualizar frases uma a uma

botao_mostrar = Button(frame, text="Mostrar frase", command=mostrar_frase, bg='blue', fg=letra, font=fonte)
botao_mostrar.grid(row=4, column=0, columnspan=2, pady=20)


resultado_mostrar = Label(frame, text='', fg=letra, bg='lightblue', font=fonte)
resultado_mostrar.grid(row=5, column=0, columnspan=2, pady=10)






botao_aleatorio = Button(frame, text="Frase aleatoria", command=aleatorio_frase, bg='blue', fg=letra, font=fonte)
botao_aleatorio.grid(row=6, column=0, columnspan=2, pady=20)

resultado_aleatorio = Label(frame, text='', fg=letra, bg='lightblue', font=fonte)
resultado_aleatorio.grid(row=5, column=0, columnspan=2, pady=10)



# #ou sortear frase
# botao = Button(frame, text="Adicionar frase", command=adicionar_frase, bg='blue', fg=letra, font=fonte)
# botao.grid(row=2, column=0, columnspan=2, pady=20)










resultado = Label(frame, text='', fg=letra, bg='lightblue', font=fonte)
resultado.grid(row=3, column=0, columnspan=2, pady=10)


root.mainloop()

