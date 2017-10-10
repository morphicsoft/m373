import sympy as sym


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


# iterate.solve(g, estimate=1.3, iterations=5, logger=logger)

if __name__ == '__main__':
    print(g(6.0))
