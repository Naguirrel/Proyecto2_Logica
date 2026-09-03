def es_literal_negativa(literal):
    """Indica si una literal representa una negacion."""
    return literal.startswith("-")


def nombre_variable(literal):
    """Obtiene el nombre de variable asociado a una literal."""
    if es_literal_negativa(literal):
        return literal[1:]
    return literal


def obtener_variables(formula):
    """Devuelve una lista ordenada con las variables de una formula CNF."""
    variables = set()
    for clausula in formula:
        for literal in clausula:
            variables.add(nombre_variable(literal))
    return sorted(variables)


def evaluar_literal(literal, asignacion):
    """Evalua una literal con una asignacion parcial o completa."""
    variable = nombre_variable(literal)
    if variable not in asignacion:
        return False

    valor = asignacion[variable]
    if es_literal_negativa(literal):
        return not valor
    return valor


def evaluar_clausula(clausula, asignacion):
    """Evalua una clausula como disyuncion de literales."""
    return any(evaluar_literal(literal, asignacion) for literal in clausula)


def evaluar_formula(formula, asignacion):
    """Evalua una formula CNF como conjuncion de clausulas."""
    return all(evaluar_clausula(clausula, asignacion) for clausula in formula)


def simplificar_formula(formula, variable, valor):
    """Simplifica una formula CNF despues de asignar un valor a una variable."""
    formula_simplificada = []

    for clausula in formula:
        nueva_clausula = []
        clausula_satisfecha = False

        for literal in clausula:
            variable_literal = nombre_variable(literal)

            if variable_literal != variable:
                nueva_clausula.append(literal)
                continue

            literal_verdadera = valor
            if es_literal_negativa(literal):
                literal_verdadera = not valor

            if literal_verdadera:
                clausula_satisfecha = True
                break

        if not clausula_satisfecha:
            formula_simplificada.append(nueva_clausula)

    return formula_simplificada
