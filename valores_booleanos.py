"""
Python representa los valores verdadero y falso con el booltipo `True`, que es un subtipo de `True` int.
Solo existen dos valores en este tipo: `True` y `False`. Estos valores se pueden asignar a 
una variable.

>>> true_variable = True
>>> false_variable = False

Podemos evaluar expresiones booleanas utilizando los operadores `&` and, or`&` y ` not&&`:

>>> true_variable = True and True
>>> false_variable = True and False

>>> true_variable = False or True
>>> false_variable = False or False

>>> true_variable = not False
>>> false_variable = not True

"""

"""
1. En este ejercicio, debes implementar algunas reglas de Pac-Man , el clásico juego arcade de los años 80.

Tienes cuatro reglas que implementar, todas relacionadas con los estados del juego.

Define una eat_ghost()función que reciba dos parámetros ( si Pac-Man tiene una píldora de poder activa y si está tocando un fantasma ) y devuelva un valor booleano que indique si Pac-Man puede comerse un fantasma. La función Truesolo debe devolver un valor booleano si Pac-Man tiene una píldora de poder activa y está tocando un fantasma.

2. Define una score()función que reciba dos parámetros ( si Pac-Man está tocando una píldora de poder y si está tocando un punto ) y devuelva un valor booleano que indique si Pac-Man ha anotado. La función debe devolver un valor booleano Truesi Pac-Man está tocando una píldora de poder o un punto.

3. Define si Pac man pierde:
Define una lose()función que reciba dos parámetros ( si Pac-Man tiene una píldora de poder activa y si está tocando un fantasma ) y devuelva un valor booleano si Pac-Man pierde. La función debe devolver verdadero Truesi Pac-Man está tocando un fantasma y no tiene una píldora de poder activa.

4. Define si pac man gana:
Define la win()función que recibe tres parámetros ( si Pac-Man ha comido todos los puntos , si Pac-Man tiene una píldora de poder activa y si Pac-Man está tocando un fantasma ) y devuelve un valor booleano que indica si Pac-Man gana. La función debe devolver verdadero Truesi Pac-Man ha comido todos los puntos y no ha perdido, según los parámetros definidos en la parte 3.
"""


#Crear una funcion que reciba los valores de la primera parte del juego
def poder(pildoraActiva, comerFantasma):
    pildoraActiva = False;
    comerFantasma = True;

    return pildoraActiva and comerFantasma #Devuelve true si ambos valores son verdaderos

def puntos(poderActivo, llegarPunto):
    poderActivo = False;
    llegarPunto = True;
    return poderActivo or llegarPunto #Devuelve true si al menos uno de los valores es verdadero


def pierde(powerActive, choqueFantasma):
    powerActive = True;
    choqueFantasma = True;
    return (not powerActive) and choqueFantasma #not invierte los valores si es F lo vuelve positivo y viceversa

def gana(totalPuntos, pildoraPactivo, toqueFantasma):
    totalPuntos = True;
    pildoraPactivo = True;
    toqueFantasma = False;

    return totalPuntos and not ((not pildoraPactivo) and toqueFantasma);




