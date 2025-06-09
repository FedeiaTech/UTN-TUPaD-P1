import time
import random

# --- 1. Breve descripción del problema a resolver ---
# Imagina que tenemos una tienda en línea y necesitamos gestionar un inventario de productos.
# Cada producto tiene un nombre y un precio.
# Constantemente, necesitamos:
# 1. Ordenar nuestros productos por precio para mostrarlos de forma ascendente o descendente.
# 2. Buscar un producto específico por su nombre o precio después de haber ordenado la lista.
# Este caso práctico demostrará cómo los algoritmos de ordenamiento (Selection Sort y Quick Sort)
# y un algoritmo de búsqueda (Búsqueda Binaria en este caso, aplicable a listas ordenadas)
# nos ayudan a gestionar eficientemente este inventario.

# Clase simple para representar un Producto
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __repr__(self):
        # Representación amigable para imprimir el objeto Producto
        return f"({self.nombre}, ${self.precio:.2f})"

    def __lt__(self, other):
        # Permite comparar productos por precio, útil para el ordenamiento
        return self.precio < other.precio

# --- 2. Código fuente comentado ---

# --- Implementación de Selection Sort ---
def selection_sort(arr):
    """
    Implementa el algoritmo de ordenamiento Selection Sort.
    Selection Sort itera a través de la lista, encuentra el elemento mínimo
    del subarreglo no ordenado y lo coloca al principio.
    Es simple pero ineficiente para grandes conjuntos de datos.
    Complejidad temporal: O(n^2) en el mejor, promedio y peor caso.
    Complejidad espacial: O(1).
    """
    n = len(arr) # Obtiene la longitud del arreglo
    for i in range(n):
        # Asume que el primer elemento no ordenado es el mínimo
        min_idx = i
        # Itera sobre el resto del arreglo no ordenado para encontrar el mínimo real
        for j in range(i + 1, n):
            if arr[j].precio < arr[min_idx].precio:
                min_idx = j # Actualiza el índice del mínimo si se encuentra un valor menor
        # Intercambia el elemento mínimo encontrado con el primer elemento no ordenado
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# --- Implementación de Quick Sort ---
def quick_sort(arr):
    """
    Implementa el algoritmo de ordenamiento Quick Sort.
    Quick Sort es un algoritmo de "divide y vencerás". Elige un 'pivote'
    del arreglo y particiona los otros elementos en dos subarreglos,
    según si son menores o mayores que el pivote. Los subarreglos se ordenan recursivamente.
    Complejidad temporal:
        O(n log n) en el mejor y promedio caso.
        O(n^2) en el peor caso (pivote mal elegido).
    Complejidad espacial: O(log n) en el promedio caso (debido a la pila de recursión).
    """
    # Función auxiliar recursiva para Quick Sort
    def _quick_sort_recursive(arr, low, high):
        if low < high:
            # Encuentra el índice de partición
            pi = _partition(arr, low, high)
            # Ordena recursivamente los elementos antes y después de la partición
            _quick_sort_recursive(arr, low, pi - 1)
            _quick_sort_recursive(arr, pi + 1, high)

    # Función de partición de Lomuto
    def _partition(arr, low, high):
        pivot = arr[high].precio # Elige el último elemento como pivote
        i = (low - 1) # Índice del elemento más pequeño
        for j in range(low, high):
            # Si el elemento actual es menor o igual que el pivote
            if arr[j].precio <= pivot:
                i += 1 # Incrementa el índice del elemento más pequeño
                # Intercambia arr[i] y arr[j]
                arr[i], arr[j] = arr[j], arr[i]
        # Intercambia el pivote con el elemento en la posición (i + 1)
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return (i + 1) # Retorna el índice de partición

    # Llama a la función recursiva con los límites iniciales
    _quick_sort_recursive(arr, 0, len(arr) - 1)
    return arr

# --- Implementación de Búsqueda Binaria ---
def binary_search(arr, target_price):
    """
    Implementa el algoritmo de búsqueda binaria.
    Requiere que la lista esté ORDENADA. Divide repetidamente el intervalo
    de búsqueda por la mitad.
    Complejidad temporal: O(log n).
    Complejidad espacial: O(1).
    """
    low = 0 # Índice inicial
    high = len(arr) - 1 # Índice final

    while low <= high:
        mid = (low + high) // 2 # Calcula el índice medio
        current_product = arr[mid]

        if current_product.precio == target_price:
            # Si el precio del producto medio es igual al objetivo, lo encontramos
            return current_product
        elif current_product.precio < target_price:
            # Si el precio del producto medio es menor que el objetivo, busca en la mitad derecha
            low = mid + 1
        else:
            # Si el precio del producto medio es mayor que el objetivo, busca en la mitad izquierda
            high = mid - 1
    return None # Retorna None si el producto no se encuentra

