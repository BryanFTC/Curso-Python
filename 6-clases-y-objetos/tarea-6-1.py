# En este ejercicio vais a crear la clase Vehículo la cual tendrá los siguientes atributos:
# Color
# Ruedas
# Puertas
# Por otro lado crearéis la clase Coche la cual heredará de Vehículo y tendrá los siguientes atributos:
# Velocidad
# Cilindrada
# # Por último, tendrás que crear un objeto de la clase Coche y mostrarlo por consola.

class Color:
    pintura = "black"
class Ruedas:
    cantidad = 4
class Puertas:
    cantidad = 4

class Vehiculo:
    color = Color()
    ruedas = Ruedas()
    puertas = Puertas()

class Coche(Vehiculo):
    velocidad = "120 km/h"
    cilindrada = "1500 cc"

c = Coche()