from tkinter import *

ventana=Tk()
ventana.config(width=300,height=200)
ventana.title("UGTO")
ventana.iconbitmap('UGTO.ico')

label= Label(ventana, text="Numero1")
label.grid(row=0, column=0, sticky="w", padx=5, pady=5)

entry=Entry(ventana)
entry.grid(row=0, column=1, padx=5, pady=5)
entry.config(justify="right",state="normal")

label2= Label(ventana, text="Nombre de Alumno")
label2.grid(row=1, column=0, sticky="w", padx=5, pady=5)

entry2=Entry(ventana)
entry2.grid(row=1, column=1, padx=5, pady=5)
entry2.config(justify="right",state="normal")

btn=Button(ventana,text="Saludo")
btn.grid(row=2, column=1, padx=5, pady=5)
ventana.mainloop();