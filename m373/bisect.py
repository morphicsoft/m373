import collections
import math

from logging import getLogger


class BisectError(Exception):
    pass


def same_sign(a, b):
    return (a < 0) == (b < 0)


def different_sign(a, b):
    return not same_sign(a, b)


def predicted_effort(f, *, interval, places, logger=None):
    k = (math.log10(interval[1] - interval[0]) + places) / math.log10(2)
    return int(math.ceil(k) + 3)


Answer = collections.namedtuple('Answer', 'solution effort')


def solve(f, *, interval, places, logger=None):
    logger = logger or getLogger('solve')
    pe = predicted_effort(f, interval=interval, places=places, logger=logger)
    logger.info("To solve to {} decimal places has predicted effort {}".format(places, pe))
    ar = interval[0]
    br = interval[1]
    n = places
    r = 0

    effort = 0

    def apply_f(x):
        """
        Simple wrapper around the function to be solved, closing over the effort variable in order to increment
        per-function application.

        :param x: Free variable passed into f(x)
        :return: Results of applying f to x.
        """
        nonlocal effort
        effort += 1
        return f(x)

    while True:
        cr = (br + ar) / 2
        if r == 0:
            f_ar = apply_f(ar)
            f_br = apply_f(br)
            logger.info("f_ar={}, f_br={}".format(f_ar, f_br))

        if same_sign(f_ar, f_br):
            raise BisectError("f(ar) and f(br) have the same sign. Cannot bisect f({}) and f({}).".format(ar, br))
        f_cr = apply_f(cr)
        r += 1

        # TODO: factor out the logging/printing from the functionality (and improve on report format)
        logger.info("r={}\tar={:.6f}\tbr={:.6f}\tcr={:.6f}\tf(ar)={:.6f}\tf(br)={:.6f}\tf(cr)={:.6f}\tbr-ar={:.6f}"
                    .format(r, ar, br, cr, f_ar, f_br, f_cr, br - ar))

        if different_sign(f_ar, f_cr):
            br = cr
            f_br = f_cr
        else:
            ar = cr
            f_ar = f_cr

        if (br - ar) < 10 ** (-n):
            rar = round(ar, n)
            # f_rar = f(rar)
            rbr = round(br, n)
            # f_rbr = f(rbr)
            rcr = (rbr + rar) / 2
            f_rcr = apply_f(rcr)
            # TODO: full logic from procedure 2.1 step d
            logger.info("r=*\tar*={:.6f}\tbr*={:.6f}\tcr*={:.6f}\tf(cr*)={:.6f}".format(rar, rbr, rcr, f_rcr))

            if different_sign(f_ar, f_rcr):
                solution = rar
            else:
                solution = rbr
            logger.info("The solution is {} to {} decimal places.".format(solution, n))
            logger.info("Actual effort was {}.".format(effort))

            return Answer(solution=solution, effort=effort)
