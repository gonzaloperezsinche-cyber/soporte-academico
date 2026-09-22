def mostrar_menu():
    print("\n=== SISTEMA DE SOPORTE ACADÉMICO ===")
    print("1. Registrar nueva solicitud")
    print("2. Registrar múltiples solicitudes")
    print("3. Ver todas las solicitudes registradas")
    print("4. Ver estadísticas por prioridad")
    print("5. Salir")

def validar_codigo(codigo):
    return len(codigo.strip()) >= 4

def validar_tipo(tipo):
    tipos_validos = ["matricula", "pagos", "constancia", "plataforma", "otro"]
    return tipo.strip().lower() in tipos_validos

def validar_texto_obligatorio(texto):
    return len(texto.strip()) > 0

def calcular_prioridad(tipo):
    tipo_limpio = tipo.strip().lower()
    if tipo_limpio in ["matricula", "plataforma"]:
        return "Alta"
    elif tipo_limpio in ["pagos", "constancia"]:
        return "Media"
    else:
        return "Baja"

def mostrar_resumen(solicitud):
    print("\n------------------------------------")
    print("      RESUMEN DE LA SOLICITUD       ")
    print("------------------------------------")
    print(f"Código del estudiante : {solicitud['codigo']}")
    print(f"Nombre del estudiante : {solicitud['nombre']}")
    print(f"Tipo de consulta     : {solicitud['tipo']}")
    print(f"Descripción          : {solicitud['descripcion']}")
    print(f"Prioridad asignada   : {solicitud['prioridad']}")
    print("------------------------------------\n")

def registrar_solicitud(lista_solicitudes):
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
    
    solicitud = {
        "codigo": codigo,
        "nombre": nombre,
        "tipo": tipo,
        "descripcion": descripcion,
        "prioridad": prioridad
    }
    
    lista_solicitudes.append(solicitud)
    
    print("\n¡Solicitud registrada con éxito!")
    mostrar_resumen(solicitud)

def registrar_multiples_solicitudes(lista_solicitudes):
    print("\n--- REGISTRO DE MÚLTIPLES SOLICITUDES ---")
    
    cantidad_str = input("¿Cuántas solicitudes desea registrar? (mínimo 3): ")
    while not cantidad_str.isdigit() or int(cantidad_str) < 3:
        print("Error: Debe ingresar un número entero mayor o igual a 3.")
        cantidad_str = input("¿Cuántas solicitudes desea registrar? (mínimo 3): ")
    
    cantidad = int(cantidad_str)
    
    for i in range(1, cantidad + 1):
        print(f"\n>>> Registrando solicitud {i} de {cantidad} <<<")
        registrar_solicitud(lista_solicitudes)

def mostrar_todas_solicitudes(lista_solicitudes):
    if not lista_solicitudes:
        print("\nNo hay solicitudes registradas aún.")
        return

    print(f"\n=== HISTORIAL DE SOLICITUDES ({len(lista_solicitudes)}) ===")
    for idx, sol in enumerate(lista_solicitudes, 1):
        print(f"\nSolicitud #{idx}:")
        print(f"  Código    : {sol['codigo']}")
        print(f"  Nombre    : {sol['nombre']}")
        print(f"  Tipo      : {sol['tipo']}")
        print(f"  Prioridad : {sol['prioridad']}")

def mostrar_estadisticas_prioridad(lista_solicitudes):
    if not lista_solicitudes:
        print("\nNo hay solicitudes registradas para generar estadísticas.")
        return

    total = len(lista_solicitudes)
    alta = sum(1 for sol in lista_solicitudes if sol["prioridad"] == "Alta")
    media = sum(1 for sol in lista_solicitudes if sol["prioridad"] == "Media")
    baja = sum(1 for sol in lista_solicitudes if sol["prioridad"] == "Baja")

    print("\n=== ESTADÍSTICAS DE SOLICITUDES ===")
    print(f"Total de solicitudes registradas : {total}")
    print(f"  - Prioridad Alta  : {alta}")
    print(f"  - Prioridad Media : {media}")
    print(f"  - Prioridad Baja  : {baja}")
    print("====================================\n")

def main():
    solicitudes = []
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            registrar_solicitud(solicitudes)
        elif opcion == "2":
            registrar_multiples_solicitudes(solicitudes)
        elif opcion == "3":
            mostrar_todas_solicitudes(solicitudes)
        elif opcion == "4":
            mostrar_estadisticas_prioridad(solicitudes)
        elif opcion == "5":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()