import math

from m373 import iterate


class PrintLogger:

    DISPLAY_LOG = True

    def info(self, msg):
        if self.DISPLAY_LOG:
            print(msg)


logger = PrintLogger()


"""
Two rearrangements of x^3 + 4x^2 - 10 = 0
"""


def f_a(x):
    return x - x**3 - 4 * x**2 + 10


def f_b(x):
	inner = 10/x - 4 * x
	logger.info("Performing sqrt({})".format(inner))
	return math.sqrt(inner)

print('-' * 40)
iterate.solve(f_a, estimate=1.5, iterations=5, logger=logger)
print('-' * 40)
iterate.solve(f_b, estimate=1.5, iterations=5, logger=logger)
print('-' * 40)

"""
f_a(x) cannot be used to solve x^3 + 4x^2 - 10 = 0 as it diverges and oscillates.
f_b(x) cannot be used to solve x^3 + 4x^2 - 10 = 0 as the 3rd iteration attempts to root a -ve number.
"""
