import math

from m373 import iterate


class PrintLogger:
    DISPLAY_LOG = True

    def info(self, msg):
        if self.DISPLAY_LOG:
            print(msg)


logger = PrintLogger()


def f_i(x):
    return 0.2 * x ** 2 + 0.4


def f_ii(x):
    return math.sqrt(5 * x - 2)


print("-" * 10, "i with x0 = 0.5", "-" * 20)
iterate.solve(f_i, estimate=0.5, iterations=5, logger=logger)

print("-" * 10, "i with x0 = 4.5", "-" * 20)
iterate.solve(f_i, estimate=4.5, iterations=5, logger=logger)

print("-" * 10, "i with x0 = 10", "-" * 20)
iterate.solve(f_i, estimate=10, iterations=5, logger=logger)

print("-" * 10, "i with x0 = 4.5", "-" * 20)
iterate.solve(f_i, estimate=4.5, iterations=15, logger=logger)

print("-" * 10, "ii with x0 = 0.5", "-" * 20)
iterate.solve(f_ii, estimate=0.5, iterations=5, logger=logger)

print("-" * 10, "ii with x0 = 4.5", "-" * 20)
iterate.solve(f_ii, estimate=4.5, iterations=5, logger=logger)

print("-" * 10, "ii with x0 = 10", "-" * 20)
iterate.solve(f_ii, estimate=10, iterations=5, logger=logger)

print("-" * 40)
