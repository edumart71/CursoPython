from tkinter import ttk
import tkinter as tk


ventana=tk.Tk()
ventana.config(width=300,height=200)
ventana.title("UGTO")
ventana.iconbitmap('UGTO.ico')
combo=ttk.Combobox()
combo.place(x=50,y=50)
ventana.mainloop()