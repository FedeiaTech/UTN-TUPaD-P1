import sys

# Función para obtener un número entero positivo del usuario
def obtener_entero_positivo(mensaje):
    while True:
        try:
            num = int(input(mensaje))
            if num >= 0:
                return num
            else:
                print("Por favor, ingresa un número entero positivo (o cero)")
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número entero")

# 1) Función recursiva para calcular el factorial de un número
def factorial(n):
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos")
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# 2) Función recursiva para calcular el valor de la serie de Fibonacci
def fibonacci_recursivo(pos):
    if pos < 0:
        raise ValueError("La posición no puede ser negativa para la serie de Fibonacci")
    if pos == 0:
        return 0
    elif pos == 1:
        return 1
    else:
        return fibonacci_recursivo(pos - 1) + fibonacci_recursivo(pos - 2)

# 3) Función recursiva para calcular la potencia de un número
def potencia_recursiva(base, exponente):
    if exponente < 0:
        # Se puede manejar de varias formas, aquí se lanza un error o se calcula 1/potencia(base, -exponente)
        raise ValueError("El exponente no puede ser negativo para esta implementación recursiva")
    if exponente == 0:
        return 1
    else:
        return base * potencia_recursiva(base, exponente - 1)

# 4) Función recursiva para convertir un número decimal a binario
def decimal_a_binario(num):
    if num == 0:
        return "0" # Caso base para el número 0
    elif num == 1:
        return "1" # Caso base para el número 1
    else:
        # La concatenación se hace al revés de cómo se obtienen los restos
        return decimal_a_binario(num // 2) + str(num % 2)

# 5) Función recursiva para verificar si una cadena es un palíndromo
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True # Caso base: cadena vacía o de un solo carácter es un palíndromo
    else:
        # Comprueba si los caracteres de los extremos son iguales
        # y luego recursivamente verifica el resto de la cadena
        if palabra[0] == palabra[-1]:
            return es_palindromo(palabra[1:-1])
        else:
            return False

# 6) Función recursiva para sumar los dígitos de un número
def suma_digitos(n):
    if n < 0:
        raise ValueError("El número debe ser positivo")
    if n < 10: # Caso base: si es un solo dígito, la suma es el propio dígito
        return n
    else:
        # Suma el último dígito (n % 10) y llama recursivamente con el resto del número (n // 10)
        return (n % 10) + suma_digitos(n // 10)

# 7) Función recursiva para contar bloques en una pirámide
def contar_bloques(n):
    if n <= 0: # Caso base: 0 o menos niveles no requieren bloques
        return 0
    elif n == 1: # Caso base: 1 nivel requiere 1 bloque
        return 1
    else:
        # La suma total es n (bloques en el nivel actual) + bloques en los niveles inferiores
        return n + contar_bloques(n - 1)

# 8) Función recursiva para contar la aparición de un dígito en un número
def contar_digito(numero, digito):
    if not (0 <= digito <= 9):
        raise ValueError("El dígito a buscar debe estar entre 0 y 9")
    if numero < 0:
        numero = abs(numero) # Manejar números negativos convirtiéndolos a positivos
    
    if numero == 0:
        # Si el número original era 0 y el dígito buscado es 0, cuenta 1
        # Esto se necesita para evitar un caso donde contar_digito(0, 0) devuelva 0
        # Si el número original era distinto de 0 y llegó a 0 recursivamente, ya no hay dígitos
        return 1 if (numero == 0 and digito == 0) else 0 
    
    # Obtener el último dígito del número
    ultimo_digito = numero % 10
    
    # Contar si el último dígito coincide y sumar el resultado de la llamada recursiva
    if ultimo_digito == digito:
        return 1 + contar_digito(numero // 10, digito)
    else:
        return 0 + contar_digito(numero // 10, digito)


# --- Menú principal y ejecución ---
def mostrar_menu():
    print("\n--- EJERCICIOS DE RECURSIVIDAD ---")
    print("1. Calcular Factorial")
    print("2. Calcular Serie de Fibonacci")
    print("3. Calcular Potencia")
    print("4. Convertir Decimal a Binario")
    print("5. Verificar Palíndromo")
    print("6. Sumar Dígitos de un Número")
    print("7. Contar Bloques de Pirámide")
    print("8. Contar Apariciones de un Dígito en un Número")
    print("0. Salir")
    print("-----------------------------------")

def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            num = obtener_entero_positivo("Ingresa un número entero positivo para calcular su factorial: ")
            print(f"Calculando factoriales desde 1 hasta {num}:")
            for i in range(1, num + 1):
                try:
                    print(f"Factorial de {i} = {factorial(i)}")
                except ValueError as e:
                    print(f"Error: {e}")
                    break # Salir del bucle si hay un error con el factorial

        elif opcion == '2':
            pos = obtener_entero_positivo("Ingresa la posición hasta la cual quieres mostrar la serie de Fibonacci: ")
            print(f"Serie de Fibonacci hasta la posición {pos}:")
            serie = []
            for i in range(pos + 1):
                try:
                    serie.append(fibonacci_recursivo(i))
                except ValueError as e:
                    print(f"Error: {e}")
                    break
            print(serie)

        elif opcion == '3':
            base = obtener_entero_positivo("Ingresa la base: ")
            exponente = obtener_entero_positivo("Ingresa el exponente (solo enteros no negativos): ")
            try:
                resultado = potencia_recursiva(base, exponente)
                print(f"{base}^{exponente} = {resultado}")
            except ValueError as e:
                print(f"Error: {e}")

        elif opcion == '4':
            num = obtener_entero_positivo("Ingresa un número decimal positivo para convertirlo a binario: ")
            if num == 0:
                print("El número binario de 0 es: 0")
            else:
                try:
                    binario = decimal_a_binario(num)
                    print(f"El número decimal {num} en binario es: {binario}")
                except RecursionError:
                    print("Error: El número es demasiado grande para la recursión en esta implementación")

        elif opcion == '5':
            palabra = input("Ingresa una palabra (sin espacios ni tildes) para verificar si es un palíndromo: ").lower()
            if es_palindromo(palabra):
                print(f"'{palabra}' ES un palíndromo")
            else:
                print(f"'{palabra}' NO es un palíndromo.")

        elif opcion == '6':
            num = obtener_entero_positivo("Ingresa un número entero positivo para sumar sus dígitos: ")
            try:
                suma = suma_digitos(num)
                print(f"La suma de los dígitos de {num} es: {suma}")
            except ValueError as e:
                print(f"Error: {e}")

        elif opcion == '7':
            n_niveles = obtener_entero_positivo("Ingresa el número de bloques en el nivel más bajo de la pirámide: ")
            total_bloques = contar_bloques(n_niveles)
            print(f"Para una pirámide con {n_niveles} bloques en la base, se necesitan {total_bloques} bloques en total")

        elif opcion == '8':
            numero = obtener_entero_positivo("Ingresa el número entero positivo: ")
            digito = obtener_entero_positivo("Ingresa el dígito (0-9) a buscar: ")
            try:
                if digito < 0 or digito > 9:
                    print("Error: El dígito debe estar entre 0 y 9")
                else:
                    conteo = contar_digito(numero, digito)
                    print(f"El dígito {digito} aparece {conteo} vez(veces) en el número {numero}")
            except ValueError as e:
                print(f"Error: {e}")

        elif opcion == '0':
            print("Saliendo del programa. ¡Hasta luego!")
            sys.exit() # Termina la ejecución del script
        else:
            print("Opción no válida. Por favor, intenta de nuevo")

main()

