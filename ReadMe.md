# Proyecto SAT en Python

Este proyecto implementa un solucionador pequeno de satisfacibilidad booleana
para formulas en forma normal conjuntiva (CNF), usando solo la biblioteca
estandar de Python.

## Archivos

- `main.py`: recibe una formula clausal, ejecuta fuerza bruta y DPLL, y tambien
  permite correr una demostracion con casos satisfacibles e insatisfacibles.
- `fuerza_bruta.py`: resuelve SAT probando todas las asignaciones posibles.
- `dpll.py`: resuelve SAT con una version basica del algoritmo DPLL.
- `utilidades.py`: contiene funciones para evaluar y simplificar formulas CNF.

## Representacion

Una formula CNF se representa como una lista de clausulas, y cada clausula como
una lista de literales en texto.

```python
formula = [
    ["p", "q"],
    ["-p", "r"],
]
```

La literal `"-p"` representa la negacion de `p`.

## Ejecucion

```bash
python main.py
```

El programa solicita una formula en forma de clausulas y muestra el resultado de
fuerza bruta, el resultado de DPLL, si ambos algoritmos coinciden y si las
asignaciones encontradas satisfacen la formula original.

Tambien puede recibirse la formula directamente como argumento:

```bash
python main.py "[['p', 'q'], ['-p', 'r']]"
```

Para ejecutar los casos de demostracion incluidos:

```bash
python main.py --demo
```

## Casos incluidos

- Formula vacia: satisfacible.
- Clausula vacia: insatisfacible.
- Formula unitaria con `p`: satisfacible.
- Contradiccion directa con `p` y `-p`: insatisfacible.
- Formula CNF satisfacible con tres variables.
- Formula CNF insatisfacible con dos variables.
