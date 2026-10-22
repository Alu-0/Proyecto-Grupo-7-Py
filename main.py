
# Commit 3: Registro y validación de encomiendas
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
