import json
import simplejson
from pathlib import Path
from ClaseManejadorProvincias import ManejadorProvincias
from ClaseProvincia import Provincia

class ObjectEncoder(object):
    __pathArchivo = None

    def __init__(self, pathArchivo):
        self.__pathArchivo = pathArchivo

    def decodificadorDiccionario(self, d):
        if "__class__" not in d:
            return (d)
        else:
            NombreClase = d["__class__"]
            class_ = eval(NombreClase)
            if (NombreClase == "ManejadorProvincias"):
                provincias = d["provincias"]
                manejador = class_()
                for i in range(len(provincias)):
                    dProvincia = provincias[i]
                    NombreClase = dProvincia.pop("__class__")
                    class_ = eval(NombreClase)
                    atributos = dProvincia["__atributos__"]
                    UnaProvincia = class_(**atributos)
                    manejador.AgregarProvincia(UnaProvincia)
                return manejador

    def GuardarJSONArchivo(self, diccionario):
        with Path(self.__pathArchivo).open("w", encoding = "UTF-8") as destino:
            json.dump(diccionario, destino, indent = 4)
            destino.close()

    def leerJSONArchivo(self):
        with Path(self.__pathArchivo).open(encoding = "UTF-8") as fuente:
            diccionario = json.load(fuente)
            fuente.close()
            return (diccionario)