from itertools import product

from utilidades import evaluar_formula, obtener_variables


def fuerza_bruta(formula, devolver_estadisticas=False):
    """Resuelve una formula CNF probando todas las asignaciones posibles."""
    variables = obtener_variables(formula)
    estadisticas = {"combinaciones_probadas": 0}

    for valores in product([False, True], repeat=len(variables)):
        estadisticas["combinaciones_probadas"] += 1
        asignacion = dict(zip(variables, valores))
        if evaluar_formula(formula, asignacion):
            if devolver_estadisticas:
                return True, asignacion, estadisticas
            return True, asignacion

    if devolver_estadisticas:
        return False, None, estadisticas
    return False, None
