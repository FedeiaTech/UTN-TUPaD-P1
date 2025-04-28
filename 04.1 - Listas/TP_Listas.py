def actividad_1():
    """Crea una lista con los números del 1 al 100 que sean múltiplos de 4"""
    multiplos_de_4 = list(range(4, 101, 4))
    print("Actividad 1:", multiplos_de_4)

def actividad_2():
    """Crea una lista con cinco elementos y muestra el penúltimo"""
    mi_lista = ["manzana", "banana", "naranja", "pera", "uva"]
    penultimo = mi_lista[-2]
    print("Actividad 2:", mi_lista)
    print("El penúltimo elemento es:", penultimo)

def actividad_3():
    """Crea una lista vacía, agrega tres palabras e imprime la lista"""
    lista_vacia = []
    lista_vacia.append("hola")
    lista_vacia.append("mundo")
    lista_vacia.append("python")
    print("Actividad 3:", lista_vacia)

def actividad_4():
    """Reemplaza el segundo y último valor de la lista 'animales'"""
    animales = ["perro", "gato", "conejo", "pez"]
    animales[1] = "loro"
    animales[-1] = "oso"
    print("Actividad 4:", animales)

def actividad_5():
    numeros = [8, 15, 3, 22, 7]
    numeros.remove(max(numeros))
    print(numeros)
    print("\nEl programa realiza las siguientes acciones:\n*   Inicializa una lista llamada numeros\n*   Encuentra el número más grande en la lista\n*   Elimina la primera ocurrencia del número más grande\n*   Imprime la lista resultante")

def actividad_6():
    """Crea una lista con números del 10 al 30 (saltos de 5) y muestra los dos primeros"""
    lista_saltos = list(range(10, 31, 5))
    dos_primeros = lista_saltos[:2]
    print("Actividad 6:", lista_saltos)
    print("Los dos primeros elementos son:", dos_primeros)

def actividad_7():
    """Reemplaza los dos valores centrales de la lista 'autos'"""
    autos = ["sedan", "polo", "suran", "gol"]
    autos[1:3] = ["fiesta", "corsa"]
    print("Actividad 7:", autos)

def actividad_8():
    """Crea una lista vacía y agrega el doble de 5, 10 y 15"""
    dobles = []
    dobles.append(5 * 2)
    dobles.append(10 * 2)
    dobles.append(15 * 2)
    print("Actividad 8:", dobles)

def actividad_9():
    """Gestiona una lista anidada de compras"""
    compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
    # a) Agregar "jugo" a la lista del tercer cliente
    compras[2].append("jugo")
    # b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente
    compras[1][1] = "tallarines"
    # c) Eliminar "pan" de la lista del primer cliente
    compras[0].remove("pan")
    # d) Imprimir la lista resultante
    print("Actividad 9:", compras)

def actividad_10():
    """Crea una lista anidada con los elementos especificados"""
    lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
    print("Actividad 10:", lista_anidada)

# Menú para elegir la actividad
while True:
    print("\nElige la actividad que deseas ejecutar (1-10) o 0 para salir:")
    opcion = input("> ")

    if opcion == '1':
        actividad_1()
    elif opcion == '2':
        actividad_2()
    elif opcion == '3':
        actividad_3()
    elif opcion == '4':
        actividad_4()
    elif opcion == '5':
        actividad_5()
    elif opcion == '6':
        actividad_6()
    elif opcion == '7':
        actividad_7()
    elif opcion == '8':
        actividad_8()
    elif opcion == '9':
        actividad_9()
    elif opcion == '10':
        actividad_10()
    elif opcion == '0':
        print("Terminado")
        break
    else:
        print("Opción inválida. Por favor, elige un número entre 1 y 10 o 0 para salir")