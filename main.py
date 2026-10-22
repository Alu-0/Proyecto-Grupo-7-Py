
# Commit 4: Búsqueda, actualización y muestra de registros

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
