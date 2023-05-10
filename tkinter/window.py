from tkinter import *
from tkinter import ttk


window = Tk()

class Aplication():

    def __init__(self):
        self.window = window
        self.tela()
        self.frames_da_tela()
        self.widgets_frame1()
        
        window.mainloop()
    
    def tela(self):
        self.window.title("Cadastro de clientes")
        self.window.configure(background= "white")
        self.window.geometry("700x500") #Definir dimensões da tela
        self.window.resizable(False, False) #Impedir que seja possível alterar o tamanho da tela no eixo x e y
        
    def frames_da_tela(self):
        self.frame_1 = Frame(self.window, bg="#c0c0c0", highlightthickness=2, highlightbackground="#a30000")
        self.frame_1.place(relx= 0.02, rely= 0.02, relwidth=0.96, relheight=0.46)
        
        self.frame_2 = Frame(self.window, bg="#c0c0c0", highlightthickness=2, highlightbackground="#a30000")
        self.frame_2.place(relx= 0.02, rely= 0.5, relwidth=0.96, relheight=0.46)
        
    def widgets_frame1(self):
        
        ###Criação do botão limpar
        self.btn_limpar = Button(self.frame_1, bg="#a30000", text="Limpar", font="Arial")
        self.btn_limpar.place(relx= 0.2, rely=0.1, relwidth=0.1, relheight=0.15)
        
        ###Criação do botão buscar
        self.btn_limpar = Button(self.frame_1, bg="#a30000", text="Buscar", font="Arial")
        self.btn_limpar.place(relx= 0.35, rely=0.1, relwidth=0.1, relheight=0.15)
        
        ###Criação do botão novo
        self.btn_limpar = Button(self.frame_1, bg="#a30000", text="Novo", font="Arial")
        self.btn_limpar.place(relx= 0.6, rely=0.1, relwidth=0.1, relheight=0.15)
        
        ###Criação do botão alterar
        self.btn_limpar = Button(self.frame_1, bg="#a30000", text="Alterar", font="Arial")
        self.btn_limpar.place(relx= 0.7, rely=0.1, relwidth=0.1, relheight=0.15)
        
        ###Criação do botão apagar
        self.btn_limpar = Button(self.frame_1, bg="#a30000", text="Apagar", font="Arial")
        self.btn_limpar.place(relx= 0.8, rely=0.1, relwidth=0.1, relheight=0.15)
        
        ###Criação da label e entrada do código
        self.label_codigo = Label(self.frame_1, text= "Código", bg="#c0c0c0")
        self.label_codigo.place(relx=0.05, rely=0.05)
        
        self.codigo_entry = Entry(self.frame_1)
        self.codigo_entry.place(relx=0.05, rely=0.15, relwidth=0.067)
        
        ###Criação da label e entrada do nome
        self.label_nome = Label(self.frame_1, text= "Nome", bg="#c0c0c0")
        self.label_nome.place(relx=0.05, rely=0.35)
        
        self.codigo_entry = Entry(self.frame_1)
        self.codigo_entry.place(relx=0.05, rely=0.45, relwidth=0.85)
        
        ###Criação da label e entrada do telefone
        self.label_nome = Label(self.frame_1, text= "Telefone", bg="#c0c0c0")
        self.label_nome.place(relx=0.05, rely=0.6)
        
        self.codigo_entry = Entry(self.frame_1)
        self.codigo_entry.place(relx=0.05, rely=0.7, relwidth=0.4)
        
        ###Criação da label e entrada da cidade
        self.label_nome = Label(self.frame_1, text= "Cidade", bg="#c0c0c0")
        self.label_nome.place(relx=0.5, rely=0.6)
        
        self.codigo_entry = Entry(self.frame_1)
        self.codigo_entry.place(relx=0.5, rely=0.7, relwidth=0.4)
        
Aplication()        
            
