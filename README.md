# Klein
# <center> Klein Manual de usuario
Bienvenido al manual **Klein**.  Este Manual tiene el proposito de facilitar el uso de las funcionalidades de Klein, explicando los diferentes metodos implementados, sus entradas, salidas y restricciones.
Se recomienda leer este manual antes de utilizar la aplicación, esto para evitar errores inesperados. 

# Introducción 
Klein es una plataforma fue creada como proyecto final de la materia Análisis numérico. Esta contiene una funcionalidad para graficar y además posee una variedad de métodos para resolver diferentes problemas matemáticos como sistemas de ecuaciones, interpolación, etc. 

# Objetivos
El proposito de este proyecto es proporcionar, a quien lo llegase a necesitar, las herramientas necesarias para la solución de diferentes problemas matemáticos. 

El principal objetivo de este proyecto es la implementación de los métodos vistos a lo largo del curso.

Además de esto, entre otros objetivos se tiene:

- La correcta implementación de las entradas de cada método.
- La correcta  visualización de las salidas de los diferentes métodos.
- La implementación de una pagina intuitiva y fácil de usar 

# Restricciones
Klein es una plataforma web diseñada para computadores (No se implemento un mecanismo **responsive**), por esto se recomienda que su uso se haga exclusivamente en computadores, ya sean portátiles o de sobremesa. 

A parte de lo antes mencionado Klein no tiene otras restricciones de hardware, y en lo que respecta a software se recomienda que Klein sea ejecutado en las versiones mas actuales de navegadores como FireFox, Edge o Chrome.

# Contenido
A continuación se mostraran las funcionalidades que se implementaron en Klein.
## Graficador
## Métodos para ecuaciones de una variable
- Busqueda Incremental
- Biseccion
- Posicion Falsa
- Punto Fijo
- Metodo de Newton-Raphson
- Método de la secante
- Múltiples raíces 
## Métodos para la solución de sistemas de ecuaciones
- Eliminacion Gaussiana simple
- Eliminacion Gaussiana pivote parcial
- Eliminacion Gaussiana pivote total
- Factorizacion directa LU sumple
- Factorizacion Croult
- Factorizacion Doolittle
- Factorizacion Choeslky
- Métodos iterativos (Jacobi, Gauss-Seidel y SOR)
## Métodos para interpolación
- Vandermone
- Newton (Diferencias divididas)
- Lagrange
- Spline (Linear, Cuadrático y Cubico)

# Guia de uso 

## Graficador
Para implementar el graficador se utilizo la librería Function Plot de javascript.

La función ingresada debe tener cierta sintaxis para funcionar, para tener un mejor entendimiento de esta recomendamos leer la documentación de la librería. 
Documentación: https://mauriciopoppe.github.io/function-plot/

A continuación  se mostraran algunos ejemplos de funciones bien definidas.

| Correcto|
| ----------- |
| x^2+3|
| log(x+3)/8|
|sin(x)|
|cos(x)|

**NOTA** Las funciones siempre deben estar en términos de x (Minúscula) para que el graficador funcione correctamente. 

## Cosas a tener en cuenta para la ejecución de los métodos:
### Sintaxis de funciones para los metodos
Para el ingreso de las funciones en los diferentes metodos se utiliza una sintaxis diferente a la de el graficador. 

Estas funciones se deben escribir en la sintaxis que se escribirían en Python, de no tener conocimiento de esta sintaxis recomendamos leer la siguiente documentación: https://docs.python.org/es/3/library/math.html

A continuación se agregara una tabla mostrando funciones bien definidas, comparándolas con las antes mostradas para el graficador.

| Graficador| Metodos |
| ----------- |--------- |
| x^2+3| x**2+3|
| log(x+3)/8| math.log(x+3)/8|
|sin(x)| math.sin(x)|
|cos(x)|math.cos(x) |

### Manejo del error
Para los diferentes métodos se utilizo el error absoluto para los diferentes cálculos. Teniendo esto en cuenta, en las diferentes salidas que muestren el error se debe entender que este error se refiere al error absoluto.

