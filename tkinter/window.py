from tkinter import *
from tkinter import ttk


window = Tk()

class App():
    
    def __init__(self):
        self.janela = window
        self.screen()
        self.frames()
        self.buttons()
        self.labels()
        self.inputs()
        self.frame2_list()
        window.mainloop()
        
    def screen(self):
        self.janela.title('NETFLIX')
        self.janela.configure (background='#bdbcb3')      
        self.janela.geometry('800x600')
        self.janela.resizable(False, False)
        self.janela.maxsize(width=800, height=600)
        
    def frames(self):
        self.frame0 = Frame(self.janela, bg='gray')
        self.frame0.place(relx= 0.03, rely= 0.03, relwidth= 0.94, relheight=0.11)
        
        self.frame1 = Frame(self.janela, bg='gray')
        self.frame1.place(relx= 0.03, rely= 0.20, relwidth= 0.94, relheight=0.25)
        
        self.frame2 = Frame(self.janela, bg='gray')
        self.frame2.place(relx= 0.03, rely= 0.50, relwidth= 0.94, relheight=0.45)
    
    def buttons(self):
        self.button_search = Button(self.frame0, text= 'Search')
        self.button_search.place(relx=0.15, rely=0.40, relwidth=0.1, relheight=0.5)
        
        self.button_clear = Button(self.frame0, text='Clear')
        self.button_clear.place(relx=0.27, rely=0.40, relwidth=0.1, relheight=0.5)
        
        self.button_Create = Button(self.frame0, text='Create')
        self.button_Create.place(relx=0.45, rely=0.40, relwidth=0.1, relheight=0.5)
        
        self.button_Read = Button(self.frame0, text='Read')
        self.button_Read.place(relx=0.57, rely=0.40, relwidth=0.1, relheight=0.5)
        
        self.button_Update = Button(self.frame0, text='Update')
        self.button_Update.place(relx=0.69, rely=0.40, relwidth=0.1, relheight=0.5)
        
        self.button_Delete = Button(self.frame0, text='Delete')
        self.button_Delete.place(relx=0.81, rely=0.40, relwidth=0.1, relheight=0.5)
    
    def labels(self):
        self.labelUser = Label(self.frame0, text='ID', bg='gray')
        self.labelUser.place(relx=0.005, rely=0.01, relwidth=0.1, relheight=0.3)
        
        self.labelName = Label(self.frame1, text='Name', bg='gray')
        self.labelName.place(relx=0.005, rely=0.06, relwidth=0.1, relheight=0.15)
        
        self.labelEmail = Label(self.frame1, text='Email', bg='gray')
        self.labelEmail.place(relx=0.005, rely=0.37, relwidth=0.1, relheight=0.15)
        
        self.labelPlan = Label(self.frame1, text='Plan', bg='gray')
        self.labelPlan.place(relx=0.005, rely=0.69, relwidth=0.1, relheight=0.15)
        
        self.labelType = Label(self.frame1, text='Type', bg='gray')
        self.labelType.place(relx=0.32, rely=0.69, relwidth=0.1, relheight=0.15)
        
        self.labelAge = Label(self.frame1, text='Age', bg='gray')
        self.labelAge.place(relx=0.62, rely=0.69, relwidth=0.1, relheight=0.15)
        
    def inputs(self):
        self.imputIDUSer = Entry(self.frame0)
        self.imputIDUSer.place(relx=0.02, rely=0.37, relwidth=0.1, relheight=0.5)
        
        self.imputName = Entry(self.frame1)
        self.imputName.place(relx=0.12, rely=0.05, relwidth=0.8, relheight=0.25)
        
        self.imputEmail = Entry(self.frame1)
        self.imputEmail.place(relx=0.12, rely=0.35, relwidth=0.8, relheight=0.25)
        
        self.imputPlan = Entry(self.frame1)
        self.imputPlan.place(relx=0.12, rely=0.65, relwidth=0.2, relheight=0.25)
        
        self.imputType = Entry(self.frame1)
        self.imputType.place(relx=0.425, rely=0.65, relwidth=0.2, relheight=0.25)
        
        self.imputAge = Entry(self.frame1)
        self.imputAge.place(relx=0.72, rely=0.65, relwidth=0.2, relheight=0.25)
        
    def frame2_list(self):
        self.clientList = ttk.Treeview(self.frame2, height=3, columns=('column1', 'column2', 'column3', 'column4', 'column5'))#Faixa onde ficam os nomes dentro do frame 02
        self.clientList.heading('#0', text='ID')
        self.clientList.heading('#1', text='Name')
        self.clientList.heading('#2', text='Email')
        self.clientList.heading('#3', text='Plan')
        self.clientList.heading('#4', text='Type')
        self.clientList.heading('#5', text='Age')
        
        self.clientList.column('#0', width=35)
        self.clientList.column('#1', width=188)
        self.clientList.column('#2', width=188)
        self.clientList.column('#3', width=70)
        self.clientList.column('#4', width=70)
        self.clientList.column('#5', width=70)
        
        self.clientList.place(relx=0.01, rely=0.1, relwidth=0.98, relheight=0.85)
        
        self.scrolList = Scrollbar(self.frame2, orient='vertical')
        self.clientList.configure(yscrollcommand=self.scrolList.set)   
        self.scrolList.place(relx=0.96, rely=0.1, relwidth=0.04, relheight=0.85)   
        