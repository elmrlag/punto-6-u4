import tkinter as tk
from tkinter import messagebox
from ClaseProvincia import Provincia

class ProvinciasList(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master)
        self.lb = tk.Listbox(self, **kwargs)
        scroll = tk.Scrollbar(self, command=self.lb.yview)
        self.lb.config(yscrollcommand=scroll.set)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.lb.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

    def insertar(self, provincia, index=tk.END):
        text = (f"{provincia.GetNombre()}")
        self.lb.insert(index, text)

    def borrar(self, index):
        self.lb.delete(index, index)

    def modificar(self, contact, index):
        self.borrar(index)
        self.insertar(contact, index)

    def bind_doble_click(self, callback):
        handler = lambda _: callback(self.lb.curselection()[0])
        self.lb.bind("<Double-Button-1>", handler)



class FormularioProvincia(tk.LabelFrame):
    fields = ("Nombre", "Capital", "cantHabitantes", "cantDepPar", "Temperatura", "Sensación Térmica", "Humedad")

    def __init__(self, master, ** kwargs):
        super().__init__(master, text="DATOS DE PROVINCIA", padx=10, pady=10, **kwargs)
        self.frame = tk.Frame(self)
        self.entries = list(map(self.crearCampo, enumerate(self.fields)))
        self.frame.pack()

    def crearCampo(self, field):
        position, text = field
        label = tk.Label(self.frame, text = text)
        entry = tk.Entry(self.frame, width = 25)
        label.grid(row = position, column = 0, pady = 5)
        entry.grid(row = position, column = 1, pady = 5)
        return entry

    def mostrarEstadoProvinciaEnFormulario(self, provincia):
        # a partir de una provincia, obtiene el estado y establece en los valores en el formulario de entrada
        values = (provincia.GetNombre(), provincia.GetCapital(), provincia.GetCantHabitantes(), provincia.GetCantDepPar(), provincia.GetTemp(), provincia.GetSens(), provincia.GetHumed())
        for entry, value in zip(self.entries, values):
            entry.delete(0, tk.END)
            entry.insert(0, value)

    def CrearProvincia(self):
        values = [e.get() for e in self.entries]
        provincia = None
        try:
            provincia = Provincia(*values)
        except ValueError as e:
            messagebox.showerror("Error de validación", str(e), parent = self)
        return provincia

    def CrearProvinciaDesdeFormulario(self):
        # obtiene los valores de los campos del formulario
        # para crear una nueva provincia
        values = [e.get() for e in self.entries]
        provincia = None
        try:
            provincia = Provincia(*values)
        except ValueError as e:
            messagebox.showerror("Error de Validación", str(e), parent=self)
        return provincia

    def limpiar(self):
        for entry in self.entries:
            entry.delete(0, tk.END)



class NuevaProvincia(tk.Toplevel):

    def __init__(self, parent):
        super().__init__(parent)
        self.provincia = None
        self.form = FormularioProvincia(self)
        self.btn_add = tk.Button(self, text="Confirmar", command=self.confirmar)
        self.form.pack(padx=10, pady=10)
        self.btn_add.pack(pady=10)

    def confirmar(self):
        self.provincia = self.form.CrearProvinciaDesdeFormulario()
        if self.provincia:
            self.destroy()

    def show(self):
        self.grab_set()
        self.wait_window()
        return self.provincia


class UpdateFormularioProvincias(FormularioProvincia):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.btn_save = tk.Button(self, text="Guardar")
        self.btn_delete = tk.Button(self, text="Borrar")
        self.btn_save.pack(side=tk.RIGHT, ipadx=5, padx=5, pady=5)
        self.btn_delete.pack(side=tk.RIGHT, ipadx=5, padx=5, pady=5)

    def bind_save(self, callback):
        self.btn_save.config(command=callback)

    def bind_delete(self, callback):
        self.btn_delete.config(command=callback)



class ProvinciasView(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Lista de Provincias")
        self.list = ProvinciasList(self, height=15)
        self.form = UpdateFormularioProvincias(self)
        self.btn_new = tk.Button(self, text="Agregar Provincia")
        self.list.pack(side=tk.LEFT, padx=10, pady=10)
        self.form.pack(padx=10, pady=10)
        self.btn_new.pack(side=tk.BOTTOM, pady=5)

    def setControlador(self, ctrl):
        #vincula la vista con el controlador
        self.btn_new.config(command=ctrl.CrearProvincia)
        self.list.bind_doble_click(ctrl.SeleccionarProvincia)
        self.form.bind_save(ctrl.ModificarProvincia)
        self.form.bind_delete(ctrl.BorrarProvincia)

    def agregarProvincia(self, provincia):
        self.list.insertar(provincia)

    def modificarProvincia(self, provincia, index):
        self.list.modificar(provincia, index)

    def borrarProvincia(self, index):
        self.form.limpiar()
        self.list.borrar(index)

    #obtiene los valores del formulario y crea una nueva provincia
    def obtenerDetalles(self):
        return self.form.CrearProvinciaDesdeFormulario()

 #Ver estado de Contacto en formulario de contactos
    def verProvinciaEnForm(self, provincia):
        self.form.mostrarEstadoProvinciaEnFormulario(provincia)
