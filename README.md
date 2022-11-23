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
Para el ingreso de las funciones en los diferentes métodos se utiliza una sintaxis diferente a la de el graficador. 

Estas funciones se deben escribir en la sintaxis que se escribirían en Python, de no tener conocimiento de esta sintaxis recomendamos leer la siguiente documentación: https://docs.python.org/es/3/library/math.html

A continuación se agregara una tabla mostrando funciones bien definidas, comparándolas con las antes mostradas para el graficador.

| Graficador| Metodos |
| ----------- |--------- |
| x^2+3| x**2+3|
| log(x+3)/8| math.log(x+3)/8|
|sin(x)| math.sin(x)|
|cos(x)|math.cos(x) |
Tener en cuenta que las funciones se deben escribir en términos de x (minúscula)

### Manejo del error
Para los diferentes métodos se utilizo el error absoluto para los diferentes cálculos. Teniendo esto en cuenta, en las diferentes salidas que muestren el error se debe entender que este error se refiere al error absoluto.

### Tamaño Matrices
En los métodos que se requiere el ingreso de matrices o vectores se tiene una entrada donde se pide que se ingrese el tamaño de la matriz, a pesar de que usted puede ingresar cualquier numero aquí, se recomienda que para el correcto funcionamiento de la aplicación se utilicen numero entre 2 y 5.

### Puntos para metodos de interpolacion
En los métodos de interpolación se piden 2 vectores X y Y, por favor ingresar los puntos de tal forma que si tenemos por ejemplo los puntos (x,y) ([1,3],[4,8]) el vector X quede como [1,4] y el vector Y como [3, 8]

## Metodos para la solucion de sistemas de una variable

### Busqueda incremental
**Entradas:**

- Función: funcion a utilizar. ej math.log(math.sin(x)**2+1)-(1/2)
- Valor inicial: valor inicial del metodo. ej -3
- Delta: tamaño de los intervalos. ej 0.5 
- Iteraciones máximas: Iteraciones máximas. ej 100

**Salida:**
Tabla que mostrara los intervalos donde se encontraron raíces, dicha tabla tendrá las columnas:

- Iteración: Numero de la fila
- Rango: Intervalo donde se encontró la raíz


### Bisección
**Entradas:**

- Función: función a utilizar. ej math.log(math.sin(x)**2+1)-(1/2)
- Intervalo inferior: intervalo inferior. ej 0
- Intervalo Superior: intervalo superior. ej 1
- Tolerancia: Tolerancia en D.C. ej 1e-7
- Iteraciones máximas: Iteraciones máximas. ej 100

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

- Función: funcion a utilizar. ej math.log(math.sin(x)**2+1)-(1/2)
- Intervalo inferior: intervalo inferior. ej 0
- Intervalo Superior: intervalo superior. ej 1
- Tolerancia: Tolerancia en D.C. ej 1e-7
- Iteraciones máximas: Iteraciones máximas. ej 100

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

- Función: función a utilizar. ej math.log(math.sin(x)**2+1)-(1/2)
- Función g: función f sobrescrita como x = ...  ej math.log(math.sin(x)**2+1)-(1/2)
- Valor inicial: Valor inicial. ej -0.5
- Tolerancia: Tolerancia en D.C. ej 1e-7
- Iteraciones máximas: Iteraciones máximas. ej 100

**Salida:**
Tabla que mostrara cada iteración, dicha tabla tendrá las columnas:

- Iteración: Numero de la fila
- x: valor de x
- f(x): función f evaluada en x
- g(x): función g evaluada en x
- E: error absoluto

### Newton-Raphson
**Entradas:**

- Función: función a utilizar. ej math.log(math.sin(x)**2+1)-(1/2)
- Función f': primera derivada de f. ej 2*(1/(math.sin(x)**2 + 1))*(math.sin(x)*math.cos(x))
- Valor inicial: Valor inicial. ej -0.5
- Tolerancia: Tolerancia en D.C. ej 1e-7
- Iteraciones máximas: Iteraciones máximas. ej 100

**Salida:**
Tabla que mostrara cada iteración, dicha tabla tendrá las columnas:

- Iteración: Numero de la fila
- x: valor de x
- f(x): función f evaluada en x
- E: error absoluto

### Secante
**Entradas:**

