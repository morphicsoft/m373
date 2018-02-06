import math

import sympy as sym

from m373 import iterate


class PrintLogger:
    DISPLAY_LOG = True

    def info(self, msg):
        if self.DISPLAY_LOG:
            print(msg)


logger = PrintLogger()


def f(x):
    return x ** 3 - 5 * x + 4


def df(argx):
    x = sym.symbols('x')
    return sym.diff(f(x), x).evalf(subs={x: argx})


def g(x):
    return x - f(x) / df(x)


def f_3_8(x):
    return math.exp(x) - 0.5 * x - 1.6


def d(x):
    return 0.5 * (x ** 2 * math.log(x) + 1)


# iterate.solve(g, estimate=1.3, iterations=5, logger=logger)

if __name__ == '__main__':
    # print(g(6.0))

    # iterate.solve(d, estimate=0.5, iterations=10, logger=logger)

    def stop(x1, x0):
        delta = abs(x1-x0)
        epsilon = 5 * 10 ** (-7)
        print("delta={}, epsilon={}".format(delta, epsilon))
        return delta <= epsilon
    iterate.solve_2(d, estimate=0.5, stop_f=stop, logger=logger)
