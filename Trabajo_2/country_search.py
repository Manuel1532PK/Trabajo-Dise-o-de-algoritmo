import lib_Request

paises = lib_Request.obtener_pais()

paises_ordenados = sorted(paises, key=lambda x: x["name"]["common"])

if paises:    
    print("Búsqueda de países de Europa")
    print("1. Búsqueda Lineal")
    print("2. Búsqueda Binaria")
        
    opcion = input("Seleccione el tipo de búsqueda (1 o 2): ")
    nombre = input("Ingrese el nombre del país: ")
        
    if opcion == "1":
        resultado = lib_Request.busqueda_lineal(paises, nombre)
    elif opcion == "2":
        resultado = lib_Request.busqueda_binaria(paises, nombre)
    else:
        print("Opción inválida.")
        resultado = None
        
    if resultado:
        print("\nPaís encontrado:")
        print("Nombre:", resultado["name"]["official"])
        print("Mapa:", resultado["maps"]["googleMaps"])
    else:
        print("País no encontrado en la lista.")    