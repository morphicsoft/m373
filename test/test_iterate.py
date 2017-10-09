from unittest import TestCase

import math

from m373 import iterate


class TestLogger:

    DISPLAY_LOG = True

    def info(self, msg):
        if self.DISPLAY_LOG:
            print(msg)


test_logger = TestLogger()


class TestIterate(TestCase):

    def test_solve_root_2(self):
        # From section 1.1

        def g(x):
            return (x + 2/x)/2

        # TODO: could parameterise to accept a stopping criterion (the examples don't use fixed # iterations)
        solution = iterate.solve(g, estimate=1.0, iterations=6, logger=test_logger)

        self.assertAlmostEqual(solution, 1.414, 3)

    def test_solve_example_2_2(self):

        def g(x):
            return 0.25 * math.exp(x)

        solution = iterate.solve(g, estimate=0.35, iterations=4, logger=test_logger)

        self.assertAlmostEqual(solution, 0.357, 3)
