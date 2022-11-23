# Klein

# <center> Klein Manual de usuario

Bienvenido al manual **Klein**.  Este Manual tiene el proposito de facilitar el uso de las funcionalidades de Klein, explicando los diferentes métodos implementados, sus entradas, salidas y restricciones.

Se recomienda leer este manual antes de utilizar la aplicación, esto para evitar errores inesperados.

# Introducción

Klein es una plataforma fue creada como proyecto final de la materia Análisis numérico. Esta contiene una funcionalidad para graficar y además posee una variedad de métodos para resolver diferentes problemas matemáticos como sistemas de ecuaciones, interpolación, etc.

# Objetivos

El proposito de este proyecto es proporcionar, a quien lo llegase a necesitar, las herramientas necesarias para la solución de diferentes problemas matemáticos.

El principal objetivo de este proyecto es la implementación de los métodos vistos a lo largo del curso.

Además de esto, entre otros objetivos se tiene:

- La correcta implementación de las entradas de cada método.

- La correcta visualización de las salidas de los diferentes métodos.

- La implementación de una página intuitiva y fácil de usar

# Restricciones

Klein es una plataforma web diseñada para computadores (No se implementó un mecanismo **responsive**), por esto se recomienda que su uso se haga exclusivamente en computadores, ya sean portátiles o de sobremesa.

A parte de lo antes mencionado Klein no tiene otras restricciones de hardware, y en lo que respecta a software se recomienda que Klein sea ejecutado en las versiones más actuales de navegadores como FireFox, Edge o Chrome.

# Contenido

A continuación, se mostraran las funcionalidades que se implementaron en Klein.

## Graficador

## Métodos para ecuaciones de una variable

- Búsqueda Incremental

- Bisección

- Posición Falsa

- Punto Fijo

- Método de Newton-Raphson

- Método de la secante

- Múltiples raíces

## Métodos para la solución de sistemas de ecuaciones

- Eliminación Gaussiana simple

- Eliminación Gaussiana pivote parcial

- Eliminación Gaussiana pivote total

- Factorización directa LU simple

- Factorización Croult

- Factorización Doolittle

- Factorización Choeslky

- Métodos iterativos (Jacobi, Gauss-Seidel y SOR)

## Métodos para interpolación

- Vandermonde

- Newton (Diferencias divididas)

- Lagrange

- Spline (Linear, Cuadrático y Cubico)

# Guía de uso

## Graficador

Para implementar el graficador se utilizó la librería Function Plot de javascript.

La función ingresada debe tener cierta sintaxis para funcionar, para tener un mejor entendimiento de esta recomendamos leer la documentación de la librería.

Documentación: https://mauriciopoppe.github.io/function-plot/

A continuación, se mostrarán algunos ejemplos de funciones bien definidas.

| Correcto|

| ----------- |

| x^2+3|

| log(x+3)/8|

|sin(x)|

|cos(x)|

**NOTA** Las funciones siempre deben estar en términos de x (Minúscula) para que el graficador funcione correctamente.

## Cosas a tener en cuenta para la ejecución de los métodos:

### Sintaxis de funciones para los métodos

Para el ingreso de las funciones en los diferentes métodos se utiliza una sintaxis diferente a la del graficador.

Estas funciones se deben escribir en la sintaxis que se escribirían en Python, de no tener conocimiento de esta sintaxis recomendamos leer la siguiente documentación: https://docs.python.org/es/3/library/math.html

A continuación, se agregará una tabla mostrando funciones bien definidas, comparándolas con las antes mostradas para el graficador.

| Graficador| Métodos |

| ----------- |--------- |

| x^2+3| x**2+3|

| log(x+3)/8| math.log(x+3)/8|

|sin(x)| math.sin(x)|

|cos(x)|math.cos(x) |

Tener en cuenta que las funciones se deben escribir en términos de x (minúscula)

### Manejo del error

Para los diferentes métodos se utilizó el error absoluto para los diferentes cálculos. Teniendo esto en cuenta, en las diferentes salidas que muestren el error se debe entender que este error se refiere al error absoluto.

### Tamaño Matrices

