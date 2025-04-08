"""Autor: Federico Iacono"""

def actividad_1():
    """Imprime números enteros de 0 a 100."""
    for i in range(101):
        print(i)

def actividad_2():
    """Solicita un número y muestra la cantidad de dígitos."""
    try:
        numero = int(input("Ingrese un número entero: "))
        cantidad_digitos = len(str(abs(numero)))
        print(f"El número {numero} tiene {cantidad_digitos} dígitos.")
    except ValueError:
        print("Por favor, ingrese un número entero válido.")

def actividad_3():
    """Suma números entre dos valores ingresados."""
    try:
        num1 = int(input("Ingrese el primer número entero: "))
        num2 = int(input("Ingrese el segundo número entero: "))
        suma = 0
        if num1 < num2:
            for i in range(num1 + 1, num2):
                suma += i
            print(f"La suma de los números entre {num1} y {num2} es: {suma}")
        elif num2 < num1:
            for i in range(num2 + 1, num1):
                suma += i
            print(f"La suma de los números entre {num2} y {num1} es: {suma}")
        else:
            print("Los números ingresados son iguales, no hay números entre ellos.")
    except ValueError:
        print("Por favor, ingrese números enteros válidos.")

def actividad_4():
    """Suma números ingresados hasta que se ingrese 0."""
    suma_total = 0
    print("Ingrese números enteros para sumar (ingrese 0 para detener):")
    while True:
        try:
            numero = int(input("> "))
            if numero == 0:
                break
            suma_total += numero
        except ValueError:
            print("Por favor, ingrese un número entero válido.")
    print(f"La suma total de los números ingresados es: {suma_total}")

import random

def actividad_5():
    """Juego de adivinar un número aleatorio."""
    numero_secreto = random.randint(0, 9)
    intentos = 0
    print("Adivina el número secreto entre 0 y 9.")
    while True:
        try:
            intento = int(input("Ingresa tu intento: "))
            intentos += 1
            if intento == numero_secreto:
                print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
                break
            elif intento < numero_secreto:
                print("El número secreto es mayor.")
            else:
                print("El número secreto es menor.")
        except ValueError:
            print("Por favor, ingrese un número entero válido.")

def actividad_6():
    """Imprime números pares de 0 a 100 en orden decreciente."""
    for i in range(100, -1, -2):
        print(i)

def actividad_7():
    """Calcula la suma de números de 0 hasta un número ingresado."""
    try:
        limite = int(input("Ingrese un número entero positivo: "))
        if limite <= 0:
            print("Por favor, ingrese un número entero positivo.")
        else:
            suma = sum(range(limite + 1))
            print(f"La suma de los números desde 0 hasta {limite} es: {suma}")
    except ValueError:
        print("Por favor, ingrese un número entero válido.")

def actividad_8(cantidad_numeros=100):
    """Cuenta pares, impares, positivos y negativos de N números."""
    pares = 0
    impares = 0
    positivos = 0
    negativos = 0
    numeros_ingresados = []
    print(f"Ingrese {cantidad_numeros} números enteros:")
    for i in range(cantidad_numeros):
        try:
            numero = int(input(f"Número {i+1}: "))
            numeros_ingresados.append(numero)
            if numero % 2 == 0:
                pares += 1
            else:
                impares += 1
            if numero > 0:
                positivos += 1
            elif numero < 0:
                negativos += 1
        except ValueError:
            print("Por favor, ingrese un número entero válido.")
            # Puedes decidir si quieres interrumpir o continuar si hay un error
            continue

    print("\nResultados:")
    print(f"Cantidad de números pares: {pares}")
    print(f"Cantidad de números impares: {impares}")
    print(f"Cantidad de números positivos: {positivos}")
    print(f"Cantidad de números negativos: {negativos}")

def actividad_9(cantidad_numeros=100):
    """Calcula la media de N números ingresados."""
    suma = 0
    numeros_ingresados = []
    print(f"Ingrese {cantidad_numeros} números enteros:")
    for i in range(cantidad_numeros):
        try:
            numero = int(input(f"Número {i+1}: "))
            numeros_ingresados.append(numero)
            suma += numero
        except ValueError:
            print("Por favor, ingrese un número entero válido.")
            # Puedes decidir si quieres interrumpir o continuar si hay un error
            continue

    if numeros_ingresados:
        media = suma / len(numeros_ingresados)
        print(f"\nLa media de los números ingresados es: {media}")
    else:
        print("No se ingresaron números para calcular la media.")

def actividad_10():
    """Invierte el orden de los dígitos de un número."""
    try:
        numero_str = input("Ingrese un número entero: ")
        numero_invertido = numero_str[::-1]
        print(f"El número invertido es: {numero_invertido}")
    except Exception:
        print("Por favor, ingrese un número entero válido.")

def mostrar_menu():
    print("\n--- Menú de Actividades ---")
    print("1) Imprimir números de 0 a 100")
    print("2) Cantidad de dígitos de un número")
    print("3) Suma de números entre dos valores")
    print("4) Suma secuencial de números (termina con 0)")
    print("5) Juego de adivinar un número")
    print("6) Imprimir números pares de 0 a 100 (decreciente)")
    print("7) Suma de números de 0 hasta un valor")
    print("8) Contar pares, impares, positivos y negativos (100 números)")
    print("9) Calcular la media de 100 números")
    print("10) Invertir dígitos de un número")
    print("0) Salir")

while True:
    mostrar_menu()
    opcion = input("Seleccione una actividad (0-10): ")

    match opcion:
        case "1":
            actividad_1()
        case "2":
            actividad_2()
        case "3":
            actividad_3()
        case "4":
            actividad_4()
        case "5":
            actividad_5()
        case "6":
            actividad_6()
        case "7":
            actividad_7()
        case "8":
            actividad_8()
        case "9":
            actividad_9()
        case "10":
            actividad_10()
        case "0":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        case _:
            print("Opción inválida. Por favor, seleccione una opción del menú.")