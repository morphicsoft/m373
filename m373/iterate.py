
def solve(g, *, estimate, iterations=5, logger=None, counter=1):
    if iterations == 0:
        return g(estimate)

    new_estimate = g(estimate)
    logger.info("x_{} = {:.6f}".format(counter, new_estimate))
    return solve(g, estimate=new_estimate, iterations=iterations-1, logger=logger, counter=counter+1)
