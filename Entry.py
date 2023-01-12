from cgitb import text
from tkinter import *

raiz = Tk()

miFrame = Frame(raiz, width=1200, height=600)
miFrame.pack()

cuadroNombre = Entry(miFrame)
cuadroNombre.grid(row=0, column=1, sticky="w", padx=10, pady=10)

cuadroApellido = Entry(miFrame)
cuadroApellido.grid(row=1, column=1, sticky="w", padx=10, pady=10)

cuadroDireccion = Entry(miFrame)
cuadroDireccion.grid(row=2, column=1, sticky="w", padx=10, pady=10)

cuadroPass = Entry(miFrame)
cuadroPass.grid(row=3, column=1, sticky="w", padx=10, pady=10)
cuadroPass.config(show="*")

cuadroComentario = Text(miFrame)
cuadroComentario.grid(row=4, column=1, sticky="w", padx=10, pady=10)


scrollVert = Scrollbar(miFrame, command=cuadroComentario.yview)
scrollVert.grid(row=4, column=2, sticky="nswe")
cuadroComentario.config(yscrollcommand=scrollVert.set)

nombreLabel = Label(miFrame, text="Nombre: ")
nombreLabel.grid(row=0, column=0, sticky="w", padx=10, pady=10)

apellidoLabel = Label(miFrame, text="Apellido: ")
apellidoLabel.grid(row=1, column=0, sticky="w", padx=10, pady=10)

direccionLabel = Label(miFrame, text="Direccion: ")
direccionLabel.grid(row=2, column=0, sticky="w", padx=10, pady=10)

passLabel = Label(miFrame, text="Password: ")
passLabel.grid(row=3, column=0, sticky="w", padx=10, pady=10)

comentarioLabel = Label(miFrame, text="Comentario: ")
comentarioLabel.grid(row=4, column=0, sticky="w", padx=10, pady=10)

botonEnvio = Button(raiz, text="Enviar")
botonEnvio.pack()

raiz.mainloop()
