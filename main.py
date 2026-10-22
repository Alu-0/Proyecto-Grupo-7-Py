
import os

archivo = "encomiendas.txt"
encomiendas = []


# Commit 1: Carga y lectura del archivo de datos
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


# Commit 2: Guardado de datos en el archivo
def guardar():
    with open(archivo, "w", encoding="utf-8") as f:
        for e in encomiendas:
            f.write(f"{e['dni']}|{e['codigo']}|{e['estado']}\n")
