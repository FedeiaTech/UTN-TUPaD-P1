import math

# 1. Función para imprimir "Hola Mundo!"
def imprimir_hola_mundo():
    print("Hola Mundo!")

# 2. Función para saludar a un usuario
def saludar_usuario(nombre):
    return f"Hola {nombre}!"

# 3. Función para mostrar información personal
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

# 4. Funciones para calcular el área y perímetro de un círculo
def calcular_area_circulo(radio):
    return math.pi * (radio ** 2)

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

# 5. Función para convertir segundos a horas
def segundos_a_horas(segundos):
    return segundos / 3600

# 6. Función para imprimir la tabla de multiplicar
def tabla_multiplicar(numero):
    print(f"Tabla de multiplicar del {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

# 7. Función para realizar operaciones básicas
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else None
    return (suma, resta, multiplicacion, division)

# 8. Función para calcular el Índice de Masa Corporal (IMC)
def calcular_imc(peso, altura):
    """
    Calcula el Índice de Masa Corporal (IMC)

    Args:
        peso (float): El peso en kilogramos
        altura (float): La altura en metros

    Returns:
        float: El valor del IMC. Retorna None si la altura es cero
    """
    if altura > 0:
        return peso / (altura ** 2)
    else:
        return None

# 9. Función para convertir Celsius a Fahrenheit
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# 10. Función para calcular el promedio de tres números
def calcular_promedio(a, b, c):
    return (a + b + c) / 3

# --- Programa Principal (Menú Interactivo) ---
def main():
    while True:
        print("\n--- Menú de Funciones ---")
        print("1. Imprimir 'Hola Mundo!'")
        print("2. Saludar a un usuario")
        print("3. Mostrar información personal")
        print("4. Calcular área y perímetro de un círculo")
        print("5. Convertir segundos a horas")
        print("6. Imprimir tabla de multiplicar")
        print("7. Realizar operaciones básicas")
        print("8. Calcular Índice de Masa Corporal (IMC)")
        print("9. Convertir Celsius a Fahrenheit")
        print("10. Calcular promedio de tres números")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            imprimir_hola_mundo()
        elif opcion == '2':
            nombre = input("Ingrese su nombre: ")
            print(saludar_usuario(nombre))
        elif opcion == '3':
            nombre = input("Ingrese su nombre: ")
            apellido = input("Ingrese su apellido: ")
            try:
                edad = int(input("Ingrese su edad: "))
            except ValueError:
                print("Edad inválida. Debe ser un número entero.")
                continue
            residencia = input("Ingrese su lugar de residencia: ")
            informacion_personal(nombre, apellido, edad, residencia)
        elif opcion == '4':
            try:
                radio = float(input("Ingrese el radio del círculo: "))
                if radio < 0:
                    print("El radio no puede ser negativo")
                    continue
                area = calcular_area_circulo(radio)
                perimetro = calcular_perimetro_circulo(radio)
                print(f"El área del círculo es: {area:.2f}")
                print(f"El perímetro del círculo es: {perimetro:.2f}")
            except ValueError:
                print("Entrada inválida. Asegúrese de ingresar un número para el radio")
        elif opcion == '5':
            try:
                segundos = int(input("Ingrese la cantidad de segundos: "))
                if segundos < 0:
                    print("Los segundos no pueden ser negativos")
                    continue
                horas = segundos_a_horas(segundos)
                print(f"{segundos} segundos equivalen a {horas:.2f} horas.")
            except ValueError:
                print("Entrada inválida. Asegúrese de ingresar un número entero para los segundos")
        elif opcion == '6':
            try:
                numero_tabla = int(input("Ingrese el número del que desea la tabla de multiplicar: "))
                tabla_multiplicar(numero_tabla)
            except ValueError:
                print("Entrada inválida. Asegúrese de ingresar un número entero")
        elif opcion == '7':
            try:
                num1 = float(input("Ingrese el primer número: "))
                num2 = float(input("Ingrese el segundo número: "))
                suma, resta, multiplicacion, division = operaciones_basicas(num1, num2)
                print(f"Suma: {suma}")
                print(f"Resta: {resta}")
                print(f"Multiplicación: {multiplicacion}")
                if division is not None:
                    print(f"División: {division}")
                else:
                    print("No se puede dividir por cero")
            except ValueError:
                print("Entrada inválida. Asegúrese de ingresar números")
        elif opcion == '8':
            try:
                peso = float(input("Ingrese su peso en kilogramos: "))
                altura = float(input("Ingrese su altura en metros: "))
                if peso <= 0 or altura <= 0:
                    print("El peso y la altura deben ser valores positivos")
                    continue
                imc = calcular_imc(peso, altura)
                if imc is not None:
                    print(f"Su Índice de Masa Corporal (IMC) es: {imc:.2f}")
                else:
                    print("No se puede calcular el IMC con altura cero")
            except ValueError:
                print("Entrada inválida. Asegúrese de ingresar números para peso y altura")
        elif opcion == '9':
            try:
                celsius = float(input("Ingrese la temperatura en grados Celsius: "))
                fahrenheit = celsius_a_fahrenheit(celsius)
                print(f"{celsius}°C equivalen a {fahrenheit:.2f}°F.")
            except ValueError:
                print("Entrada inválida. Asegúrese de ingresar un número para la temperatura")
        elif opcion == '10':
            try:
                num_a = float(input("Ingrese el primer número: "))
                num_b = float(input("Ingrese el segundo número: "))
                num_c = float(input("Ingrese el tercer número: "))
                promedio = calcular_promedio(num_a, num_b, num_c)
                print(f"El promedio de los tres números es: {promedio:.2f}")
            except ValueError:
                print("Entrada inválida. Asegúrese de ingresar números")
        elif opcion == '0':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo")


main()