### Tamaño Matrices
En los métodos que se requiere el ingreso de matrices o vectores se tiene una entrada donde se pide que se ingrese el tamaño de la matriz, a pesar de que usted puede ingresar cualquier numero aquí, se recomienda que para el correcto funcionamiento de la aplicación se utilicen numero entre 2 y 5.

## Metodos para la solucion de sistemas de una variable

### Busqueda incremental
**Entradas:**

- Función: funcion a utilizar
- Valor inicial: valor inicial del metodo
- Delta: tamaño de los intervalos
- Iteraciones máximas: Iteraciones máximas

**Salida:**
Tabla que mostrara los intervalos donde se encontraron raíces, dicha tabla tendrá las columnas:

- Iteración: Numero de la fila
- Rango: Intervalo donde se encontró la raíz


### Bisección
**Entradas:**

- Función: función a utilizar
- Intervalo inferior: intervalo inferior
- Intervalo Superior: intervalo superior
- Tolerancia: Tolerancia en D.C
- Iteraciones máximas: Iteraciones máximas

**Salida:**
Tabla que mostrara cada iteración, dicha tabla tendrá las columnas:

- Iteración: Numero de la fila
- a: valor de la izquierda
- xm: a+b/2
- b: valor de la derecha
- f(xm): función evaluada en xm
- E: error absoluto

### Regla Falsa
**Entradas:**

- Función: funcion a utilizar
- Intervalo inferior: intervalo inferior
- Intervalo Superior: intervalo superior
- Tolerancia: Tolerancia en D.C
- Iteraciones máximas: Iteraciones máximas

**Salida:**
Tabla que mostrara cada iteración, dicha tabla tendrá las columnas:

- Iteración: Numero de la fila
- a: valor de la izquierda
- xm: a+b/2
- b: valor de la derecha
- f(xm): funcion evaluada en xm
- E: error absoluto

### Punto fijo
**Entradas:**

- Función: función a utilizar
- Función g: función f sobrescrita como x = ...
- Valor inicial: Valor inicial
- Tolerancia: Tolerancia en D.C
- Iteraciones máximas: Iteraciones máximas

**Salida:**
Tabla que mostrara cada iteración, dicha tabla tendrá las columnas:

- Iteración: Numero de la fila
- x: valor de x
- f(x): función f evaluada en x
- g(x): función g evaluada en x
- E: error absoluto

### Newton-Raphson
**Entradas:**

- Función: función a utilizar
- Función f': primera derivada de f
- Valor inicial: Valor inicial
- Tolerancia: Tolerancia en D.C
- Iteraciones máximas: Iteraciones máximas

**Salida:**
Tabla que mostrara cada iteración, dicha tabla tendrá las columnas:

- Iteración: Numero de la fila
- x: valor de x
- f(x): función f evaluada en x
- E: error absoluto

### Secante
**Entradas:**

- Función: función a utilizar
- Valor inicial x0: Valor inicial de x0
- Valor inicial x1: Valor inicial de x1
- Tolerancia: Tolerancia en D.C
- Iteraciones máximas: Iteraciones máximas

**Salida:**
Tabla que mostrara cada iteración, dicha tabla tendrá las columnas:

- Iteración: Numero de la fila
- x: valor de x
- f(x): función f evaluada en x
- E: error absoluto

### Raices multiples
**Entradas:**

- Función f: función a utilizar
- Función f': primera derivada de f
- Función f'': segunda derivada de f
- Valor inicial x0: Valor inicial de x0
- Tolerancia: Tolerancia en D.C
- Iteraciones máximas: Iteraciones máximas

**Salida:**
Tabla que mostrara cada iteración, dicha tabla tendrá las columnas:

- Iteración: Numero de la fila
- x: valor de x
- f(x): función f evaluada en x
- E: error absoluto

## Métodos para la solución de sistemas de ecuaciones 
### Eliminación Gaussiana Simple
**Entradas:**

- Tamaño Matriz (n x n): tamaño de la matriz y del vector
- Matriz: Matriz que se utilizara (A)
- Vector: Vector de respuestas (b)


**Salida:**
Tabla que mostrara cada iteración, dicha tabla tendrá las columnas:

- Iteración: Numero de la fila
- x: valor de x
- f(x): función f evaluada en x
- E: error absoluto
