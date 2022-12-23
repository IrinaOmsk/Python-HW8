# Модуль для выполнения опреаций
import sympy


def execute_expr(expr: str) -> str:         # (5+3)*10 -> 80
    """"Принимает на вход строку-пример.
    Возвращает результат примера."""
    return eval(expr)


def solve_eq(expr: str) -> str:                    # x**3 - 8 = 0 -> "2"                                                    # x**2 - 1 = 0 -> "1,-1"
    """Принимает на вход уравнение в виде строки.
    Возвращает список корней уравнения в строку с разделителем"""
    x = sympy.Symbol('x')
    lst = expr.split("=")
    if len(lst) == 2:
        left = lst[0].strip()
        right = lst[1].strip()
        expr = f"{left} - ({right})"
    ans = sympy.solve(expr, x)
    return ", ".join(list(map(str, ans)))


def simpify_pol(expr: str) -> str:           # x**2 + 3*x**2 + 4 -> 4*x**2 + 4
    """"Упрощает введенный многочлен"""
    ans = sympy.simplify(expr)
    return ans
