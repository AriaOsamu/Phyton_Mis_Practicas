"""
Números En Python existen tres tipos diferentes de números integrados: ints, floats, y complex. Sin embargo, en este ejercicio solo trabajarás con intsy floats. ints intsson números enteros. ej 1234. , -10, 20201278. En Python, los números enteros tienen precisión arbitraria ; el número de dígitos solo está limitado por la memoria disponible del sistema anfitrión.

Python puede manejar enteros enormes, tan grandes como la memoria de la computadora aguante.

En Python, los números de punto flotante suelen implementarse usando un tipo de dato similar doubleal de C (con 15 decimales de precisión ), pero su representación puede variar según el sistema operativo y otros detalles de implementación. Esto puede generar algunas sorpresas al trabajar con números de punto flotante, pero suele ser suficiente en la mayoría de los casos. resume para que entienda explicalo de manera simple y divertida
"""

#Ejercicio practico
"""
Tu amigo Chandler planea visitar países exóticos por todo el mundo. Lamentablemente, no se le dan bien las matemáticas. Le preocupa mucho que le estafen en las casas de cambio durante su viaje, y quiere que le hagas una calculadora de divisas. Estas son las especificaciones para la aplicación:
"""

#Tarea 1
# Valor estimado despues del intercambio
"""
Crea la exchange_money()función, tomando 2 parámetros:

budgetLa cantidad de dinero que planea intercambiar.
exchange_rate: La cantidad de moneda nacional equivalente a una unidad de moneda extranjera.
Esta función debe devolver el valor de la moneda intercambiada.

Nota: Si su moneda es USD y desea cambiar USD por EUR con un tipo de cambio de 1.20, entonces 1.20 USD == 1 EUR.

>>> exchange_money(127.5, 1.2)
106.25
"""

def cantidadDivisa(cantidadCambiar, valorUnitario):

    valorFinal = cantidadCambiar * valorUnitario
    return valorFinal

cantidadCambiar = (209); #Dolar
valorUnitario = (26.25); #Lempiras

print(f"El valor que puedes recibir por ${cantidadCambiar} es de L{cantidadDivisa(cantidadCambiar, valorUnitario)}")

# Parte 2
#Calcula la moneda restante despues de un cambio
"""
Crea la get_change()función, tomando 2 parámetros:

budgetCantidad de dinero antes del cambio.
exchanging_valueCantidad de dinero que se toma del presupuesto para ser intercambiada.
"""

def decision(dineroDisponible, parteCambiar):

    sobrante = dineroDisponible - parteCambiar
    return sobrante;

dineroDisponible = 1000;
parteCambiar = 75;

print (f"Le restan ${decision(dineroDisponible, parteCambiar)} de su presupuesto");

# Tarea 3
# Calcular el valor de las facturas
"""
Crea la get_value_of_bills()función, tomando 2 parámetros:

denominationEl valor de un solo billete.
number_of_bills: El número total de facturas.
Esta casa de cambio solo acepta efectivo en cantidades fijas. El total que recibes debe ser divisible por el valor de un billete, lo que puede generar una fracción o resto. Tu función debe devolver únicamente el valor total de los billetes ( excluyendo las fracciones ) que la casa de cambio te entregaría. Lamentablemente, la casa de cambio se queda con el resto o cambio como ganancia.
"""

def factura(valorUnidad, tasaDeCambio):

    totalRecibir = tasaDeCambio // valorUnidad
    return int(totalRecibir);

valorUnidad = 26.25; #Valor de la moneda nacional que se quiere intercambiar
tasaDeCambio = 5500; #Total de lempiras a intgercambiar

print(f"Valor de moneda/unidad: L. {valorUnidad} \n Monto a intercambiar: L. {tasaDeCambio} \n Total de dolares a recibir: ${factura(valorUnidad, tasaDeCambio)}")

#Tarea 4
# Calcular el numero de facturas
"""
Esta función debe devolver la cantidad de billetes que puedes recibir con la cantidad dada . En otras palabras: ¿Cuántos billetes caben en la cantidad inicial? Recuerda: solo puedes recibir billetes enteros , no fracciones, así que divide correctamente. Básicamente, estás redondeando hacia abajo al billete entero más cercano.
"""

def valorBillete(totalMonto, numBillete):
    almacenar = totalMonto // numBillete
    return int(almacenar)

numBillete = 10;
totalMonto = 290;

print(f"El monto total de dinero es: {totalMonto} \nCada billete tiene un valor de {numBillete} \n El total de billetes es de: {valorBillete(totalMonto, numBillete)}")

# Tarea 5
"""
Crea la get_leftover_of_bills()función, tomando amounty denomination.

Esta función debe devolver el importe restante que no se puede recuperar del importe inicial , teniendo en cuenta la denominación de los billetes. Es fundamental saber con exactitud cuánto se queda la cabina.
"""

def restoCabina(montoInicial, denominacion):
    denominacionFaltante = (montoInicial // denominacion)
    sobrante = montoInicial - (denominacionFaltante * denominacion)
    
    return float(sobrante);

montoInicial = 279;
denominacion = 5;


print(f"Monto a retirar: ${montoInicial} \n Denominacion disponible: ${denominacion} \n Importe restante debido a la denominacion: ${restoCabina(montoInicial, denominacion)}")

# Tarea 6
# Calcular el valor del intercambio
"""
Crea la exchangeable_value()función, tomando budget, exchange_rate, spread, y denomination.

El parámetro spreades el porcentaje que se cobra como comisión de cambio, expresado como un número entero. Debe convertirse a decimal dividiéndolo entre 100. Si 1.00 EUR == 1.20 USDel diferencial es 10, el tipo de cambio real será: 1.00 EUR == 1.32 USDporque el 10% de 1,20 es 0,12, y esta comisión adicional se suma al cambio.

Esta función debe devolver el valor máximo de la nueva moneda tras calcular el tipo de cambio más el diferencial . Recuerde que la denominación de la moneda es un número entero y no se puede subdividir.

Nota: El valor devuelto debe ser intde tipo.
"""

# Calcular el porcentaje adicional de la comision
# Base : 26.50 Lempiras = 1 USD

def calcularCambio (montoInicial, tipoCambio, comision, denominacion):
    billeteReal = tipoCambio* (1 + comision / 100)
    montoConvertido = montoInicial / billeteReal
    montoFinal = (montoConvertido // denominacion) * denominacion
    return int(montoFinal);

montoInicial = 1000;
tipoCambio = 1;
comision = 30;
denominacion = 5;

resultado = calcularCambio(montoInicial, tipoCambio, comision, denominacion)
print(f"Monto total que puedes recibir: ${resultado}")