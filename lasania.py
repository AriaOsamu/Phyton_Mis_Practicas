"""Funciones utilizadas para preparar la hermosa lasaña de Guido.

Aprende sobre Guido, el creador del lenguaje Python:
https://en.wikipedia.org/wiki/Guido_van_Rossum

Este es un *docstring* del módulo, usado para describir la funcionalidad
de un módulo y sus funciones y/o clases.
"""


#TODO: define tus constantes EXPECTED_BAKE_TIME (requerida) y PREPARATION_TIME (opcional) abajo.

#TODO: Elimina 'pass' y completa la función 'bake_time_remaining()' de abajo.
def bake_time_remaining():
    """Calcula el tiempo de horneado restante.

    :param elapsed_bake_time: int - tiempo de horneado que ya ha transcurrido.
    :return: int - tiempo de horneado restante (en minutos) derivado de 'EXPECTED_BAKE_TIME'.

    Función que toma como argumento los minutos reales que la lasaña ha estado en el horno
    y devuelve cuántos minutos aún necesita hornearse
    basándose en el valor de `EXPECTED_BAKE_TIME`.
    """

    pass


#TODO: Define la función 'preparation_time_in_minutes()' abajo.
# Para evitar el uso de *números mágicos* (ver: https://en.wikipedia.org/wiki/Magic_number_(programming)),
# deberías definir una constante PREPARATION_TIME.
# Puedes hacerlo en la línea debajo de la constante 'EXPECTED_BAKE_TIME'.
# Esto facilitará los cálculos y permitirá hacer cambios en tu código más fácilmente.



#TODO: Define la función 'elapsed_time_in_minutes()' abajo.



# TODO: Recuerda volver y agregar *docstrings* a todas tus funciones
#  (puedes copiar y luego modificar el de 'bake_time_remaining'.)


#Definir las variables a utilizar
tiempoHorno = 40; #min
tiempoPreparacion = 60; #min

def tiempoRestante(tiempoHorno, tiempoPreparacion):
    minFaltantes = tiempoPreparacion - tiempoHorno;
    return minFaltantes

print("La lasania debe hornearse por", (tiempoRestante(tiempoHorno, tiempoPreparacion)), "minutos mas." )