- Función: función a utilizar. ej math.log(math.sin(x)**2+1)-(1/2)
- Valor inicial x0: Valor inicial de x0. ej 0.5
- Valor inicial x1: Valor inicial de x1. ej 1
- Tolerancia: Tolerancia en D.C. ej 1e-7
- Iteraciones máximas: Iteraciones máximas. ej 100

**Salida:**
Tabla que mostrara cada iteración, dicha tabla tendrá las columnas:

- Iteración: Numero de la fila
- x: valor de x
- f(x): función f evaluada en x
- E: error absoluto

### Raices multiples
**Entradas:**

- Función f: función a utilizar. ej math.exp(x)-x-1
- Función f': primera derivada de f. ej math.exp(x)-1
- Función f'': segunda derivada de f. ej math.exp(x)
- Valor inicial x0: Valor inicial de x0. ej 1
- Tolerancia: Tolerancia en D.C. ej 1e-7
- Iteraciones máximas: Iteraciones máximas. ej 100

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

### Eliminación Gaussiana Simple
**Entradas:**

- Tamaño Matriz (n x n): tamaño de la matriz y del vector
- Matriz: Matriz que se utilizara (A)
- Vector: Vector de respuestas (b)


**Salida:**
- Primero se mostraran los pasos realizados en la eliminacion, estos pasos se mostraran como matrices 
- Posteriormente se mostrara los resultados luego de aplicar sustitución regresiva

### Eliminación Gaussiana Pivote Parcial
**Entradas:**

- Tamaño Matriz (n x n): tamaño de la matriz y del vector
- Matriz: Matriz que se utilizara (A)
- Vector: Vector de respuestas (b)


**Salida:**
- Primero se mostraran los pasos realizados en la eliminacion, estos pasos se mostraran como matrices 
- Posteriormente se mostrara los resultados luego de aplicar sustitución regresiva


### Eliminación Gaussiana Pivote Total
**Entradas:**

- Tamaño Matriz (n x n): tamaño de la matriz y del vector
- Matriz: Matriz que se utilizara (A)
- Vector: Vector de respuestas (b)


**Salida:**
- Primero se mostraran los pasos realizados en la eliminacion, estos pasos se mostraran como matrices 
- Posteriormente se mostrara los resultados luego de aplicar sustitución regresiva



### Factorización Directa LU simple
**Entradas:**

- Tamaño Matriz (n x n): tamaño de la matriz y del vector
- Matriz: Matriz que se utilizara (A)
- Vector: Vector de respuestas (b)


**Salida:**
- Primero se mostraran los pasos realizados en la factorización, en cada paso se mostraran las matrices U, L y M
- Posteriormente se mostrara los resultados luego de aplicar sustitución regresiva

### Croult
**Entradas:**

- Tamaño Matriz (n x n): tamaño de la matriz y del vector
- Matriz: Matriz que se utilizara (A)
- Vector: Vector de respuestas (b)


**Salida:**
- Primero se mostraran los pasos realizados en la factorización, en cada paso se mostraran las matrices U, L y M
- Posteriormente se mostrara los resultados luego de aplicar sustitución regresiva y progresiva

### Doolittle
**Entradas:**

- Tamaño Matriz (n x n): tamaño de la matriz y del vector
- Matriz: Matriz que se utilizara (A)
- Vector: Vector de respuestas (b)


**Salida:**
- Primero se mostraran los pasos realizados en la factorización, en cada paso se mostraran las matrices U, L y M
- Posteriormente se mostrara los resultados luego de aplicar sustitución regresiva y progresiva

### Cholesky
**Entradas:**

- Tamaño Matriz (n x n): tamaño de la matriz y del vector
- Matriz: Matriz que se utilizara (A)
- Vector: Vector de respuestas (b)


**Salida:**
- Primero se mostraran los pasos realizados en la factorización, en cada paso se mostraran las matrices U, L y M
- Posteriormente se mostrara los resultados luego de aplicar sustitución regresiva y progresiva

### Metodos Iterativos
**Entradas:**

- Tamaño Matriz (n x n): tamaño de la matriz y del vector
- Matriz: Matriz que se utilizara (A)
- Vector: Vector de respuestas (b)
- x0: Vector de valores iniciales
- Metodo: Jacobi, Seidel o sor
- Tolerancia: Tolerancia en D.C
- Iteraciones Maximas: Numero de iteraciones Maximas
- w (sor): numero w del metodo de sor, este campo solo se debe llenar si se ejecutara sor


