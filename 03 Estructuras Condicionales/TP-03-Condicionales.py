# 1. Programa para determinar si un usuario es mayor de edad:

suedad = int(input("Ingrese su edad: "))

if suedad >= 18:
    print("Es mayor de edad")

# 2. Programa para determinar si un usuario aprobó o desaprobó:

nota = float(input("Ingrese su nota: "))

if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

# 3. Programa para ingresar solo números pares:

numero = int(input("Ingrese un número: "))

if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

#4. Programa para clasificar la edad del usuario:

edad = int(input("Ingrese su edad: "))

if edad < 12:
    print("Niño/a")
elif edad < 18:
    print("Adolescente")
elif edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")

# 5. Programa para validar la longitud de una contraseña:

contrasena = input("Ingrese su contraseña: ")

if 8 <= len(contrasena) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#6. Programa para determinar el sesgo de una distribución:

import random
from statistics import mode, median, mean

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)

if media > mediana > moda:
    print("Sesgo positivo o a la derecha")
elif media < mediana < moda:
    print("Sesgo negativo o a la izquierda")
else:
    print("Sin sesgo")

# 7. Programa para añadir signo de exclamación a una palabra o frase:

frase = input("Ingrese una frase o palabra: ")

if frase[-1] in "aeiouAEIOU":
    frase += "!"
print(frase)

# 8. Programa para transformar un nombre según la opción del usuario:

nombre = input("Ingrese su nombre: ")
opcion = int(input("Ingrese 1 (MAYUSCULAs), 2 (minusculas) o 3 (1ra en Mayuscula) para la opción deseada: "))

if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())
else:
    print("Opción inválida")

# 9. Programa para clasificar la magnitud de un terremoto:

magnitud = float(input("Ingrese la magnitud del terremoto: "))

if magnitud < 3:
    print("Muy leve (imperceptible)")
elif magnitud < 4:
    print("Leve (ligeramente perceptible)")
elif magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos)")
else:
    print("Extremo (puede causar graves daños a gran escala)")

#10. Hemisferios

hemisferio = input("Ingrese el hemisferio en el que se encuentra (N/S): ").upper()
mes = int(input("Ingrese el mes del año (1-12): "))
dia = int(input("Ingrese el día del mes: "))

if hemisferio == "N":
    if mes == 12 and dia >= 21 or mes == 1 or mes == 2 or mes == 3 and dia <= 20:
        print("Invierno")
    elif mes == 3 and dia >= 21 or mes == 4 or mes == 5 or mes == 6 and dia <= 20:
        print("Primavera")
    elif mes == 6 and dia >= 21 or mes == 7 or mes == 8 or mes == 9 and dia <= 20:
        print("Verano")
    elif mes == 9 and dia >= 21 or mes == 10 or mes == 11 or mes == 12 and dia <= 20:
        print("Otoño")
elif hemisferio == "S":
    if mes == 12 and dia >= 21 or mes == 1 or mes == 2 or mes == 3 and dia <= 20:
        print("Verano")
    elif mes == 3 and dia >= 21 or mes == 4 or mes == 5 or mes == 6 and dia <= 20:
        print("Otoño")
    elif mes == 6 and dia >= 21 or mes == 7 or mes == 8 or mes == 9 and dia <= 20:
        print("Invierno")
    elif mes == 9 and dia >= 21 or mes == 10 or mes == 11 or mes == 12 and dia <= 20:
        print("Primavera")
else:
    print("Hemisferio inválido")

## Autor: IACONO, Fede