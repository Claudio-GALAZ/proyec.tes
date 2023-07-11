departamentos = [['D' for _ in range(4)] for _ in range(10)]  # Matriz para almacenar el estado de los departamentos
ganancias_totales = 0  # Variable para almacenar las ganancias totales

def main():
    while True:
        print("Bienvenido a la Inmobiliaria Casa Feliz")
        print("Seleccione una opción:")
        print("1. Comprar departamento")
        print("2. Mostrar departamentos disponibles")
        print("3. Ver listado de compradores")
        print("4. Mostrar ganancias totales")
        print("5. Salir")

        opcion = input()

        if opcion == '1':
            comprar_departamento()
        elif opcion == '2':
            mostrar_departamentos_disponibles()
        elif opcion == '3':
            ver_listado_compradores()
        elif opcion == '4':
            mostrar_ganancias_totales()
        elif opcion == '5':
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

        print()

def comprar_departamento():
    global departamentos, ganancias_totales
    print("Departamentos disponibles:")
    mostrar_departamentos_disponibles()

    print("Ingrese el número de piso (1-10):")
    piso = int(input())
    if piso < 1 or piso > 10:
        print("\nNúmero de piso inválido. Por favor, ingrese un número de piso válido (1-10).")
        return

    print("Ingrese el tipo de departamento (A, B, C, D):")
    tipo = input().upper()
    if tipo not in ['A', 'B', 'C', 'D']:
        print("\nTipo de departamento inválido. Por favor, ingrese un tipo válido (A, B, C, D).")
        return

    fila = piso - 1
    columna = tipo_departamento_to_columna(tipo)

    if departamentos[fila][columna] == 'X':
        print("\nEl departamento seleccionado ya está vendido. Por favor, elija otro departamento.")
    else:
        departamentos[fila][columna] = 'X'
        precio = calcular_precio_departamento(piso, tipo)
        ganancias_totales += precio
        print(f"\n¡Departamento {tipo}{piso} comprado con éxito! Precio: ${precio}")

def mostrar_departamentos_disponibles():
    print("Estado de los departamentos:")
    print("Piso\tTipo\tEstado")

    for piso in range(1, 11):
        for tipo in range(4):
            estado = 'V' if departamentos[piso - 1][tipo] == 'X' else 'D'
            print(f"{piso}\t{(chr(ord('A') + tipo))}\t{estado}")

def ver_listado_compradores():
    print("Listado de compradores:")

    for piso in range(1, 11):
        for tipo in range(4):
            if departamentos[piso - 1][tipo] == 'X':
                print(f"Departamento {(chr(ord('A') + tipo))}{piso}")

def mostrar_ganancias_totales():
    print(f"Ganancias totales: ${ganancias_totales}")

def tipo_departamento_to_columna(tipo):
    return ord(tipo) - ord('A')

def calcular_precio_departamento(piso, tipo):
    # Aquí puedes implementar tu lógica para calcular el precio del departamento en base al piso y tipo
    # En este ejemplo, el precio se calcula sumando el número de piso y el valor ASCII del tipo de departamento
    return piso + ord(tipo)

if _name_ == '_main_':
    main()