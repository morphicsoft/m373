import math

from m373 import iterate, bisect


class PrintLogger:
    DISPLAY_LOG = True

    def info(self, msg):
        if self.DISPLAY_LOG:
            print(msg)


logger = PrintLogger()


def f(x):
    """ Example 2.3, cube root of 2
    x^3 = 2
    x^3 - 2 = 0

    So:
    f = x^3 - 2
    f' = 3x^2

    So the Newton-Raphson iteration formula is:

    x_r+1 = x - (x^3 - 2)/3x^2
    """
    return x - (x ** 3 - 2) / (3 * x ** 2)


def g(x):
    """ Exercise 2.12
    xe^-x = 0.25 near x = 0.35

    xe^-x - 0.25 = 0

    So:
    f = xe^-x - 0.25
    f' = uv' - u'v, where u = x, v = e^-x
    so f' = -xe^-x + e^-x
          = e^-x - xe^-x

    So the Newton-Raphson iteration formula is:

    x - (xe^-x - 0.25) / (e^-x - xe^-x)
    x - (x - 0.25 * e^x) / (1 - x)
    """
    return x - (x - 0.25 * math.exp(x)) / (1 - x)


def h(x):
    """ Exercise 2.13
    x^3 + 4x^2 - 10 = 0 near x = 1.5, to 3dp

    f = x^3 + 4x^2 - 10
    f' = 3x^2 + 8x

    So N-R formula is:

    x - (x^3 + 4x^2 - 10)/(3x^2 + 8x)
    """
    return x - (x ** 3 + 4 * x ** 2 - 10) / (3 * x ** 2 + 8 * x)


def make_functions():
    """ Exercise 2.14
    a) estimated values are -2.7, 1.0 and 1.6

    """

    def g(x):
        #  b) i)
        return (x ** 3 + 4) / 5.0

    def h(x):
        """ b) ii)
        f = x^3 - 5x + 4
        f' = 3x^2 - 5
        """

        def f(x):
            return x ** 3 - 5 * x + 4

        def df(x):
            return 3 * x ** 2 - 5

        return x - f(x) / df(x)

    return g, h


iterate.solve(f, estimate=1.0, iterations=5, logger=logger)
print('-' * 40)
iterate.solve(g, estimate=0.35, iterations=5, logger=logger)
print('-' * 40)
iterate.solve(h, estimate=1.5, iterations=5, logger=logger)
print('-' * 40)

print("Exercise 2.14")
funcs = make_functions()
iterate.solve(funcs[0], estimate=1.3, iterations=5, logger=logger)
print('-' * 40)
iterate.solve(funcs[1], estimate=1.3, iterations=5, logger=logger)

#  Ex 2.14 c)
ans = bisect.solve(lambda x: x ** 3 - 5 * x + 4, interval=(1.1, 1.9), places=1, logger=logger)
print("Root found with bisect = ", ans.solution)

"""
n.b. Each N-R iteration is regarded as 2 function evaluations, as f(x) and f'(x) are considered separately
(presumably this means that the method comes up with the derivative f'(x), but unclear how this is done programatically)
"""
