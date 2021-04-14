"""
.. module:: auxnb
   :platform: Linux, Windows
   :synopsis: Listado de codigo fuente en Jupyter Notebook.

.. moduleauthor:: Alejandro Araneda <eloscurodeefeso@gmail.com>

    El presente módulo :mod:`auxnb` contiene las funciones
    auxiliares para el listado del codigo fuente de un objeto
    en una Jupyter Notebook.
"""
from inspect import getsource
from IPython.display import display, Markdown

def code(objeto):
    """
    Genera un _code fencing_ en Markdown y ordena su visualización

    Se espera que el *objeto* tenga asociado un archivo con su
    código fuente. Se creará un salida del tipo 
    :class:`IPython.core.display.Markdown`

    :param objeto: entidad de la que se desea el código fuente
    :type objeto: object
    """
    display(Markdown("```python\n" + getsource(objeto) + "```"))