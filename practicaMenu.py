from _tkinter import *
from tkinter import Menu, Tk
from tkinter import messagebox

root = Tk()


def infoAdicional():
    messagebox.showinfo("Procesasdor de Juan", "Procesador de textos version")


def avisoLicencia():
    messagebox.showwarning("licencia", "Producto bajo licencia GNU")


def avisoSalir():
    #valor = messagebox.askquestion("Salir", "Deseas salir de la apllicacion?")
    valor = messagebox.askokcancel("Salir", "Deseas salir de la apllicacion?")

    if valor == True:
        root.destroy()


def cerrarDocumento():
    valor = messagebox.askretrycancel(
        "reintentar", "No es posible cerrar el documento. Documento bloqueado")

    if valor == False:
        root.destroy()


barraMenu = Menu(root)
root.config(menu=barraMenu, width=300, height=300)


archivoMenu = Menu(barraMenu, tearoff=0)
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Guardar como")
archivoMenu.add_separator()
archivoMenu.add_command(label="Cerrar", command=cerrarDocumento)
archivoMenu.add_command(label="Salir", command=avisoSalir)


archivoEdicion = Menu(barraMenu, tearoff=0)
archivoEdicion.add_command(label="Copiar")
archivoEdicion.add_command(label="Cortar")
archivoEdicion.add_command(label="Pegar")


archivoHerramientas = Menu(barraMenu, tearoff=0)

archivoAyuda = Menu(barraMenu, tearoff=0)
archivoAyuda.add_command(label="Licencia", command=avisoLicencia)
archivoAyuda.add_command(label="Acerca de...", command=infoAdicional)


barraMenu.add_cascade(label="Archivo", menu=archivoMenu)

barraMenu.add_cascade(label="Edicion", menu=archivoEdicion)

barraMenu.add_cascade(label="Herramientas", menu=archivoHerramientas)

barraMenu.add_cascade(label="Ayuda", menu=archivoAyuda)


root.mainloop()
