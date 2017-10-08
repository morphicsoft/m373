import math


class Exercise(object):
    def __init__(self, a, b, dp):
        self.a = a
        self.b = b
        self.dp = dp
        self.effort = 0

    def __call__(self, *args):
        self.effort += 1
        return self.f(*args)

    @property
    def predicted_effort(self):
        k = (math.log10(self.b - self.a) + self.dp) / math.log10(2)
        return int(math.ceil(k) + 3)


class Exercise_2_1(Exercise):
    def __init__(self):
        super(Exercise_2_1, self).__init__(0, 3, 0.4, 3)

    def f(self, x):
        return x * math.exp(-x) - 0.25


class Exercise_2_2(Exercise):
    def __init__(self):
        super(Exercise_2_2, self).__init__(1.0, 1.6, 2)

    def f(self, x):
        # n.b. Python cos works in radians (which is what we want)
        return x * math.cos(x) - math.log(x)


class Exercise_2_3(Exercise):
    def __init__(self):
        super(Exercise_2_3, self).__init__(1.0, 4.0, 2)

    def f(self, x):
        return x * math.tan(x) - math.log(x)


class Example_2_1(Exercise):
    def __init__(self):
        super(Example_2_1, self).__init__(1.5, 2.0, 3)

    def f(self, x):
        return x ** 3 - 0.75 * x ** 2 - 4.5 * x + 4.75


def same_sign(a, b):
    if a < 0 and b < 0:
        return True
    if a >= 0 and b >= 0:
        return True
    return False


def different_sign(a, b):
    if a < 0:
        return b >= 0
    elif a > 0:
        return b <= 0
    return False


def solve(c):
    f = c()
    print("To solve {} to {} decimal places has predicted effort {}".format(c.__name__, f.dp, f.predicted_effort))
    ar = f.a
    br = f.b
    n = f.dp
    r = 0
    while True:
        cr = (br + ar) / 2
        if r == 0:
            f_ar = f(ar)
            f_br = f(br)
        f_cr = f(cr)

        print("r={}\tar={:.6f}\tbr={:.6f}\tcr={:.6f}\tf(ar)={:.6f}\tf(br)={:.6f}\tf(cr)={:.6f}\tbr-ar={:.6f}" \
              .format(r, ar, br, cr, f_ar, f_br, f_cr, br - ar))
        if (br - ar) < 10 ** (-n):
            rar = round(ar, n)
            f_rar = f(rar)
            rbr = round(br, n)
            f_rbr = f(rbr)
            rcr = (rbr + rar) / 2
            f_rcr = f(rcr)
            # TODO: full logic from procedure 2.1 step d
            print("r=*\tar*={:.6f}\tbr*={:.6f}\tcr*={:.6f}\tf(ar*)={:.6f}\tf(br*)={:.6f}\tf(cr*)={:.6f}" \
                  .format(rar, rbr, rcr, f_rar, f_rbr, f_rcr))

            if different_sign(f_ar, f_rcr):
                solution = rar
            else:
                solution = rbr
            print("The solution is {} to {} decimal places.".format(solution, n))
            print("Actual effort was {}.".format(f.effort))
            return
        r += 1

        if same_sign(f_ar, f_br):
            raise Exception("f(ar) and f(br) have the same sign. Cannot bisect f({}) and f({}.".format(ar, br))

        if different_sign(f_ar, f_cr):
            br = cr
            f_br = f_cr
        elif different_sign(f_br, f_cr):
            ar = cr
            f_ar = f_cr
        else:
            raise Exception("There is no root between {} and {}.".format(ar, br))


solve(Exercise_2_2)
