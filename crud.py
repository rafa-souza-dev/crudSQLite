from tkinter import *
from database import *


def confirmar():
    n = ed1.get()
    t = ed2.get()
    e = ed3.get()
    d = ed4.get()
    inserir(n, t, e, d)

    lb['text'] = 'Cadastrado com sucesso! :D'
    lb['foreground'] = 'blue'


crud = Tk()

crud.geometry('1300x1000+0+0')
crud.title('Cadastro')

lb = Label(crud, text='Aguardando...')
lb.place(x=15, y=450)

lb1 = Label(crud, text='CADASTRAMENTO', fg='blue', font=('arial', 40, 'bold'))
lb1.pack(side=TOP)

lb2 = Label(crud, text='Nome: ', font=('arial', 15))
lb3 = Label(crud, text='Telefone: ', font=('arial', 15))
lb4 = Label(crud, text='E-mail: ', font=('arial', 15))
lb5 = Label(crud, text='Data do Cadastro: ', font=('arial', 15))
lb6 = Label(crud, text='Bem vindo!!!', font=('arial', 20, 'bold'))
lb7 = Label(crud, text='Informe os dados a seguir...', font=('arial', 20, 'bold'))

b1 = Button(crud, width=30, text='Confirmar', font=('arial'), command=confirmar)

lb6.place(x=10, y=100)
lb7.place(x=10, y=130)

lb2.place(x=10, y=250)
lb3.place(x=10, y=300)
lb4.place(x=10, y=350)
lb5.place(x=10, y=400)

ed1 = Entry(crud, width=50)
ed2 = Entry(crud, width=50)
ed3 = Entry(crud, width=50)
ed4 = Entry(crud, width=50)

ed1.place(x=200, y=255)
ed2.place(x=200, y=305)
ed3.place(x=200, y=355)
ed4.place(x=200, y=405)

b1.place(x=100, y=500)
