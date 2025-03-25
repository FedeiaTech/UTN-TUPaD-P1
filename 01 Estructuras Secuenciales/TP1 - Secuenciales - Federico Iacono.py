## Trabajo practico de Programacion I - Secuenciales

# Alumno: Federico Iacono

# 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
print("Hola mundo")

# 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla.
nombre = input("ingrese un nombre: ")
print(f"Hola, {nombre}")

# 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30 años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla.
print("-Armando la oracion-")
nombre = input("ingrese un nombre: ")
apellido = input("ingrese un apellido: ")
edad = input("ingrese una edad: ")
nacionalidad = input("ingrese una nacionalidad: ")

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {nacionalidad}")

# 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.
radio = int(input("ingrese el radio de un circulo"))
PI = 3.14

area = PI * radio**2
perimetro = PI * radio * 2

print(f"Area del circulo: {area}")
print(f"Perimetro del circulo: {perimetro}")

# 5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale.
segundos = int(input("ingrese cantidad de segundos"))

horas = float(segundos/3600)

print(f"Son: {horas} horas")

# 6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.
factor = int(input("ingrese un numero para saber sus valores en la tabla de multiplicar"))

print(f"1x{factor}={factor*1}")
print(f"2x{factor}={factor*2}")
print(f"3x{factor}={factor*3}")
print(f"4x{factor}={factor*4}")
print(f"5x{factor}={factor*5}")
print(f"6x{factor}={factor*6}")
print(f"7x{factor}={factor*7}")
print(f"8x{factor}={factor*8}")
print(f"9x{factor}={factor*9}")
print(f"10x{factor}={factor*10}")

# 7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.
print("Calculadora")
primero = float(input("ingrese el primer numero entero >0: "))
segundo = float(input("ingrese el segundo numero entero >0: "))

suma = primero + segundo
resta = primero - segundo
multi = primero * segundo
division = primero / segundo

print(f"la suma de ambos es: {suma}")
print(f"la resta de ambos es: {resta}")
print(f"la multiplicacion de ambos es: {multi}")
print(f"la division de ambos es: {division}")

# 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente modo:
# 𝐼𝑀𝐶 = 𝑝𝑒𝑠𝑜 𝑒𝑛 𝑘𝑔 / (𝑎𝑙𝑡𝑢𝑟𝑎 𝑒𝑛 𝑚)^2
print("Indice de Masa Corporal")
altura = float(input("Coloque su altura en (m): "))
peso = float(input("Coloque su peso en (kg): "))

imc = peso / altura **2

print(f"Su IMC es: {imc}")


# 9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:
# 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐹𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖𝑡 = 9/5 * 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐶𝑒𝑙𝑠𝑖𝑢𝑠 + 32

tempC = float(input("Indique la tempereatura en grados Celsius: "))

tempF = 9/5 * tempC +32

print(f"La temperatura en grados Fahrenheit es: {tempF}")

# 10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números.
print("Promedio de tres numeros")
primer = float(input("Indique el primer numero: "))
segundo = float(input("Indique el segundo numero: "))
tercer = float(input("Indique el tercer numero: "))

prom = (primero + segundo + tercer) / 3

print(f"el promedio de los tres numeros es: {prom}")