"""
.. module:: auxnb
   :platform: Linux, Windows
   :synopsis: Listado de codigo fuente en Jupyter Notebook.

.. moduleauthor:: Alejandro Araneda <eloscurodeefeso@gmail.com>

    El presente módulo :mod:`auxnb` contiene las funciones
    auxiliares para el listado del codigo fuente de un objeto
    en una Jupyter Notebook.
"""
from IPython.display import display, Markdown
from ast import Expr, Str, walk, parse
from astunparse import unparse
from inspect import getsource
from black import format_str, FileMode


def code(objeto):
    """
    Genera un _code fencing_ en Markdown y ordena su visualización

    Se espera que el *objeto* tenga asociado un archivo con su
    código fuente. El resultado puede diferir del código literal ya
    que se analizará el árbol sintáctico abstracto, se eliminarán
    los _docstring_ y se reconstruirá el código. Se creará un salida
    del tipo :class:`IPython.core.display.Markdown`

    :param objeto: entidad de la que se desea el código fuente
    :type objeto: object
    """
    tree = parse(getsource(objeto))
    for node in walk(tree):
        try:
            node.body = list(
                filter(
                    lambda x: not isinstance(x, Expr)
                    or not isinstance(x.value, Str),
                    node.body,
                )
            )
        except BaseException:
            pass
    display(
        Markdown(
            "```python\n"
            + format_str(unparse(tree).strip(), mode=FileMode())
            + "\n```"
        )
    )
