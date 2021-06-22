from ClaseRepositorioProvinciasJSON import RespositorioProvincias
from Vista import ProvinciasView
from ClaseControlador import Controlador
from ObjectEncoder import ObjectEncoder

if __name__ == "__main__":
    conn = ObjectEncoder("provincias.json")
    repo = RespositorioProvincias(conn)
    vista = ProvinciasView()
    controlador = Controlador(repo, vista)
    vista.setControlador(controlador)
    controlador.Start()
    controlador.SalirGrabarDatos()
