from itertools import product

from utilidades import evaluar_formula, obtener_variables


def fuerza_bruta(formula):
    """Resuelve una formula CNF probando todas las asignaciones posibles."""
    variables = obtener_variables(formula)

    for valores in product([False, True], repeat=len(variables)):
        asignacion = dict(zip(variables, valores))
        if evaluar_formula(formula, asignacion):
            return True, asignacion

    return False, None
