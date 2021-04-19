"""
.. module:: practica1
   :platform: Linux, Windows
   :synopsis: Generación de tablas en Jupyter Notebook.

.. moduleauthor:: Alejandro Araneda <eloscurodeefeso@gmail.com>

    El presente módulo :mod:`practica1` contiene las funciones
    necesarias para resolver los ejercicios de la Práctica N°1
    de la materia Procesamiento de Señales dictada en la UNTREF
    en el ciclo lectivo de 2021.
"""
from matplotlib.pyplot import stem, xlim
from numpy import linspace


def duration(signal):
    """
    Calcula la duración de una señal a partir de sus muestras y frecuencia

    :param signal: señal de la que se desea calcular la duración
    :type signal: tuple(list(float), float, float)
    :return: duración de la señal en segundos
    :rtype: float
    """
    return (len(signal[0]) - 1) / signal[1]


def med(signal):
    """
    Calcula el valor medio de una señal discretizada

    :param signal: señal de la que se desea calcular el valor medio
    :type signal: tuple(list(float), float, float)
    :return: valor medio de la señal en la misma unidad que la amplitud
    :rtype: float
    """
    return sum(signal[0]) / len(signal[0])


def heavi(t):
    """
    Función escalón de Heaviside

    Implementa la función escalón de Heaviside con
    semicontinuidad superior (:func:`heavi`(0) = 1)

    :param t: parámetro de la función
    :type t: Union[float, int, complex]
    :return: devuelve 1 ó 0
    :rtype: int
    """
    return 1 if t >= 0 else 0


def sample(func, frec, init, dur):
    """
    Generación de una señal a partir de una función

    Genera una terna que representa a una señal muestreada
    apartir de una función. La función *func* de estar definida en
    el mismo marco temporal que el resto de las funciones y
    debe aceptar un flotante como argumento. La frecuencia
    *frec* debe estar expresada de hercios, el tiempo de inicio
    *init* de la señal muestreada debe ser expresado en segundos
    con respecto al marco temporal compartido por todas las
    funciones. La duración *dur* debe expresarse en segundos.
    Una duración de cero segundo tomará una muestra puntual.

    :param func: función de la que se desea tomar una muestra
    :type func: function
    :param frec: frecuencia de muestreo
    :type frec: float
    :param init: tiempo de inicio del muestreo
    :type init: float
    :param dur: duración del muestreo
    :type dur: float
    :return: una terna que representa una señal muestreada
    :rtype: tuple(list(), float, float)
    """
    return (
        [func(init + t / frec) for t in range(int(frec * dur) + 1)],
        frec,
        init,
    )


def graph(signal, xlimit=None):
    """
    Gráfica de una señal

        :param signal: señal a graficar
        :type signal: tuple(list(float), float, float)
        :param xlim: límites de representación de abscisas
        :type xlim: tuple(float, float), optional
    """
    if xlimit:
        xlim(xlimit)
    stem(
        linspace(
            signal[2], signal[2] + duration(signal), len(signal[0])
        ),
        signal[0],
        linefmt = '--',
    )
