from utilidades import obtener_variables, simplificar_formula


def dpll(formula, asignacion=None, devolver_estadisticas=False):
    """Resuelve una formula CNF con busqueda recursiva DPLL basica."""
    estadisticas = {
        "llamadas_recursivas": 0,
        "combinaciones_probadas": 0,
        "ramas_podadas": 0,
    }
    satisfacible, resultado = _dpll(formula, asignacion, estadisticas)

    if devolver_estadisticas:
        return satisfacible, resultado, estadisticas
    return satisfacible, resultado


def _dpll(formula, asignacion, estadisticas):
    estadisticas["llamadas_recursivas"] += 1

    if asignacion is None:
        asignacion_actual = {}
    else:
        asignacion_actual = dict(asignacion)

    if not formula:
        return True, asignacion_actual

    if any(len(clausula) == 0 for clausula in formula):
        estadisticas["ramas_podadas"] += 1
        return False, None

    variables = obtener_variables(formula)
    variable = None
    for candidata in variables:
        if candidata not in asignacion_actual:
            variable = candidata
            break

    if variable is None:
        return False, None

    for valor in [True, False]:
        nueva_asignacion = dict(asignacion_actual)
        nueva_asignacion[variable] = valor
        estadisticas["combinaciones_probadas"] += 1
        formula_simplificada = simplificar_formula(formula, variable, valor)

        satisfacible, resultado = _dpll(
            formula_simplificada, nueva_asignacion, estadisticas
        )
        if satisfacible:
            return True, resultado

    return False, None
