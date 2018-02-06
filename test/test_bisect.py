from unittest import TestCase

import math

from m373 import bisect
from m373.bisect import solve, BisectError


class TestLogger:

    DISPLAY_LOG = False

    def info(self, msg):
        if self.DISPLAY_LOG:
            print(msg)


test_logger = TestLogger()


class TestBisect(TestCase):

    def test_solve_example_2_1(self):
        def f(x):
            return x ** 3 - 0.75 * x ** 2 - 4.5 * x + 4.75

        predicted_effort = bisect.predicted_effort(f, interval=(1.5, 2.0), places=3, logger=test_logger)
        self.assertEqual(predicted_effort, 12)
        ans = bisect.solve(f, interval=(1.5, 2.0), places=3, logger=test_logger)

        self.assertAlmostEqual(ans.solution, 1.779, 3)
        self.assertEqual(predicted_effort, ans.effort)

    def test_solve_exercise_2_1(self):
        def f(x):
            return x * math.exp(-x) - 0.25

        predicted_effort = bisect.predicted_effort(f, interval=(0.3, 0.4), places=3, logger=test_logger)
        ans = bisect.solve(f, interval=(0.3, 0.4), places=3, logger=test_logger)

        self.assertAlmostEqual(ans.solution, 0.357, 3)
        self.assertEqual(predicted_effort, ans.effort)

    def test_solve_exercise_2_2(self):
        def f(x):
            return x * math.cos(x) - math.log(x)

        predicted_effort = bisect.predicted_effort(f, interval=(1.0, 1.6), places=2, logger=test_logger)
        ans = bisect.solve(f, interval=(1.0, 1.6), places=2, logger=test_logger)

        self.assertAlmostEqual(ans.solution, 1.35, 2)
        self.assertEqual(predicted_effort, ans.effort)

    def test_solve_exercise_2_3(self):
        def f(x):
            return x * math.tan(x) - math.log(x)

        # check that s.split fails when the separator is not a string
        with self.assertRaises(BisectError):
            solve(f, interval=(1.0, 4.0), places=2, logger=test_logger)
