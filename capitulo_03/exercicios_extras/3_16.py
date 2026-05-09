import tkinter as tk


# def diga_ola():
#     print(input("Diga seu nome: "))
#     print("Olá!")
    
window = tk.Tk()
window.title("Meu novo Projeto") # Título do projeto/ atributo da janela 
window.geometry("400x300")  # definindo o tamanho da janela

# label = tk.Label(window, text= "Olá, Mundo!")
# label.pack()

# botao = tk.Button(window, text="Don't Click me!", command=diga_ola)
# botao.pack()

def mostrar_texto():
    print(entrada.get())

entrada = tk.Entry(window)
entrada.pack()

botao = tk.Button(window, text="Enviar", command=mostrar_texto())
botao.pack()





window.mainloop()  # método que mantém a janela aberta 