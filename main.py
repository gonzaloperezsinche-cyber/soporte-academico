def mostrar_menu():
    print("\n=== SISTEMA DE SOPORTE ACADÉMICO ===")
    print("1. Registrar nueva solicitud")
    print("2. Salir")

def validar_codigo(codigo):
    longitud_minima = 4
    if len(codigo.strip()) >= longitud_minima:
        return True
    return False

def validar_tipo(tipo):
    tipos_validos = ["matricula", "pagos", "constancia", "plataforma", "otro"]
    if tipo.strip().lower() in tipos_validos:
        return True
    return False

def calcular_prioridad(tipo):
    tipo_limpio = tipo.strip().lower()
    if tipo_limpio in ["matricula", "plataforma"]:
        return "Alta"
    elif tipo_limpio in ["pagos", "constancia"]:
        return "Media"
    else:
        return "Baja"

def registrar_solicitud():
    print("\n--- REGISTRAR NUEVA SOLICITUD ---")
    
    codigo = input("Ingrese código de estudiante (mínimo 4 caracteres): ")
    while not validar_codigo(codigo):
        print("Error: El código debe tener al menos 4 caracteres.")
        codigo = input("Ingrese un código válido: ")
    
    print("Tipos válidos: matricula, pagos, constancia, plataforma, otro")
    tipo = input("Ingrese tipo de consulta: ")
    while not validar_tipo(tipo):
        print("Error: Tipo de consulta no válido.")
        tipo = input("Ingrese un tipo válido: ")
        
    prioridad = calcular_prioridad(tipo)
    
    print("\n¡Solicitud registrada con éxito!")
    print(f"Código: {codigo.strip()}")
    print(f"Tipo: {tipo.strip().lower()}")
    print(f"Prioridad asignada: {prioridad}")

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