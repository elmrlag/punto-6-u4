import urllib, json
from urllib.request import urlopen

class Provincia():
    __nombre = ""
    __capital = ""
    __cantHabitantes = 0
    __cantDepPar = 0
    __temperatura = 0
    __sensacion = 0
    __humedad = 0

    def __init__(self, nombre, capital, cantHabitantes, cantDepPar, temperatura = 0, sensacion = 0, humedad = 0):
        self.__nombre = self.requerido(nombre, "Se necesita un nombre de provincia")
        self.__capital = self.requerido(capital, "se necesita el nombre de la capital")
        self.__cantHabitantes = self.requerido(cantHabitantes, "se necesita la cantidad de habitantes")
        self.__cantDepPar = self.requerido(cantDepPar, "se necesita la cantidad de departamentos/partidos")
        self.__temperatura = temperatura
        self.__sensacion = sensacion
        self.__humedad = humedad

    def requerido(self, valor, mensaje):
        if not valor:
            raise ValueError(mensaje)
        return valor

    def GetNombre(self):
        return (self.__nombre)

    def GetCapital(self):
        return (self.__capital)

    def GetCantHabitantes(self):
        return (self.__cantHabitantes)

    def GetCantDepPar(self):
        return (self.__cantDepPar)

    def GetTemp(self):
        ciudad = str(self.__nombre)
        url = "https://api.openweathermap.org/data/2.5/weather?q="+ciudad+"&units=metric&appid=d655ddfa293902bae611a63a77da7351"
        url = url.replace(" ", "%20")
        response = urlopen(url)
        data = json.loads(response.read())
        temp = data["main"]["temp"]
        return (temp)

    def GetSens(self):
        url = str("https://api.openweathermap.org/data/2.5/weather?q="+self.__nombre+"&units=metric&appid=d655ddfa293902bae611a63a77da7351")
        url = url.replace(" ", "%20")
        response = urlopen(url)
        data = json.loads(response.read())
        sens = data["main"]["feels_like"]
        return (sens)

    def GetHumed(self):
        url = str("https://api.openweathermap.org/data/2.5/weather?q="+self.__nombre+"&units=metric&appid=d655ddfa293902bae611a63a77da7351")
        url = url.replace(" ", "%20")
        response = urlopen(url)
        data = json.loads(response.read())
        humed = data["main"]["humidity"]
        return (humed)


    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                nombre=self.__nombre,
                capital=self.__capital,
                cantHabitantes=self.__cantHabitantes,
                cantDepPar=self.__cantDepPar,
                temperatura=self.__temperatura,
                sensacion=self.__sensacion,
                humedad=self.__humedad
            )
        )
        return d