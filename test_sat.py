import unittest

from dpll import dpll
from fuerza_bruta import fuerza_bruta
from utilidades import evaluar_formula, parsear_formula_clausal


class FormulaClausalTests(unittest.TestCase):
    def test_parsea_formula_clausal_valida(self):
        formula = parsear_formula_clausal('[["p", "q"], ["-p", "r"]]')

        self.assertEqual(formula, [["p", "q"], ["-p", "r"]])

    def test_rechaza_entrada_que_no_es_formula_clausal(self):
        with self.assertRaises(ValueError):
            parsear_formula_clausal('"p and q"')

        with self.assertRaises(ValueError):
            parsear_formula_clausal('["p", "q"]')

        with self.assertRaises(ValueError):
            parsear_formula_clausal('[["-"]]')

    def test_algoritmos_resuelven_formula_ingresada(self):
        formula = parsear_formula_clausal('[["p", "q"], ["-p", "r"]]')

        sat_fuerza_bruta, asignacion_fuerza_bruta = fuerza_bruta(formula)
        sat_dpll, asignacion_dpll = dpll(formula)

        self.assertTrue(sat_fuerza_bruta)
        self.assertTrue(sat_dpll)
        self.assertTrue(evaluar_formula(formula, asignacion_fuerza_bruta))
        self.assertTrue(evaluar_formula(formula, asignacion_dpll))

    def test_algoritmos_detectan_insatisfacible(self):
        formula = parsear_formula_clausal('[["p"], ["-p"]]')

        self.assertEqual(fuerza_bruta(formula), (False, None))
        self.assertEqual(dpll(formula), (False, None))


if __name__ == "__main__":
    unittest.main()
