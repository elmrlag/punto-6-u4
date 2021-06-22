from ClaseManejadorProvincias import ManejadorProvincias
from Vista import ProvinciasList, ProvinciasView, NuevaProvincia

class Controlador():

    def __init__(self, repo, vista):
        self.repo = repo
        self.vista = vista
        self.seleccion = -1
        self.provincias = list(repo.ObtenerListaProvincias())

    # comandos que se ejecutan a través de la vista
    def CrearProvincia(self):
        nuevaProvincia = NuevaProvincia(self.vista).show()
        if nuevaProvincia:
            provincia = self.repo.AgregarProvincia(nuevaProvincia)
            self.provincias.append(provincia)
            self.vista.agregarProvincia(provincia)

    def SeleccionarProvincia(self, index):
        self.seleccion = index
        provincia = self.provincias[index]
        self.vista.verProvinciaEnForm(provincia)

    def ModificarProvincia(self):
        if self.seleccion == -1:
            return
        rowid = self.provincias[self.seleccion].rowid
        DetallesProvincia = self.vista.obtenerDetalles()
        DetallesProvincia.rowid = rowid
        provincia = self.repo.ModificarProvincia(DetallesProvincia)
        self.provincias[self.seleccion] = provincia
        self.vista.modificarProvincia(provincia, self.seleccion)
        self.seleccion = -1

    def BorrarProvincia(self):
        if self.seleccion == -1:
            return
        provincia = self.provincias[self.seleccion]
        self.repo.BorrarProvincia(provincia)
        self.provincias.pop(self.seleccion)
        self.vista.borrarProvincia(self.seleccion)
        self.seleccion = -1

    def Start(self):
        for p in self.provincias:
            self.vista.agregarProvincia(p)
        self.vista.mainloop()

    def SalirGrabarDatos(self):
        self.repo.GrabarDatos()
