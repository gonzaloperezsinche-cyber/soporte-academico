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

def main():
    mostrar_menu()

if __name__ == "__main__":
    main()