En los métodos que se requiere el ingreso de matrices o vectores se tiene una entrada donde se pide que se ingrese el tamaño de la matriz, a pesar de que usted puede ingresar cualquier número aquí, se recomienda que para el correcto funcionamiento de la aplicación se utilicen número entre 2 y 5.

### Puntos para métodos de interpolación

En los métodos de interpolación se piden 2 vectores X y Y, por favor ingresar los puntos de tal forma que si tenemos por ejemplo los puntos (x,y) ([1,3],[4,8]) el vector X quede como [1,4] y el vector Y como [3, 8]

## Métodos para la solución de sistemas de una variable

### Búsqueda incremental

**Entradas:**

- Función: función a utilizar

- Valor inicial: valor inicial del método

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

Tabla que mostrará cada iteración, dicha tabla tendrá las columnas:

- Iteración: Numero de la fila

- a: valor de la izquierda

- xm: a+b/2

- b: valor de la derecha

- f(xm): función evaluada en xm

- E: error absoluto

### Regla Falsa

**Entradas:**

- Función: función a utilizar

- Intervalo inferior: intervalo inferior

- Intervalo Superior: intervalo superior

- Tolerancia: Tolerancia en D.C

- Iteraciones máximas: Iteraciones máximas

**Salida:**

Tabla que mostrará cada iteración, dicha tabla tendrá las columnas:

- Iteración: Numero de la fila

- a: valor de la izquierda

- xm: a+b/2

- b: valor de la derecha

- f(xm): función evaluada en xm

- E: error absoluto

### Punto fijo

**Entradas:**

- Función: función a utilizar

- Función g: función f sobrescrita como x = ...

- Valor inicial: Valor inicial

- Tolerancia: Tolerancia en D.C

- Iteraciones máximas: Iteraciones máximas

**Salida:**

Tabla que mostrará cada iteración, dicha tabla tendrá las columnas:

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

Tabla que mostrará cada iteración, dicha tabla tendrá las columnas:

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

### Raíces múltiples

**Entradas:**

- Función f: función a utilizar

- Función f': primera derivada de f

- Función f'': segunda derivada de f

- Valor inicial x0: Valor inicial de x0

- Tolerancia: Tolerancia en D.C

- Iteraciones máximas: Iteraciones máximas

**Salida:**

Tabla que mostrará cada iteración, dicha tabla tendrá las columnas:

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

Tabla que mostrará cada iteración, dicha tabla tendrá las columnas:

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

- Primero se mostrarán los pasos realizados en la eliminación, estos pasos se mostrarán como matrices

- Posteriormente se mostrará los resultados luego de aplicar sustitución regresiva

### Eliminación Gaussiana Pivote Parcial

**Entradas:**

- Tamaño Matriz (n x n): tamaño de la matriz y del vector

- Matriz: Matriz que se utilizara (A)

- Vector: Vector de respuestas (b)

**Salida:**

- Primero se mostrarán los pasos realizados en la eliminación, estos pasos se mostrarán como matrices

- Posteriormente se mostrará los resultados luego de aplicar sustitución regresiva

### Eliminación Gaussiana Pivote Total

**Entradas:**

- Tamaño Matriz (n x n): tamaño de la matriz y del vector

- Matriz: Matriz que se utilizara (A)

- Vector: Vector de respuestas (b)

**Salida:**

- Primero se mostrarán los pasos realizados en la eliminación, estos pasos se mostrarán como matrices

- Posteriormente se mostrará los resultados luego de aplicar sustitución regresiva

### Factorización Directa LU simple

**Entradas:**

- Tamaño Matriz (n x n): tamaño de la matriz y del vector

- Matriz: Matriz que se utilizara (A)

- Vector: Vector de respuestas (b)

**Salida:**

- Primero se mostrarán los pasos realizados en la factorización, en cada paso se mostrarán las matrices U, L y M

- Posteriormente se mostrará los resultados luego de aplicar sustitución regresiva

### Croult

**Entradas:**

- Tamaño Matriz (n x n): tamaño de la matriz y del vector

- Matriz: Matriz que se utilizara (A)

- Vector: Vector de respuestas (b)

**Salida:**

