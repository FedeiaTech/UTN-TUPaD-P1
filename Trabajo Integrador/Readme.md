# Proyecto grupal: Algoritmos de Búsqueda y Ordenamiento en Python

## Integrantes:

* HEREDIA, Giuliana
* IACONO, Federico


## Introducción
En el mundo de la programación, los algoritmos de búsqueda y ordenamiento son pilares fundamentales que impactan directamente el rendimiento y la experiencia de usuario de cualquier aplicación. Comprender los diferentes tipos de algoritmos, así como sus ventajas y desventajas, es crucial para seleccionar la herramienta adecuada en cada escenario y optimizar la eficiencia de nuestros sistemas.

Este proyecto se adentra en el concepto general de estos algoritmos, haciendo un foco especial en dos métodos de ordenamiento clave: Selection Sort y Quick Sort.


## Problema Resuelto - Caso práctico
Para ilustrar la aplicación práctica de estos algoritmos, simulamos un escenario común en el desarrollo de software: **la gestión de un inventario de productos para una tienda en línea**, donde cada Producto posee un nombre y un precio. 

Las operaciones principales que debemos realizar eficientemente son:

**Ordenar productos:** Organizar la lista de productos por precio (ascendente o descendente) para su visualización.

**Buscar productos:** Encontrar rápidamente un producto específico dentro del inventario.


## Algoritmos Implementados
Este repositorio contiene implementaciones y un caso práctico para los siguientes algoritmos:

* ### Ordenamiento Selection Sort (Ordenamiento por Selección)
Un algoritmo de ordenamiento simple y fácil de entender. Funciona seleccionando repetidamente el elemento más pequeño (o más grande) del resto de la lista no ordenada y colocándolo en su posición correcta.

Complejidad Temporal: 
O(n^2) (cuadrática) en todos los casos. Es adecuado solo para conjuntos de datos muy pequeños debido a su eficiencia limitada.


* ### Quick Sort (Ordenamiento Rápido)
Un algoritmo de "divide y vencerás" altamente eficiente y uno de los más rápidos en la práctica para grandes volúmenes de datos. Selecciona un "pivote" y particiona el resto de los elementos en dos subarreglos, según si son menores o mayores que el pivote, ordenando luego estos subarreglos recursivamente.

Complejidad Temporal: 
O(n log n) (logarítmica lineal) en el mejor y promedio caso. Puede degradarse a O(n^2) en el peor caso, aunque esto es raro con una buena estrategia de selección de pivote.


* ### Búsqueda Binaria (Binary Search)
Aunque **no será foco de nuestra investigación**, es importante mencionar este algoritmo de búsqueda extremadamente eficiente que requiere que la lista esté previamente ordenada. Funciona dividiendo repetidamente el intervalo de búsqueda por la mitad hasta encontrar el elemento deseado o determinar que no existe.

Complejidad Temporal: 
O(logn) (logarítmica). Esto la hace ideal para buscar elementos en listas muy grandes, ya que el número de pasos crece muy lentamente con el tamaño de la lista.


## Estructura del Repositorio
Los archivos están organizados de la siguiente manera:

* ### Carpeta de consignas y requisitos para la aprobacion del proyecto: 
Posee diferentes archivos para la conformacion del proyecto y sus condiciones de aprobación.

* ### Archivo de informe final: 
Analisis detallado y muestra de resultados de la investigación realizada.

* ### Archivo de Código Python (.py): 
Los algoritmos y la lógica del caso práctico están encapsulados en archivos .py con su correspondiente documentación