# Autor: IACONO. Federico

def actividad_1():
    print("\n--- Actividad 1 ---")
    # Dado el diccionario precios_frutas, añadir nuevas frutas.
    precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

    # Añadir las siguientes frutas con sus respectivos precios
    precios_frutas['Naranja'] = 1200
    precios_frutas['Manzana'] = 1500
    precios_frutas['Pera'] = 2300

    print("Diccionario después de añadir frutas:")
    print(precios_frutas)
    print("-" * 30)

def actividad_2():
    print("\n--- Actividad 2 ---")
    # Siguiendo con el diccionario precios_frutas del punto anterior, actualizar los precios.
    # (Para esta actividad, necesitamos el estado final de precios_frutas de la Actividad 1.
    # Si se ejecuta de forma aislada, es mejor recrearlo o pasar como parámetro).
    # Aquí lo recrearemos para que sea independiente si se ejecuta sola.
    precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450, 'Naranja': 1200, 'Manzana': 1500, 'Pera': 2300}

    # Actualizar precios
    precios_frutas['Banana'] = 1330
    precios_frutas['Manzana'] = 1700
    precios_frutas['Melón'] = 2800

    print("Diccionario después de actualizar precios:")
    print(precios_frutas)
    print("-" * 30)

def actividad_3():
    print("\n--- Actividad 3 ---")
    # Siguiendo con el diccionario precios_frutas del punto anterior, crear una lista que contenga únicamente las frutas sin los precios.
    # (Recreamos el diccionario para independencia).
    precios_frutas = {'Banana': 1330, 'Ananá': 2500, 'Melón': 2800, 'Uva': 1450, 'Naranja': 1200, 'Manzana': 1700, 'Pera': 2300}

    # Obtener solo las claves (nombres de las frutas)
    lista_frutas = list(precios_frutas.keys())

    print("Lista de frutas (solo nombres):")
    print(lista_frutas)
    print("-" * 30)

def actividad_4():
    print("\n--- Actividad 4 ---")
    # Programa para almacenar y consultar números telefónicos.

    contactos = {}
    print("Carga de 5 contactos:")
    for i in range(5):
        nombre = input(f"Ingrese el nombre del contacto {i+1}: ")
        numero = input(f"Ingrese el número de teléfono para {nombre}: ")
        contactos[nombre] = numero

    print("\nContactos cargados:")
    print(contactos)

    # Pedir un nombre y mostrar el número asociado
    nombre_consulta = input("\nIngrese un nombre para consultar su número de teléfono: ")
    if nombre_consulta in contactos:
        print(f"El número de {nombre_consulta} es: {contactos[nombre_consulta]}")
    else:
        print(f"El contacto '{nombre_consulta}' no se encontró en la agenda.")
    print("-" * 30)

def actividad_5():
    print("\n--- Actividad 5 ---")
    # Solicitar una frase e imprimir palabras únicas y recuento de palabras.

    frase = input("Ingrese una frase: ").lower() # Convertir a minúsculas para contar palabras de forma insensible a mayúsculas/minúsculas
    palabras = frase.split() # Dividir la frase en palabras

    # Palabras únicas (usando un set)
    palabras_unicas = set(palabras)
    print(f"Palabras únicas: {palabras_unicas}")

    # Diccionario con la cantidad de veces que aparece cada palabra
    recuento_palabras = {}
    for palabra in palabras:
        recuento_palabras[palabra] = recuento_palabras.get(palabra, 0) + 1

    print(f"Recuento de palabras: {recuento_palabras}")
    print("-" * 30)

def actividad_6():
    print("\n--- Actividad 6 ---")
    # Permitir ingresar nombres de 3 alumnos y 3 notas, luego mostrar el promedio.

    alumnos = {}
    for i in range(3):
        nombre_alumno = input(f"Ingrese el nombre del alumno {i+1}: ")
        notas_str = input(f"Ingrese 3 notas para {nombre_alumno} (separadas por espacios): ")
        # Convertir las notas de string a enteros y guardarlas en una tupla
        try:
            notas = tuple(map(int, notas_str.split()))
            if len(notas) != 3:
                print("Debe ingresar exactamente 3 notas. Intente de nuevo.")
                return # Salir de la función si no hay 3 notas
        except ValueError:
            print("Entrada inválida. Asegúrese de ingresar solo números para las notas.")
            return # Salir de la función si la entrada no es numérica

        alumnos[nombre_alumno] = notas

    print("\nPromedio de cada alumno:")
    for alumno, notas_alumno in alumnos.items():
        if notas_alumno: # Asegurarse de que haya notas para evitar división por cero
            promedio = sum(notas_alumno) / len(notas_alumno)
            print(f"El promedio de {alumno} es: {promedio:.2f}") # Formatear a 2 decimales
        else:
            print(f"El alumno {alumno} no tiene notas para calcular el promedio.")
    print("-" * 30)

def actividad_7():
    print("\n--- Actividad 7 ---")
    # Dados dos sets de estudiantes, mostrar intersecciones y diferencias.

    parcial1_aprobados = {101, 103, 105, 107, 109, 111, 113}
    parcial2_aprobados = {102, 103, 106, 108, 109, 112, 113}

    print("Estudiantes que aprobaron Parcial 1:", parcial1_aprobados)
    print("Estudiantes que aprobaron Parcial 2:", parcial2_aprobados)

    # Estudiantes que aprobaron ambos parciales (intersección)
    ambos_parciales = parcial1_aprobados.intersection(parcial2_aprobados)
    print(f"Estudiantes que aprobaron ambos parciales: {ambos_parciales}")

    # Estudiantes que aprobaron solo uno de los dos (diferencia simétrica)
    solo_uno = parcial1_aprobados.symmetric_difference(parcial2_aprobados)
    print(f"Estudiantes que aprobaron solo uno de los dos parciales: {solo_uno}")

    # Lista total de estudiantes que aprobaron al menos un parcial (unión)
    total_aprobados = parcial1_aprobados.union(parcial2_aprobados)
    print(f"Lista total de estudiantes que aprobaron al menos un parcial: {total_aprobados}")
    print("-" * 30)