- Primero se mostrarán los pasos realizados en la factorización, en cada paso se mostrarán las matrices U, L y M

- Posteriormente se mostrará los resultados luego de aplicar sustitución regresiva y progresiva

### Doolittle

**Entradas:**

- Tamaño Matriz (n x n): tamaño de la matriz y del vector

- Matriz: Matriz que se utilizara (A)

- Vector: Vector de respuestas (b)

**Salida:**

- Primero se mostrarán los pasos realizados en la factorización, en cada paso se mostrarán las matrices U, L y M

- Posteriormente se mostrará los resultados luego de aplicar sustitución regresiva y progresiva

### Cholesky

**Entradas:**

- Tamaño Matriz (n x n): tamaño de la matriz y del vector

- Matriz: Matriz que se utilizara (A)

- Vector: Vector de respuestas (b)

**Salida:**

- Primero se mostrarán los pasos realizados en la factorización, en cada paso se mostrarán las matrices U, L y M

- Posteriormente se mostrará los resultados luego de aplicar sustitución regresiva y progresiva

### Métodos Iterativos

**Entradas:**

- Tamaño Matriz (n x n): tamaño de la matriz y del vector

- Matriz: Matriz que se utilizara (A)

- Vector: Vector de respuestas (b)

- x0: Vector de valores iniciales

- Metodo: Jacobi, Seidel o sor

- Tolerancia: Tolerancia en D.C

- Iteraciones Máximas: Numero de iteraciones Máximas

- w (sor): número w del método de sor, este campo solo se debe llenar si se ejecutara sor

**Salida:**

- Primero se mostrará la matriz T, el vector C y el radio espectral calculado a partir de T

- Posteriormente se mostrarán los pasos mostrando por cada uno una matriz con: n, vector de respuestas, error

## Métodos de interpolación

### Vandermonde

**Entradas:**

- Tamaño vectores(n): tamaño del vector

- Vector x: Puntos en x

- Vector y: puntos en y

**Salida:**

- Matriz de vandermonde

-  Coeficientes polinómicos

- Polinomio de vandermonde

### Newton Diferencias Divididas

**Entradas:**

- Tamaño vectores(n): tamaño del vector

- Vector x: Puntos en x

- Vector y: puntos en y

**Salida:**

- tabla de diferencias divididas

- Coeficientes polinómicos

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

- Grafica con intervalos

## Pseudo Código
Esta sección permitirá al usuario ver con mas detalle el funcionamiento de los diferentes métodos implementados.

### Búsqueda incremental
Se debe tener la certeza de que la función es continua.

- Se pide a función
- Se pide al usuario que ingrese un valor inicial (A) para encontrar la raíz de la función mas cercana - Se pide al usuario un delta, lo que nos permitirá saber le valor de B (B=A+delta).
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
-Se revisa si hay una raíz en el intervalo `if f(A) * f(B) <= 0`
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

-Se pide la función tolerancia y numero máximo de iteraciones
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
 -Ahora encontraremos el siguiente valor de x, y lo guardaremos en Xn, luego continuaremos evaluando X0 en g(x). Así tenemos `Xn = g(X0).`
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
 -Ahora encontraremos el siguiente valor de x, y lo guardaremos en Xn, luego continuaremos evaluando X0 en g(x). Así tenemos `Xn = x0-(f(x0)/f'(x0))`
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

### Raíces Múltiples
Se debe tener la certeza de que la función f es continua

-Se pide la función f, la primera derivada de f, la segunda derivada de f, tolerancia y numero máximo de iteraciones
-Se pide al usuario un valor X0 y se evalúa f(X0) f'(X0) y f''(X0)
 -Ahora encontraremos el siguiente valor de x, y lo guardaremos en Xn, luego continuaremos evaluando X0 en g(x). Así tenemos `Xn = x0-(f(x0)*f'(x0)/f'(x1)^2-f(x0)*f''(x0))`
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


### Eliminación Gaussiana Simple

-Pedir al usuario la matriz A

-Pedir al usuario el vector computable B y el número entero n.

  

	For i = 1 < n

		For j - 1 < n + 1

			Leer Aij

  

