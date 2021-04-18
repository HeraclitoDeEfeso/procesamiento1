# UNTREF
## Procesamiento de Señales
### Trabajo Práctico N°1


| Archivo         | Descripción                                                 |
|-----------------|-------------------------------------------------------------|
| Readme.md       | Este archivo                                                |
| tp1.ipynb       | Jupyter Notebook con el trabajo práctico                    |
| auxnb.py        | Módulo Python con funciones auxiliares para la presentación |
| practica1.py    | Módulo Python con las funciones de la práctica              |

_TODO_

- [X] Agregar enunciado original.
- [X] Agregar notebook vacia.
- [ ] Agregar modelo de exportación en latex.
- [ ] Agregar script de exportación.
- [X] Pasar fórmulas a latex.

Resolver

- [X] 1. Implementar una función que, dada la frecuencia de muestreo y una cantidad de muestras, de-
vuelva la duración en el tiempo de una señal con dichas características.

- [X] 2. Implementar una función que calcule el valor medio de una señal.

- [ ] 3. Implementar una función que construya la señal escalón u[t] con 5 segundos de duración y una
frecuencia de muestreo f s = 5, y la grafique en el intervalo (−2,5;2,5).

- [ ] 4. Graficar la señal anterior en el intervalo (−1;1)

- [ ] 5. Implementar una función que construya la recta y = mx +b y la grafique en el intervalo (−5;5). m
y b deben ser parámetros de entrada.

- [ ] 6. Utilizando la función del punto anterior, generar las rectas y1 = 2x + 1 y y2 = −x. Dibujarlas en
la misma gráfica con líneas gruesas de distintos colores y agregar etiquetas que indiquen a que
ecuación corresponde cada recta. Marcar el punto de intersección.

- [ ] 7. Implementar una función que construya la señal s(t) = Acos(ωt +φ0). La amplitud, la frecuencia
en Hz y la fase inicial deben ser parámetros de entrada, así como la frecuencia de muestreo. La
duración de la señal debe ser siempre de 1 segundo. Debe además graficarla.

- [ ] 8. Utilizando la función del punto anterior, generar una misma señal con frecuencias de muestreo 5,
10, 20, 50 y 100 muestras por segundo y observar las diferencias.

- [ ] 9. En las gráficas del punto anterior, ajustar el rango del eje y para que la visualización sea buena y
agregar etiquetas que muestren el valor de los parámetros.

- [ ] 10. Implementar una función que, dada una señal de entrada s(t), devuelva la señal espejada s(−t).

- [ ] 11. Implementar una función que, dada una señal de entrada s(t), devuelva la señal desplazada s(t −τ)
rellenando con ceros.

- [ ] 12. Implementar una función que, dada una señal de entrada s(t), devuelva la señal escalada s(kt).

- [ ] 13. Generar la función

	<span style="display:block; text-align:center">![
		s(t) = 	2cos(t)	para t en (0, 2π)
			0	en otro caso
	](https://latex.codecogs.com/png.image?s(t)=%5Cleft%5C%7B%5Cbegin%7Bmatrix%7D2%5Ccos(t)&%5Ctext%7Bsi%7D%7B%5Cquad%7Dt%5Cin(0,2%5Cpi)%5C%5C0&%5Ctext%7Ben%5C;otro%5C;caso%7D%5Cend%7Bmatrix%7D%5Cright.)</span>
	
	en el intervalo (−5π;5π). Graficar en dicho intervalo:

	-  s(−t)
	-  s(t −2π)
	-  s(t +2π)
	-  s(−t +π)
	-  s(4t)
	-  s(1/4 t)
	−  s(1/2 t)

	Deben mostrarse las funciones en ocho subplots de la misma ventana de gráfica, indicando en
	respectivas etiquetas que función es cada una.

- [ ] 14. En el punto anterior, ajustar el eje t de las gráficas para que lo muestre en escala de π.

- [ ] 15. Implementar funciones que, dada una señal de entrada, devuelvan la parte par y la parte impar
respectivamente.
