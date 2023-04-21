# En este ejercicio tendréis que crear un módulo que contenga las operaciones básicas 
# de una calculadora: sumar, restar, multiplicar y dividir.

# Este módulo lo importaréis a un archivo python y llamaréis a las funciones creadas. 
# Los resultados tenéis que mostrarlos por consola.

from operaciones import sumar, restar, multiplicar, dividir   # noqa: F403

a = 15
b = 3

suma = sumar(a, b)

resta = restar(a, b)

multiplicacion = multiplicar(a, b)

divicion = dividir(a, b)

print(suma, resta, multiplicacion, divicion)