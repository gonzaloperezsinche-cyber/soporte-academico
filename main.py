def mostrar_menu():
    print("\n=== SISTEMA DE SOPORTE ACADÉMICO ===")
    print("1. Registrar nueva solicitud")
    print("2. Salir")

def validar_codigo(codigo):
    return len(codigo.strip()) >= 4

def validar_tipo(tipo):
    tipos_validos = ["matricula", "pagos", "constancia", "plataforma", "otro"]
    return tipo.strip().lower() in tipos_validos

def validar_texto_obligatorio(texto):
    """Valida que un texto no esté vacío ni contenga solo espacios."""
    return len(texto.strip()) > 0

def calcular_prioridad(tipo):
    tipo_limpio = tipo.strip().lower()
    if tipo_limpio in ["matricula", "plataforma"]:
        return "Alta"
    elif tipo_limpio in ["pagos", "constancia"]:
        return "Media"
    else:
        return "Baja"

def mostrar_resumen(codigo, nombre, tipo, descripcion, prioridad):
    print("\n------------------------------------")
    print("      RESUMEN DE LA SOLICITUD       ")
    print("------------------------------------")
    print(f"Código del estudiante : {codigo}")
    print(f"Nombre del estudiante : {nombre}")
    print(f"Tipo de consulta     : {tipo}")
    print(f"Descripción          : {descripcion}")
    print(f"Prioridad asignada   : {prioridad}")
    print("------------------------------------\n")

def registrar_solicitud():
    print("\n--- REGISTRAR NUEVA SOLICITUD ---")
    
    codigo = input("Ingrese código de estudiante (mínimo 4 caracteres): ")
    while not validar_codigo(codigo):
        print("Error: Código no válido.")
        codigo = input("Ingrese código de estudiante (mínimo 4 caracteres): ")

    nombre = input("Ingrese nombre del estudiante: ")
    while not validar_texto_obligatorio(nombre):
        print("Error: El nombre no puede estar vacío.")
        nombre = input("Ingrese nombre del estudiante: ")

    print("Tipos válidos: matricula, pagos, constancia, plataforma, otro")
    tipo = input("Ingrese tipo de consulta: ")
    while not validar_tipo(tipo):
        print("Error: Tipo de consulta no válido.")
        tipo = input("Ingrese tipo de consulta: ")

    descripcion = input("Ingrese descripción breve: ")
    while not validar_texto_obligatorio(descripcion):
        print("Error: La descripción no puede estar vacía.")
        descripcion = input("Ingrese descripción breve: ")

    prioridad = calcular_prioridad(tipo)
    
    print("\n¡Solicitud registrada con éxito!")
    mostrar_resumen(codigo, nombre, tipo, descripcion, prioridad)

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            registrar_solicitud()
        elif opcion == "2":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()