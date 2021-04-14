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
    return (len(signal[0]) - 1) / signal[1]