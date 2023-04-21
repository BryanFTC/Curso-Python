# En este segundo ejercicios tendréis que crear un script que nos diga si es la hora de 
# ir a casa. Tendréis que hacer uso del modulo time. Necesitaréis la fecha del sistema 
# y poder comprobar la hora.

# En el caso de que sean más de las 7, se mostrará un mensaje y en caso contrario, 
# haréis una operación para calcular el tiempo que queda de trabajo.


import time

# Formateamos el tiempo para que solo se vean las horas y minutos

hora = time.strftime('%H') 
minutos = time.strftime('%M') 

# Creamos una funcion que nos diga si es hora de ir a casa

def hora_de_ir_a_casa(hora, minutos):
    
    hora_restantes = 18 - int(hora)
    minutos_restantes = 59 - int(minutos)
    if int(hora) >= 19:
        print ("Es hora de irse a casa.")
    else:
        print (f"Quedan {hora_restantes} horas y {minutos_restantes} minutos para irnos a casa.")  # noqa: E501

# Ejemplo

print(hora_de_ir_a_casa(13, 30))