from tkinter import *


def sumar():
    r.set(float(n1.get()) + float(n2.get()))


ventana=Tk()
ventana.config(bd=15)

n1=StringVar()
n2=StringVar()
r=StringVar()

Label(ventana, text="Número 1").pack()
Entry(ventana, justify="center", textvariable=n1).pack()

Label(ventana, text="Número 2").pack()
Entry(ventana, justify="center", textvariable=n2).pack()

Label(ventana, text="Resultado").pack()
Entry(ventana, justify="center", textvariable=r).pack()

Button(ventana,text="Sumar", command=sumar).pack(side="left")

ventana.mainloop()

