from ClaseProvincia import Provincia

class ManejadorProvincias():
    indice = 0
    __Provincias = None

    def __init__(self):
        self.__Provincias = []

    def AgregarProvincia(self, provincia):
        provincia.rowid = ManejadorProvincias.indice
        ManejadorProvincias.indice +=1
        self.__Provincias.append(provincia)

    def EliminarProvincia(self, provincia):
        indice = self.obtenerIndiceProvincia(provincia)
        self.__Provincias.pop(indice)

    def UpdateProvincia(self, provincia):
        indice = self.obtenerIndiceProvincia(provincia)
        self.__Provincias[indice] = provincia

    def GetListaProvincias(self):
        return (self.__Provincias)

    def obtenerIndiceProvincia(self, provincia):
        bandera = False
        i = 0
        while not bandera and i < len(self.__Provincias):
            if self.__Provincias[i].rowid == provincia.rowid:
                bandera = True
            else:
                i += 1
        return (i)

    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            provincias=[provincia.toJSON() for provincia in self.__Provincias]
            )
        return d
