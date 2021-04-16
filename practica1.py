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