-Aplicar la eliminación de Gauss a la matriz A

  

	For i = 1 < n - 1

		If Aij = 0

			print "Error!"

		endIf

		For j - i + 1 < n

			Ratio = Aij / Aii

			For k = 1 to n+1

				Ajk = Ajk - Ratio * Aik

  

-Obtener la solución por sustitución regresiva

  

	Xn = An,n+1 / Ann

	For i = n - 1 < 1 (Step: -1)

		Xi = Ai,n+1

		For j = i + 1 < n

			xi = xi - Aij * xj

		xi = xi / Aii

  

-Mostrar la solución

  
	
	for i = 1 < n

		Mostrar xi

  

***Nota:*** Todos los índices de la matriz se asumen a partir de 1.

### Eliminación Gaussiana con pivote parcial

-Pedir al usuario la matriz A

-Pedir al usuario el vector computable B y el número entero n.

  

	For k = 1 until n-1

		For p - k until n

			akk_max = |apk|

		If akk = 0

			Imprimir "Use otro método"

		If not

			if k != p

				Intercambiar la fila k por p

		For i = k + 1 until n

			mik = aij / akk

			If mik <= 1

				For j = k until n + 1

				aij = aij - mik * aik

-Obtener la solución por sustitución progresiva

  
	
	For i = n < 1

		sum = 0

		For j = i + 1 < 1

			sum = sum + aij * xij

		xi = (ain + 1 - sum) / aij

  

### Eliminación Gaussiana con pivote total

-Pedir al usuario la matriz A

-Pedir al usuario el vector computable B y el número entero n.

  

	For k = 1 until n-1

		For p - k until n

			For r = k until n

				akk= max|apr|

		If akk = 0

			Imprimir "Use otro método"

		If not

			if k != p and k != r

				Intercambiar la fila k por p

				Intercambiar columna k por r

		For i = k + 1 until n

			mik = aij / akk

			If mik <= 1

				For j = k until n + 1

					aij = aij - mik * aik

-Obtener la solución por sustitución progresiva

  
	
	For i = n < 1

		sum = 0

		For j = i + 1 < 1

			sum = sum + aij * xij

		xi = (ain + 1 - sum) / aij

  

### Factorización LU (simple)

-Pedir al usuario que introduzca una matriz. La llamaremos *A*.

***Nota:*** Tiene que ser una matriz cuadrada.

-Ahora tomamos el tamaño de la matriz A y lo almacenamos en una variable llamada *n*.

-A continuación, creamos 2 matrices más, las llamamos *L* y *U*. Las matrices *L* y *U* deben tener las siguientes características, ambas deben tener el mismo tamaño que la matriz *A*, todos los elementos diagonales de *L* serán 1 y el resto serán 0. Todos los elementos de *U* serán 0.

-El siguiente paso es crear una variable auxiliar, la llamaremos *M* y su valor inicial es el mismo que el de *A*.

-Mostrar al usuario el paso cero imprimiendo las matrices *L* y *U*.

-Ahora comenzaremos a ejecutar el método

  

	For i = 1 < n - 1

		If a diagonal element == 0

			Imprimir "Usar otro método"

		For j = i + 1 < n
		
			If element Mji != 0

				/* A continuación encontraremos los multiplicadores del pivote. Asignaremos estos elementos de L: */

				Lji = Mji / Mii

			/* Ahora comienza la operación de filas para los elementos de la matriz que están por debajo del elemento Mii. Convirtiéndolos todos en 0 */

		/* Ahora asignamos cada elemento de la fila i de M y de la fila i de U y añadimos 1 a i para que pueda tomar el siguiente elemento de la diagonal */

		/* Imprimir cada paso para que el usuario pueda visualizarlo */

### Factorización LU con pivote parcial

-Pedir al usuario que introduzca una matriz. La llamaremos *A*.

***Nota:*** Tiene que ser una matriz cuadrada.

-Ahora tomamos el tamaño de la matriz A y lo almacenamos en una variable llamada *n*.