# --- 3. Explicación de decisiones de diseño ---
"""
Decisiones de Diseño: Selection Sort vs. Quick Sort

Para este caso práctico, se eligieron Selection Sort y Quick Sort para el ordenamiento debido a que
representan dos paradigmas diferentes:

1.  Selection Sort:
    * Ventajas: Es uno de los algoritmos de ordenamiento más simples de entender e implementar.
        Es eficiente en el uso de memoria (in-place) y realiza un número mínimo de intercambios,
        lo que puede ser beneficioso si el costo de los intercambios es muy alto.
    * Desventajas: Su principal desventaja es su complejidad temporal de O(n^2) en todos los casos.
        Esto lo hace poco práctico para conjuntos de datos grandes, ya que el tiempo de ejecución
        crece cuadráticamente con el número de elementos. No es adecuado para aplicaciones donde
        el rendimiento es crítico con grandes volúmenes de datos.

2.  Quick Sort:
    * Ventajas: Es uno de los algoritmos de ordenamiento más rápidos en la práctica para grandes
        conjuntos de datos, con una complejidad promedio de O(n log n). Es un algoritmo de
        "divide y vencerás" que lo hace muy eficiente. Es in-place, lo que significa que no requiere
        una gran cantidad de memoria adicional.
    * Desventajas: En el peor de los casos (cuando la elección del pivote es consistentemente pobre),
        su complejidad puede degradarse a O(n^2), similar a Selection Sort. Sin embargo, esto es raro
        en implementaciones bien hechas con elección de pivote aleatoria o mediana de tres.
        También es un algoritmo recursivo, lo que puede llevar a un desbordamiento de pila
        para conjuntos de datos extremadamente grandes si la recursión no se gestiona correctamente
        (por ejemplo, optimización de cola o un límite de recursión).

¿Por qué se eligió Quick Sort sobre Selection Sort para rendimiento general?
Para la mayoría de los escenarios del mundo real, donde el rendimiento y la escalabilidad
son cruciales (como ordenar un gran inventario de productos), Quick Sort es la elección preferida
debido a su eficiencia promedio de O(n log n). Aunque Selection Sort es simple, su rendimiento
cuadrático lo hace inviable para colecciones de tamaño significativo.

Búsqueda Binaria:
Una vez que los datos están ordenados (ya sea por Selection Sort o Quick Sort), la Búsqueda Binaria
se convierte en el método de búsqueda más eficiente. Su complejidad de O(log n) significa que el
tiempo de búsqueda crece logarítmicamente con el tamaño de la lista, permitiendo encontrar elementos
rápidamente incluso en conjuntos de datos muy grandes. No sería posible usar Búsqueda Binaria
si la lista no estuviera previamente ordenada.
"""

# --- 4. Validación del funcionamiento ---

if __name__ == "__main__":
    print("--- Caso Práctico de Búsqueda y Ordenamiento ---")

    # Generar una lista de productos de ejemplo
    productos_originales = []
    n_productos = 10000 # Número de productos para probar el rendimiento
    for i in range(n_productos):
        productos_originales.append(Producto(f"Producto_{i}", round(random.uniform(10, 1000), 2)))

    # Mostrar algunos productos iniciales (solo los primeros 10 para no inundar la consola)
    print("\nProductos Originales (primeros 10):")
    print(productos_originales[:10])

    # --- Prueba de Selection Sort ---
    print(f"\n--- Probando Selection Sort con {n_productos} productos ---")
    productos_selection_sort = list(productos_originales) # Crear una copia para no modificar el original
    start_time = time.time()
    selection_sort(productos_selection_sort)
    end_time = time.time()
    print(f"Tiempo de ejecución de Selection Sort: {end_time - start_time:.4f} segundos")
    print("Productos Ordenados por Selection Sort (primeros 10):")
    print(productos_selection_sort[:10])
    print("Productos Ordenados por Selection Sort (últimos 10):")
    print(productos_selection_sort[-10:])
    # Verificar si está ordenado (opcional, pero buena práctica)
    is_sorted_selection = all(productos_selection_sort[i].precio <= productos_selection_sort[i+1].precio for i in range(len(productos_selection_sort) - 1))
    print(f"¿Lista ordenada por Selection Sort? {is_sorted_selection}")

    # --- Prueba de Quick Sort ---
    print(f"\n--- Probando Quick Sort con {n_productos} productos ---")
    productos_quick_sort = list(productos_originales) # Crear otra copia
    start_time = time.time()
    quick_sort(productos_quick_sort)
    end_time = time.time()
    print(f"Tiempo de ejecución de Quick Sort: {end_time - start_time:.4f} segundos")
    print("Productos Ordenados por Quick Sort (primeros 10):")
    print(productos_quick_sort[:10])
    print("Productos Ordenados por Quick Sort (últimos 10):")
    print(productos_quick_sort[-10:])
    # Verificar si está ordenado
    is_sorted_quick = all(productos_quick_sort[i].precio <= productos_quick_sort[i+1].precio for i in range(len(productos_quick_sort) - 1))
    print(f"¿Lista ordenada por Quick Sort? {is_sorted_quick}")

    # --- Prueba de Búsqueda Binaria (requiere lista ordenada, usamos la de Quick Sort) ---
    print("\n--- Probando Búsqueda Binaria ---")
    if productos_quick_sort:
        # Elegir un precio para buscar (uno que exista y uno que no)
        target_price_found = productos_quick_sort[len(productos_quick_sort) // 2].precio # Un precio del medio
        target_price_not_found = 9999.99 # Un precio que probablemente no exista

        print(f"\nBuscando producto con precio: ${target_price_found:.2f}")
        found_product = binary_search(productos_quick_sort, target_price_found)
        if found_product:
            print(f"¡Producto encontrado!: {found_product}")
        else:
            print("Producto no encontrado.")

        print(f"\nBuscando producto con precio: ${target_price_not_found:.2f}")
        not_found_product = binary_search(productos_quick_sort, target_price_not_found)
        if not_found_product:
            print(f"¡Producto encontrado!: {not_found_product}")
        else:
            print("Producto no encontrado.")
    else:
        print("La lista de productos está vacía, no se puede realizar la búsqueda binaria.")

