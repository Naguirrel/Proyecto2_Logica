import argparse
from time import perf_counter

from dpll import dpll
from fuerza_bruta import fuerza_bruta
from utilidades import evaluar_formula, parsear_formula_clausal


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

EJEMPLO_ENTRADA = '[["p", "q"], ["-p", "r"]]'


def copiar_formula(formula):
    return [list(clausula) for clausula in formula]


def verificar_resultado(formula, satisfacible, asignacion):
    if satisfacible:
        return asignacion is not None and evaluar_formula(formula, asignacion)
    return asignacion is None


def medir_algoritmo(algoritmo, formula):
    inicio = perf_counter()
    satisfacible, asignacion, estadisticas = algoritmo(
        copiar_formula(formula), devolver_estadisticas=True
    )
    tiempo = perf_counter() - inicio
    return satisfacible, asignacion, tiempo, estadisticas


def mostrar_resultado(nombre_algoritmo, satisfacible, asignacion, tiempo, estadisticas):
    print(f"{nombre_algoritmo}:")
    print(f"  Satisfacible: {satisfacible}")
    print(f"  Asignacion: {asignacion}")
    print(f"  Tiempo: {tiempo:.6f} segundos")
    print(f"  Combinaciones probadas: {estadisticas['combinaciones_probadas']}")

    if "llamadas_recursivas" in estadisticas:
        print(f"  Llamadas recursivas: {estadisticas['llamadas_recursivas']}")
        print(f"  Ramas podadas: {estadisticas['ramas_podadas']}")


def ejecutar_caso(nombre, formula):
    print("=" * 60)
    print(nombre)
    print(f"Formula: {formula}")

    formula_original = copiar_formula(formula)

    (
        sat_fuerza_bruta,
        asignacion_fuerza_bruta,
        tiempo_fuerza_bruta,
        estadisticas_fuerza_bruta,
    ) = medir_algoritmo(fuerza_bruta, formula)
    sat_dpll, asignacion_dpll, tiempo_dpll, estadisticas_dpll = medir_algoritmo(
        dpll, formula
    )

    mostrar_resultado(
        "Fuerza bruta",
        sat_fuerza_bruta,
        asignacion_fuerza_bruta,
        tiempo_fuerza_bruta,
        estadisticas_fuerza_bruta,
    )
    mostrar_resultado(
        "DPLL", sat_dpll, asignacion_dpll, tiempo_dpll, estadisticas_dpll
    )

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


def ejecutar_demo():
    for nombre, formula in CASOS:
        ejecutar_caso(nombre, formula)


def ejecutar_formula_usuario(formula):
    ejecutar_caso("Formula ingresada", formula)


def leer_formula_interactiva():
    print("Ingrese una formula booleana en forma de clausulas.")
    print(f"Ejemplo: {EJEMPLO_ENTRADA}")

    while True:
        texto = input("Formula CNF: ").strip()
        if not texto:
            print("La entrada no puede estar vacia.")
            continue

        try:
            return parsear_formula_clausal(texto)
        except ValueError as error:
            print(f"Entrada invalida: {error}")


def crear_parser_argumentos():
    parser = argparse.ArgumentParser(
        description="Resuelve SAT para formulas CNF en forma clausal."
    )
    parser.add_argument(
        "formula",
        nargs="?",
        help=f"Formula en forma clausal. Ejemplo: '{EJEMPLO_ENTRADA}'",
    )
    parser.add_argument(
        "--demo",
        action="store_true",
        help="Ejecuta los casos de demostracion incluidos en el proyecto.",
    )
    return parser


def main():
    parser = crear_parser_argumentos()
    argumentos = parser.parse_args()

    if argumentos.demo:
        ejecutar_demo()
        return

    if argumentos.formula is None:
        formula = leer_formula_interactiva()
    else:
        formula = parsear_formula_clausal(argumentos.formula)

    ejecutar_formula_usuario(formula)


if __name__ == "__main__":
    main()