-A continuación, creamos 3 matrices más, las llamamos *L*, *P* y *U*. Las matrices *L*, *P* y *U* deben tener las siguientes características, ambas deben tener el mismo tamaño que la matriz *A*, todos los elementos diagonales de *L* serán 1 y el resto serán 0. Todos los elementos de *L* y *P* serán 1 y el resto serán 0. Todos los elementos de _U_ serán 0.

-El siguiente paso es crear una variable auxiliar, la llamaremos *M* y su valor inicial es el mismo que el de *A*.

-Mostrar al usuario el paso cero imprimiendo las matrices *L* y *U*.

-Ahora comenzaremos a ejecutar el método

  

	For i = 1 < n - 1

		/* Para ver si debemos hacer un cambio de filas, miramos el valor absoluto del elemento mayor de los que están debajo del elemento Mii y comparamos. */

		/* Si el valor absoluto del elemento es mayor que el valor absoluto de Mii necesitamos cambiar filas entre la variable auxiliar,*/

		/* y hacemos el mismo cambio en las mismas filas de la matriz P */

		If a diagonal element == 0

			Imprimir "Usar otro método"

		For j = i + 1 < n

			If element Mji != 0

				/* A continuación encontraremos los multiplicadores del pivote. Asignaremos estos elementos de L: */

				Lji = Mji / Mii

			/* Ahora comienza la operación de filas para los elementos de la matriz que están por debajo del elemento Mii. Convirtiéndolos todos en 0 */

		/* Ahora asignamos cada elemento de la fila i de M y de la fila i de U y añadimos 1 a i para que pueda tomar el siguiente elemento de la diagonal */

		/* Imprimir cada paso para que el usuario pueda visualizarlo */

  

### Croult

-Pide al usuario una matriz A. Debe ser una matriz cuadrada.

-Pedir al usuario el vector B y asegurarse de que tiene la misma longitud que la matriz A, y pedir un número entero n.

-A continuación, creamos 2 matrices más, las llamamos L y U. Las matrices L y U deben tener las siguientes características,

-Tener el mismo tamaño que la matriz A

-L tendrá los mismos elementos que están debajo de la diagonal en A pero con el signo contrario. La diagonal en L será la misma que en A, y todos los demás elementos serán 0.

-U tendrá los mismos elementos en A que están por encima de la diagonal con signos opuestos, y tendrá los mismos elementos en la diagonal que A y el resto de los elementos serán 0.

  

	For k = 1 < n

		sum1 = 0

		For p = 1 < k - 1

			sum1 = sum1 + Lkp * Ukp

			Lkk = sqrt(akk + sum1)

		For i = k + 1 < n

			sum2 = 0

			For r = 1 < k - 1

				sum2 = sum2 + Lir * Urk

			Ljk = (akk - sum2)

			For j = k + 1 < n

				sum3 = 0

				For s = 1 < s-1

					sum3 = sum3 + Lks * Usj

					Ukj = (akj-sum3) / Lkk

-Sustitución regresiva

  

	For i = n < n

		sum = 0

		For j = 1 + 1 < n

			sum = sum + aij * xij

		xi = ((ain+1) - sum) / aii

-Sustitución progresiva

  

	For i=1 < n

		sum = 0

		For j = i + 1 < n

			sum = sum + aij * xij

		xi = ((ain+1) - sum) / aii

### Doolittle

-Pide al usuario una matriz A. Debe ser una matriz cuadrada.

-Pedir al usuario el vector B y asegurarse de que tiene la misma longitud que la matriz A, y pedir un número entero n.

-A continuación, creamos 2 matrices más, las llamamos L y U. Las matrices L y U deben tener las siguientes características,

-Tener el mismo tamaño que la matriz A

-L tendrá los mismos elementos que están debajo de la diagonal en A pero con el signo contrario. La diagonal en L será la misma que en A, y todos los demás elementos serán 0.

-U tendrá los mismos elementos en A que están por encima de la diagonal con signos opuestos, y tendrá los mismos elementos en la diagonal que A y el resto de los elementos serán 0.

  

	For k = 1 < n

		sum1 = 0

		For p = 1 < k - 1

			sum1 = sum1 + Lkp * Ukp

		For i = k + 1 < n

			sum2 = 0

			For r = 1 < k - 1

				sum2 = sum2 + Lir * Urk

			Ljk = (akk - sum2) / Ukk

			For j = k + 1 < n

				sum3 = 0

				For s = 1 < s-1

					sum3 = sum3 + Lks * Usj

					Ukj = (akj-sum3)

