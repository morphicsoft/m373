from unittest import TestCase

import math

from m373 import iterate


class TestLogger:

    DISPLAY_LOG = True

    def info(self, *args):
        if self.DISPLAY_LOG:
            print(*args)


logger = TestLogger()


class TestIterate(TestCase):

    def test_solve_ex_2_9_i(self):

        def f_i(x):
            return 0.2 * x ** 2 + 0.4

        logger.info("-" * 10, "i with x0 = 0.5", "-" * 20)
        # Seems to be converging
        s = iterate.solve(f_i, estimate=0.5, iterations=5, logger=logger)
        self.assertAlmostEqual(s, 0.438, 3)

        logger.info("-" * 10, "i with x0 = 4.5", "-" * 20)
        # Unclear if converging
        s = iterate.solve(f_i, estimate=4.5, iterations=5, logger=logger)
        self.assertAlmostEqual(s, 3.493, 3)

        logger.info("-" * 10, "i with x0 = 10", "-" * 20)
        # Diverges
        iterate.solve(f_i, estimate=10, iterations=5, logger=logger)

        logger.info("-" * 10, "i with x0 = 4.5", "-" * 20)
        # Seems to be slowly converging to 0.438
        iterate.solve(f_i, estimate=4.5, iterations=15, logger=logger)

    def test_solve_ex_2_9_ii(self):

        def f_ii(x):
            return math.sqrt(5 * x - 2)

        logger.info("-" * 10, "ii with x0 = 0.5", "-" * 20)
        # Might be converging to root ~ 4.56
        iterate.solve(f_ii, estimate=0.5, iterations=5, logger=logger)

        logger.info("-" * 10, "ii with x0 = 4.5", "-" * 20)
        # Appears to be slowly converging to root ~ 4.56
        iterate.solve(f_ii, estimate=4.5, iterations=5, logger=logger)

        logger.info("-" * 10, "ii with x0 = 10", "-" * 20)
        # Appears to be converging towards root ~ 4.56
        iterate.solve(f_ii, estimate=10, iterations=5, logger=logger)

        logger.info("-" * 40)

    def test_solve_ex_2_10(self):
        # Attempt to solve sqrt(2)
        def g(x):
            return x ** 2 + x - 2

        # cannot be used for solving sqrt(2) as it does not converge
        s = iterate.solve(g, estimate=1.0, iterations=5, logger=logger)
        self.assertNotAlmostEqual(s, 1.414, 3)

    def test_solve_ex_2_11(self):
        """
        Two rearrangements of x^3 + 4x^2 - 10 = 0
        """

        def f_a(x):
            return x - x ** 3 - 4 * x ** 2 + 10

        def f_b(x):
            inner = 10 / x - 4 * x
            logger.info("Performing sqrt({})".format(inner))
            return math.sqrt(inner)

        logger.info('-' * 40)
        # f_a(x) cannot be used to solve x^3 + 4x^2 - 10 = 0 as it diverges and oscillates.
        iterate.solve(f_a, estimate=1.5, iterations=5, logger=logger)
        logger.info('-' * 40)

        with self.assertRaises(ValueError):
            # f_b(x) cannot be used to solve x^3 + 4x^2 - 10 = 0 as the 3rd iteration attempts to root a -ve number.
            iterate.solve(f_b, estimate=1.5, iterations=5, logger=logger)
        logger.info('-' * 40)
