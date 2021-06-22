from ClaseProvincia import Provincia
from ObjectEncoder import ObjectEncoder
from ClaseManejadorProvincias import ManejadorProvincias

class RespositorioProvincias(object):
    __conn = None
    __manejador = None

    def __init__(self, conn):
        self.__conn = conn
        diccionario = self.__conn.leerJSONArchivo()
        self.__manejador = self.__conn.decodificadorDiccionario(diccionario)

    def ObtenerListaProvincias(self):
        return self.__manejador.GetListaProvincias()

    def AgregarProvincia(self, Provincia):
        self.__manejador.AgregarProvincia(Provincia)
        return Provincia

    def ModificarProvincia(self, Provincia):
        self.__manejador.UpdateProvincia(Provincia)
        return Provincia

    def BorrarProvincia(self, Provincia):
        self.__manejador.EliminarProvincia(Provincia)

    def GrabarDatos(self):
        self.__conn.GuardarJSONArchivo(self.__manejador.toJSON())