-Sustitución regresiva

  

	For i = n < n

		sum = 0

		For j = 1 + 1 < n

			sum = sum + aij * xij

		xi = ((ain+1) - sum) / aii

-Sustitución progresiva

  

	For i=1 < n

		sum = 0

		For j = i + 1 < n

			sum = sum + aij * xij

		xi = ((ain+1) - sum) / aii

### Cholesky

-Pide al usuario una matriz A. Debe ser una matriz cuadrada.

-Pedir al usuario el vector B y asegurarse de que tiene la misma longitud que la matriz A, y pedir un número entero n.

-A continuación, creamos 2 matrices más, las llamamos L y U. Las matrices L y U deben tener las siguientes características,

-Tener el mismo tamaño que la matriz A

-L tendrá los mismos elementos que están debajo de la diagonal en A pero con el signo contrario. La diagonal en L será la misma que en A, y todos los demás elementos serán 0.

-U tendrá los mismos elementos en A que están por encima de la diagonal con signos opuestos, y tendrá los mismos elementos en la diagonal que A y el resto de los elementos serán 0.

  

	For k = 1 < n

		sum1 = 0

		For p = 1 < k - 1

			sum1 = sum1 + Lkp * Ukp

			Lkk = sqrt(akk + sum1)

		For i = k + 1 < n

			sum2 = 0

			For r = 1 < k - 1

				sum2 = sum2 + Lir * Urk

			Ljk = (akk - sum2) / Ukk

			For j = k + 1 < n

				sum3 = 0

				For s = 1 < s-1

					sum3 = sum3 + Lks * Usj

					Ukj = (akj-sum3) / Lkk

-Sustitución regresiva

  

	For i = n < n

		sum = 0

		For j = 1 + 1 < n

			sum = sum + aij * xij

		xi = ((ain+1) - sum) / aii

-Sustitución progresiva

  

	For i=1 < n

		sum = 0

		For j = i + 1 < n

			sum = sum + aij * xij

		xi = ((ain+1) - sum) / aii

  

### Jacobi, Gauss Seidel y SOR

-Pedimos al usuario una matriz. Llamamos a la matriz *A*. La matriz debe ser una matriz cuadrada

-Pedimos un vector *B* y nos aseguramos de que tiene la misma longitud que la matriz *A*.

-Ahora pedimos al usuario una aproximación del valor inicial que llamaremos x0, una tolerancia (tol) y nos aseguramos de que no sea negativa, también pedimos un número máximo de iteraciones (Nmax), que también tiene que ser no negativo, l (será 1 si se quiere ejecutar Jacobi, o 2 si se quiere ejecutar Gauss Seidel, y w si se quiere usar el método de la relación)

-Nos aseguramos de que A no tiene ningún 0 en la diagonal, y que el det(*A*) != 0

-Ahora hacemos 3 nuevas matrices, llamadas *D*, *L* y *U*. Todas deben tener el mismo tamaño que *A* y deben tener los siguientes parámetros:

-*D* debe ser una matriz que tenga los mismos elementos de la diagonal principal que tiene la matriz *A* y el resto de los elementos deben ser 0.

-*L* tendrá los mismos elementos que están debajo de la diagonal en *A* pero con el signo contrario. La diagonal de *L* será la misma que la de *A* y el resto de los elementos serán 0.

-*U* tendrá los mismos elementos en *A* que están por encima de la diagonal con los signos opuestos, y tendrá los mismos elementos en la diagonal que *A* y el resto de los elementos serán 0.

La ejecución del método va así:

  

	If l == 1

		/* Jacobi */

		T = D^-1 * (L+U)

		C = D^-1 * N

	If l == 2

		/* Gauss Seidel */

		T = (D-L)^-1 * U

		C = (D-L)^-1 * B

	If l == 3

		/* SOR */

		T = (D-w * L)^-1 * ((1-w) * (D + w * U))

		C = (w * (D-w * L))^-1 * B

