from dpll import dpll
from fuerza_bruta import fuerza_bruta
from utilidades import evaluar_formula


CASOS = [
    ("Formula vacia", []),
    ("Clausula vacia", [[]]),
    ("Variable unitaria", [["p"]]),
    ("Contradiccion directa", [["p"], ["-p"]]),
    ("Formula satisfacible", [["p", "q"], ["-p", "r"]]),
    (
        "Formula insatisfacible",
        [["p", "q"], ["-p", "q"], ["p", "-q"], ["-p", "-q"]],
    ),
]


def copiar_formula(formula):
    return [list(clausula) for clausula in formula]


def verificar_resultado(formula, satisfacible, asignacion):
    if satisfacible:
        return asignacion is not None and evaluar_formula(formula, asignacion)
    return asignacion is None


def mostrar_resultado(nombre_algoritmo, satisfacible, asignacion):
    print(f"{nombre_algoritmo}:")
    print(f"  Satisfacible: {satisfacible}")
    print(f"  Asignacion: {asignacion}")


def ejecutar_caso(nombre, formula):
    print("=" * 60)
    print(nombre)
    print(f"Formula: {formula}")

    formula_original = copiar_formula(formula)

    sat_fuerza_bruta, asignacion_fuerza_bruta = fuerza_bruta(formula)
    sat_dpll, asignacion_dpll = dpll(formula)

    mostrar_resultado("Fuerza bruta", sat_fuerza_bruta, asignacion_fuerza_bruta)
    mostrar_resultado("DPLL", sat_dpll, asignacion_dpll)

    coinciden = sat_fuerza_bruta == sat_dpll
    verifica_fuerza_bruta = verificar_resultado(
        formula_original, sat_fuerza_bruta, asignacion_fuerza_bruta
    )
    verifica_dpll = verificar_resultado(formula_original, sat_dpll, asignacion_dpll)

    print(f"Coinciden: {coinciden}")
    print(f"Asignacion de fuerza bruta valida: {verifica_fuerza_bruta}")
    print(f"Asignacion de DPLL valida: {verifica_dpll}")

    if formula != formula_original:
        raise AssertionError("La formula original fue modificada")
    if not coinciden:
        raise AssertionError("Los algoritmos no coincidieron")
    if not verifica_fuerza_bruta or not verifica_dpll:
        raise AssertionError("Un algoritmo devolvio una asignacion invalida")


def main():
    for nombre, formula in CASOS:
        ejecutar_caso(nombre, formula)


main()
