from tkinter import *

ventana=Tk()
ventana.config(width=300,height=200)
ventana.title("UGTO")
ventana.iconbitmap('UGTO.ico')

frame=Frame(ventana,width=200,height=200)
frame.pack(side=RIGHT)
frame.pack(anchor=N)
frame.config(bg="lightblue")
#frame.config(width=100,height=100)

ventana.mainloop()