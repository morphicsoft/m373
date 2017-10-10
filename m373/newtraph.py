import sympy as sym

from m373 import iterate


def solve(f, *, estimate, iterations=5, logger=None, counter=0):
    def df(argx):
        # Use sympy to do the differentiation
        x = sym.symbols('x')
        return sym.diff(f(x), x).evalf(subs={x: argx})

    def g(x):
        return x - f(x) / df(x)

    return iterate.solve(g, estimate=estimate, iterations=iterations, logger=logger, counter=counter)
