# Escribe una función que pueda decirte si un año (número entero) es bisiesto o no.

def bisiesto(anyo):
    if anyo%4 == 0:
        return "Es bisiesto"
    
    else:
        return "No es bisiesto"