# Mini-Proyecto: Explorador de Directorios

class ExploradorRecursivo:

    # Muestra el árbol con sangrías
    def imprimir_arbol(self, sistema, nivel=0):
        for nombre, contenido in sistema.items():
            if isinstance(contenido, dict):  # es una carpeta
                print("    " * nivel + nombre + "/")
                self.imprimir_arbol(contenido, nivel + 1)
            else:  # es un archivo
                print("    " * nivel + nombre + " (" + contenido + ")")

    # Busca la ruta de un archivo (devuelve None si no existe)
    def buscar_archivo(self, sistema, nombre):
        for clave, contenido in sistema.items():
            if isinstance(contenido, dict):
                ruta = self.buscar_archivo(contenido, nombre)
                if ruta is not None:
                    return clave + "/" + ruta
            elif clave == nombre:
                return clave
        return None

    # Cuenta los archivos (las carpetas no cuentan)
    def contar_archivos(self, sistema):
        total = 0
        for contenido in sistema.values():
            if isinstance(contenido, dict):
                total += self.contar_archivos(contenido)
            else:
                total += 1
        return total


sistema_archivos = {
    "Documentos": {
        "apuntes.txt": "10kb",
        "fotos": {
            "vacaciones.png": "2mb",
            "perro.jpg": "1mb"
        }
    },
    "sistema.dll": "500kb"
}

explorador = ExploradorRecursivo()

print("Árbol de archivos:")
explorador.imprimir_arbol(sistema_archivos)

print("\nBuscar archivos:")
print(explorador.buscar_archivo(sistema_archivos, "perro.jpg"))
print(explorador.buscar_archivo(sistema_archivos, "sistema.dll"))
print(explorador.buscar_archivo(sistema_archivos, "nada.txt"))

print("\nTotal de archivos:")
print(explorador.contar_archivos(sistema_archivos))
