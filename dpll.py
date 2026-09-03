from utilidades import obtener_variables, simplificar_formula


def dpll(formula, asignacion=None):
    """Resuelve una formula CNF con busqueda recursiva DPLL basica."""
    if asignacion is None:
        asignacion_actual = {}
    else:
        asignacion_actual = dict(asignacion)

    if not formula:
        return True, asignacion_actual

    if any(len(clausula) == 0 for clausula in formula):
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
        formula_simplificada = simplificar_formula(formula, variable, valor)

        satisfacible, resultado = dpll(formula_simplificada, nueva_asignacion)
        if satisfacible:
            return True, resultado

    return False, None
