from unittest import TestCase

from m373.bisect import Exercise_2_1, solve, Exercise_2_2, Exercise_2_3, BisectError


class TestLogger:

    DISPLAY_LOG = False

    def info(self, msg):
        if self.DISPLAY_LOG:
            print(msg)


test_logger = TestLogger()


class TestBisect(TestCase):

    def test_solve_exercise_2_1(self):
        exercise = Exercise_2_1()
        solution = solve(exercise, test_logger)

        self.assertAlmostEqual(solution, 0.357, 3)
        self.assertEqual(exercise.predicted_effort, exercise.effort)

    def test_solve_exercise_2_2(self):
        exercise = Exercise_2_2()
        solution = solve(exercise, test_logger)

        self.assertAlmostEqual(solution, 1.35, 2)
        self.assertEqual(exercise.predicted_effort, exercise.effort)

    def test_solve_exercise_2_3(self):
        exercise = Exercise_2_3()

        # check that s.split fails when the separator is not a string
        with self.assertRaises(BisectError):
            solve(exercise, test_logger)
