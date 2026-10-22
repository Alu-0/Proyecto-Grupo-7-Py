
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


def guardar():
    with open(archivo, "w", encoding="utf-8") as f:
        for e in encomiendas:
            f.write(f"{e['dni']}|{e['codigo']}|{e['estado']}\n")


def registrar():
    dni = input("DNI (8 dígitos): ").strip()
    codigo = input("Código (mín. 4 caracteres): ").strip()

    if not dni.isdigit() or len(dni) != 8:
        print("El DNI debe tener exactamente 8 números.")
        return

    if len(codigo) < 4 or "|" in codigo:
        print("El código debe tener al menos 4 caracteres y no contener '|'.")
        return

    if any(e["codigo"].upper() == codigo.upper() for e in encomiendas):
        print("El código ya está registrado.")
        return

    encomiendas.append({
        "dni": dni,
        "codigo": codigo,
        "estado": "Registrado"
    })

    guardar()
    print("¡Encomienda registrada y guardada!")


def buscar():
    codigo = input("Ingrese el código: ").strip()

    for e in encomiendas:
        if e["codigo"].upper() == codigo.upper():
            print(
                f"\nEncontrado -> DNI: {e['dni']} | "
                f"Código: {e['codigo']} | Estado: {e['estado']}"
            )
            return

    print("No se encontró la encomienda.")


def actualizar():
    codigo = input("Ingrese el código de seguimiento: ").strip()

    for e in encomiendas:
        if e["codigo"].upper() == codigo.upper():
            print(f"Estado actual: {e['estado']}")

            if input("¿Marcar como Entregado? (S/N): ").strip().upper() == "S":
                e["estado"] = "Entregado"
                guardar()
                print("¡Estado actualizado y guardado!")
            else:
                print("No se realizaron cambios.")

            return

    print("No se encontró la encomienda.")


def mostrar():
    if not encomiendas:
        print("No hay registros.")
        return

    print("\n<<< LISTA DE ENCOMIENDAS >>>")

    for i, e in enumerate(encomiendas, 1):
        print(
            f"{i}. DNI: {e['dni']} | "
            f"Código: {e['codigo']} | Estado: {e['estado']}"
        )


def ordenar():
    if not encomiendas:
        print("No hay registros para ordenar.")
        return

    encomiendas.sort(key=lambda x: x["codigo"].lower())
    guardar()

    print("¡Encomiendas ordenadas por código!")
    mostrar()


cargar()
