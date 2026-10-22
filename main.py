
import os

archivo = "encomiendas.txt"
encomiendas = []

def cargar():
    if os.path.exists(archivo):
        with open(archivo, "r", encoding="utf-8") as f:
            for linea in f:
                datos = linea.strip().split("|")
                if len(datos) == 3:
                    encomiendas.append({
                        "dni": datos[0],
                        "codigo": datos[1],
                        "estado": datos[2]
                    })
