from _tkinter import *
from cProfile import label
from tkinter import Frame, Tk

raiz = Tk()

raiz.title("Ventana de Pruebas")

raiz.config(bg="light blue")

miFrame = Frame(raiz, width=500, height=400)

miFrame.pack()
label(miFrame, text="Hola alumnos de python",
      fg="black", font=(14)).place(x=100, y=200)
#milabel = label(miFrame, text="Hola alumnos de python")
#milabel.place(x=100, y=200)

miImage = PhotoImage(file)


raiz.mainloop()