def actividad_8():
    print("\n--- Actividad 8 ---")
    # Diccionario de productos y stock con interacción de usuario.

    stock_productos = {
        "leche": 50,
        "pan": 30,
        "huevos": 120
    }

    while True:
        print("\nOpciones de gestión de stock:")
        print("1. Consultar stock de un producto")
        print("2. Agregar unidades a un producto existente")
        print("3. Agregar un nuevo producto")
        print("4. Mostrar todo el stock")
        print("5. Salir del programa de gestión")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            producto = input("Ingrese el nombre del producto a consultar: ").lower()
            if producto in stock_productos:
                print(f"El stock de {producto} es: {stock_productos[producto]} unidades.")
            else:
                print(f"El producto '{producto}' no se encuentra en el stock.")
        elif opcion == '2':
            producto = input("Ingrese el nombre del producto para agregar unidades: ").lower()
            if producto in stock_productos:
                try:
                    unidades = int(input(f"¿Cuántas unidades desea agregar a {producto}?: "))
                    if unidades > 0:
                        stock_productos[producto] += unidades
                        print(f"Se agregaron {unidades} unidades a {producto}. Nuevo stock: {stock_productos[producto]}.")
                    else:
                        print("Por favor, ingrese un número positivo de unidades.")
                except ValueError:
                    print("Entrada inválida. Por favor, ingrese un número entero.")
            else:
                print(f"El producto '{producto}' no existe. Use la opción 3 para agregarlo.")
        elif opcion == '3':
            producto = input("Ingrese el nombre del nuevo producto: ").lower()
            if producto not in stock_productos:
                try:
                    unidades = int(input(f"Ingrese el stock inicial para {producto}: "))
                    if unidades >= 0:
                        stock_productos[producto] = unidades
                        print(f"Producto '{producto}' agregado con stock inicial de {unidades}.")
                    else:
                        print("Por favor, ingrese un número de unidades no negativo.")
                except ValueError:
                    print("Entrada inválida. Por favor, ingrese un número entero.")
            else:
                print(f"El producto '{producto}' ya existe. Use la opción 2 para agregar unidades.")
        elif opcion == '4':
            print("\n--- Stock Actual ---")
            if stock_productos:
                for prod, stock_cant in stock_productos.items():
                    print(f"- {prod.capitalize()}: {stock_cant} unidades")
            else:
                print("El stock está vacío.")
            print("--------------------")
        elif opcion == '5':
            print("Saliendo del programa de gestión de stock.")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")
    print("-" * 30)


def actividad_9():
    print("\n--- Actividad 9 ---")
    # Creación de una agenda con tuplas (día, hora) como claves.

    agenda = {
        ("lunes", "10:00"): "Reunión de equipo",
        ("martes", "15:00"): "Clase de inglés",
        ("miércoles", "09:30"): "Cita con el dentista"
    }

    print("Agenda actual:")
    for (dia, hora), evento in agenda.items():
        print(f"El {dia} a las {hora}: {evento}")

    while True:
        print("\nOpciones de la agenda:")
        print("1. Consultar actividad en día y hora")
        print("2. Salir de la agenda")

        opcion_agenda = input("Seleccione una opción: ")

        if opcion_agenda == '1':
            dia_consulta = input("Ingrese el día (ej. lunes): ").lower()
            hora_consulta = input("Ingrese la hora (ej. 10:00): ")
            
            clave_consulta = (dia_consulta, hora_consulta)
            
            if clave_consulta in agenda:
                print(f"El {dia_consulta} a las {hora_consulta} la actividad es: {agenda[clave_consulta]}")
            else:
                print(f"No hay actividad programada para el {dia_consulta} a las {hora_consulta}.")
        elif opcion_agenda == '2':
            print("Saliendo de la agenda.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
    print("-" * 30)


def actividad_10():
    print("\n--- Actividad 10 ---")
    # Invertir un diccionario de países y capitales.

    paises_capitales = {
        "Argentina": "Buenos Aires",
        "Chile": "Santiago",
        "España": "Madrid",
        "México": "Ciudad de México"
    }

    print("Diccionario original (País: Capital):")
    print(paises_capitales)

    # Construir un nuevo diccionario donde las capitales sean las claves y los países los valores.
    # Usamos una comprensión de diccionario (dictionary comprehension)
    capitales_paises = {capital: pais for pais, capital in paises_capitales.items()}

    print("\nDiccionario invertido (Capital: País):")
    print(capitales_paises)
    print("-" * 30)


def mostrar_menu():
    print("\n" + "="*40)
    print("        MENÚ DE ACTIVIDADES")
    print("="*40)
    print("1: Añadir frutas a diccionario")
    print("2: Actualizar precios de frutas")
    print("3: Obtener solo nombres de frutas")
    print("4: Agenda telefónica (5 contactos)")
    print("5: Analizar frase (palabras únicas y recuento)")
    print("6: Promedio de notas de alumnos")
    print("7: Operaciones con sets de estudiantes")
    print("8: Gestión de stock de productos")
    print("9: Agenda (día, hora: evento)")
    print("10: Invertir diccionario de países y capitales")
    print("0. Salir")
    print("="*40)

def main():
    while True:
        mostrar_menu()
        opcion = input("Ingrese el número de la actividad a ejecutar (0 para salir): ")

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
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, ingrese un número del 0 al 10.")
        
        input("\nPresione Enter para continuar...")


main()