**Salida:**
- Primero se mostrara la matriz T, el vector C y el radio espectral calculado a partir de T
- Posteriormente se mostraran los pasos mostrando por cada uno una matriz con: n, vector de respuestas, error

## Metodos de interpolacion
### Vandermone

**Entradas:**
- Tamaño vectores(n): tamaño del vector
- Vector x: Puntos en x
- Vector y: puntos en y


**Salida:**
- Matriz de vandermone 
-  Coeficientes polinomicos
- Polinomio de vandermonde

### Newton Diferencias Divididas

**Entradas:**
- Tamaño vectores(n): tamaño del vector
- Vector x: Puntos en x
- Vector y: puntos en y


**Salida:**
- tabla de diferencias divididas
- Coeficientes polinomicos
- Polinomio de newton

### Lagrange

**Entradas:**
- Tamaño vectores(n): tamaño del vector
- Vector x: Puntos en x
- Vector y: puntos en y


**Salida:**
- Polinomios de interpolación
- Polinomio de Lagrange

### Spline

**Entradas:**
- Tamaño vectores(n): tamaño del vector
- Vector x: Puntos en x
- Vector y: puntos en y
- Método: lineal, cuadrático o cubico


**Salida:**
- Coeficientes
- Polinomios


## Pseudo Codigo
Esta sección permitirá al usuario ver con mas detalle el funcionamiento de los diferentes métodos implementados.

### Búsqueda incremental
Se debe tener la certeza de que la función es continua.

- Se pide a función
- Se pide al usuario que ingrese un valor inicial (A) para encontrar la raiz de la funcion mas cercana - Se pide al usuario un delta, lo que nos permitira saber le valor de B (B=A+delta).
- Se evalúa los valores A y B en la función para obtener f(A) y f(B)

	   while f(A) * f(B) > 0 do
        A=B
        f(A) = f(B)
        B=B+delta
        f(B)



El ciclo parara cuando haya un cambio de signo, es decir cuando se haya encontrado una raíz en el intervalo. En el caso preciso de Klein se deja correr este ciclo para encontrar todas las raíces posibles hasta n.

### Bisección 
Se debe tener la certeza de que la función es continua.

-Se pide la función tolerancia y numero máximo de iteraciones
-Se pide al usuario A y B, los valores para el intervalo inicial
 -Se crea variable i para contar las iteraciones
-Se evalua A y B obteniendo f(A) y f (B)
-Se revisa si hay una raiz en el intervalo `if f(A) * f(B) <= 0`
-`Error = (A+B)/2^i`
-Ahora encontraremos el valor medio del intervalo `M = (A+B)/2` y lo evaluamos

	while error > tolerance, i < niter, f(M)!=., f(A)*f(B)<0 do:
		if f(A)*f(M)< 0:
			B=M
			f(B) = f(M)
			M = (A+B)/2
			f(M)
			i = i + 1
			Error = (A+B)/2^i
		if f(M)*f(B) < 0
			A=M
			f(A) = f(M)
			M = (A+B)/2
			f(M)
			i = i + 1
			Error = (A+B)/2^i
- Ahora podemos llegar a diferentes paradas.
-  si `error <= tolerance` devolveremos la raíz localizada en el intervalo [A,B] junto con el error.
- Si `i >= niter` Se muestra hasta donde se haya iterado.

### Regla Falsa
Se debe tener la certeza de que la función es continua.

-Se pide la funcion tolerancia y numero maximo de iteraciones
-Se pide al usuario A y B, los valores para el intervalo inicial
 -Se crea variable i para contar las iteraciones
-Se evalua A y B obteniendo f(A) y f (B)
-Se revisa si hay una raiz en el intervalo `if f(A) * f(B) <= 0`
-`Error = |A-B|`
-Ahora encontraremos el valor medio del intervalo `M = A-(f(A)*(A-B))/(f(A)-f(B))` y lo evaluamos 

	while error > tolerance, i < niter, f(M)!=., f(A)*f(B)<0 do:
		if f(A)*f(M)< 0:
			B=M
			f(B) = f(M)
			M = A-(f(A)*(A-B))/(f(A)-f(B))
			f(M)
			i = i + 1
			Error = |A-B|
		if f(M)*f(B) < 0
			A=M
			f(A) = f(M)
			M = A-(f(A)*(A-B))/(f(A)-f(B))
			f(M)
			i = i + 1
			Error = |A-B|

