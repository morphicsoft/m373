import math

from m373 import iterate


class PrintLogger:

    DISPLAY_LOG = True

    def info(self, msg):
        if self.DISPLAY_LOG:
            print(msg)


logger = PrintLogger()


def g(x):
    return x**2 + x - 2


iterate.solve(g, estimate=1.0, iterations=5, logger=logger)

"""
The above form cannot be used for solving sqrt(2) as it does not converge.
"""
