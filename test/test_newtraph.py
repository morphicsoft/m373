from unittest import TestCase

from m373 import newtraph


class TestLogger:

    DISPLAY_LOG = True

    def info(self, msg):
        if self.DISPLAY_LOG:
            print(msg)


test_logger = TestLogger()


class TestNewtonRaphson(TestCase):

    def test_example_2_3(self):
        # Solve cube root of 2, x^3 = 2

        def f(x):
            return x**3 - 2

        solution = newtraph.solve(f, estimate=1.0, iterations=5, logger=test_logger)

        self.assertAlmostEqual(solution, 1.26, 2)