- Ahora podemos llegar a diferentes paradas.
-  si `error <= tolerance` devolveremos la raíz localizada en el intervalo [A,B] junto con el error.
- Si `i >= niter` Se muestra hasta donde se haya iterado.


### Punto fijo
Se debe tener la certeza de que la función f es continua, además la función g debe ser valida.

-Se pide la función f, la función g, tolerancia y numero máximo de iteraciones
-Se pide al usuario un valor X0 que será el valor inicial y se evalúa f(X0)
 -Ahora encontraremos el siguiente valor de x, y lo guardaremos en Xn, luego continuaremos evaluando X0 en g(x). Asi tenemos `Xn = g(X0).`
-Buscamos el `error = |x0 - xn|`

	while error > tolerance, n < niter:
		X0= Xn
		Xn = g(Xn)
		Error = |X0-Xn|
		f(Xn)
		
Ahora podemos llegar a diferentes paradas.
-  si `error <= tolerance` devolveremos la raíz localizada en el intervalo [A,B] junto con el error.
- Si `i >= niter` Se muestra hasta donde se haya iterado.


### Newton Raphson
Se debe tener la certeza de que la función f es continua, además su derivada debe ser diferente de cero en el intervalo dado.

-Se pide la función f, su derivada, tolerancia y numero máximo de iteraciones
-Se pide al usuario un valor X0 que será el valor inicial y se evalúa f(X0) 
-Se evalúa X0 en la derivada para obtener f'(X0)
 -Ahora encontraremos el siguiente valor de x, y lo guardaremos en Xn, luego continuaremos evaluando X0 en g(x). Asi tenemos `Xn = x0-(f(x0)/f'(x0))`
-Buscamos el `error = |x0 - xn|`

	while error > tolerance, n < niter:
		X0= Xn
		X0 = f(Xn)
		f'(x0)
		Xn = x0-(f(x0)/f'(x0))
		Error = |X0-Xn|
		f(Xn)
		
Ahora podemos llegar a diferentes paradas.
-  si `error <= tolerance` devolveremos la raíz localizada en el intervalo [A,B] junto con el error.
- Si `i >= niter` Se muestra hasta donde se haya iterado.


### Secante
Se debe tener la certeza de que la función f es continua

-Se pide la función f, tolerancia y numero máximo de iteraciones
-Se pide al usuario un valor X0 y X1 y se evalúan f(X0) y f(X1)
 -Ahora encontraremos el siguiente valor de x, y lo guardaremos en Xn, luego continuaremos evaluando X0 en g(x). Asi tenemos `Xn = x1-(f(X1)*(x1-x0)/f(x1)-f(x0))`
-Buscamos el `error = |x1 - xn|`

	while error > tolerance, n < niter:
		X0= X1
		x1 = xn
		f(x0)
		f(x1)
		Xn = x1-(f(X1)*(x1-x0)/f(x1)-f(x0))
		f(xn)
		Error = |X1-Xn|
		f(Xn)
		
Ahora podemos llegar a diferentes paradas.
-  si `error <= tolerance` devolveremos la raíz localizada en el intervalo [A,B] junto con el error.
- Si `i >= niter` Se muestra hasta donde se haya iterado.

### Raices Multiples
Se debe tener la certeza de que la función f es continua

-Se pide la función f, la primera derivada de f, la segunda derivada de f, tolerancia y numero máximo de iteraciones
-Se pide al usuario un valor X0 y se evalúa f(X0) f'(X0) y f''(X0)
 -Ahora encontraremos el siguiente valor de x, y lo guardaremos en Xn, luego continuaremos evaluando X0 en g(x). Asi tenemos `Xn = x0-(f(x0)*f'(x0)/f'(x1)^2-f(x0)*f''(x0))`
-Buscamos el `error = |x0 - x1|`

	while error > tolerance, n < niter:
		X0= X1
		f(x0)
		f'(x0)
		f''(x0)
		Xn = x0-(f(x0)*f'(x0)/f'(x1)^2-f(x0)*f''(x0))
		Error = |X1-Xn|
		f(Xn)
		
		
Ahora podemos llegar a diferentes paradas.
-  si `error <= tolerance` devolveremos la raíz localizada en el intervalo [A,B] junto con el error.
- Si `i >= niter` Se muestra hasta donde se haya iterado.