-Ahora encontramos y hacemos la radiancia espectral como el valor absoluto de los mayores valores propios asegurándonos de que son menores que 1.

-Ahora hacemos un contador para las iteraciones que empieza por 0, una variable para el error que empieza por 1, y una variable para la antigua X, la llamaremos Xant, y la iniciaremos como Xant = x0 nuestra aproximación inicial

-Ahora hacemos un ciclo, mientras el Error > la tolerancia, iteraciones (contador) < Nmax

  
	
	Xact = Xant * T + C

	Error = norm of Xant - Xact

	Xant = Xact

	Counter++

### Método de Vandermonde

- Se solicita la entrada, esta consta de dos vectores x y f(x) o y.

- Se construye la matriz de Vandermonde a partir del vector x.

- Se multiplica la inversa de la matriz de Vandermonde por el vector y y se obtienen los coeficientes.
- El método retorna la matriz de Vandermonde y los coeficientes del polinomio de interpolación.

### Método de de Spline

1. Se solicita la entrada, esta consta de dos vectores x y f(x), y un argumento d que corresponde a el grado de los polinomios, lineales(1),cuadraticos(2) y cubicos(3).

2. Segun el parametro d se hace lo siguiente:

		Si d=1

			Para i = 0 hasta n-1

				Mi = (y(xi+1) – y(xi)) / (xi+1 -xi)

				p(x) = (y(xi+1)-y(xi)) = Mi∗(x-xi)
	
		Si d = 2

			Para i = 1 hasta n

				p(x) = Ai∗xi 2 + Bi∗xi + Ci

			Para i = 2 hasta n

				p(x) = 2∗Ai-1∗xi-1 + Bi-1 = 2∗Ai∗xi-1 + Bi

			Finalmente

				p(x) = 2∗Ai-1∗xn + Bi-1=0
		
				p(x) = 2∗Ai∗xn + Bi = 0

		Si d=3

			Para i = 1 hasta n

				p(X) = Ai∗Xi 3 + Bi∗xi 2 + Ci∗xi + Di

			Para i = 2 hasta n

				p(X) = 3∗Ai-1∗xi-1 2 + 2∗Bi-1∗xi-1 + Ci-1 = 3∗Ai∗xi-1 2 + 2∗Bi∗Xi-1+ Ci

			Para i = 3 hasta n

				p(X) = 6∗Ai-1∗Xi-1+ 2∗Bi-1 = 6∗Ai-1∗Xi + 2∗Bi-1

			Finalmente

				p(X) = 6∗Ai-1∗X0 + Bi-1= 0

				p(X) = 6∗Ai∗Xn + Bi = 0

4.El método retorna una lista con los coeficientes de cada polinomio.

### Método de Newton de interpolación

- Se solicita la entrada, esta consta de dos vectores x y f(x) o y.

- Se construye la tabla de diferencias divididas asi:

		Tabla = matriz(nxn) # Donde n es la longitud de los datos de entrada

			Para j=1 hasta n

				Para i=1 hasta n
	
					Tabla[i][j] <- (Tabla[i+1][j-1] - Tabla[i][j-1]) / (x[i+j]-x[i])

- Se sacan los coeficientes del polinomio que corresponden a la primera fila de la Tabla.

- El metodo retorna la tabla de diferencias divididas y los coeficientes del polinomio de interpolacion

### Método de Lagrange

- Se solicita la entrada, esta consta de dos vectores x y f(x) o y.

- Se construye la tabla de diferencias divididas asi:

		Tabla = matriz(nxn) # Donde n es la longitud de los datos de entrada

			Para i=0 hasta n

				Para j=0 hasta n

					si j != i #Evitamos la diagonal

						paux=[1 - x[j]]

						Li=Convolucion(Li,paux)

						den=den*(x[i]-x[j])

				Tabla[i,toda la columna]=y[i]*Li/den

- Se suman las columnas de la tabla y se obtienen los coeficientes.

- El método retorna la tabla de diferencias divididas y los coeficientes del polinomio de interpolación.
