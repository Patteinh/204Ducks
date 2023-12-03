import sys
import math

def f(t, v):
    return v * math.exp(-t) + (4 - 3 * v) * math.exp(-2 * t) + (2 * v - 4) * math.exp(-4 * t)

def my_quad(func, v, b, n, *args):
    h = (b - v) / n
    s = func(v, *args) + func(b, *args)

    for i in range(1, n, 2):
        s += 4 * func(v + i * h, *args)
    for i in range(2, n-1, 2):
        s += 2 * func(v + i * h, *args)
    return s * h / 3

def average_return_time(v):
    return my_quad(lambda t, v: t * f(t, v), 0, 200, 10000, v)

def standard_deviation(v, mean):
    return math.sqrt(my_quad(lambda t, v, mean: ((t - mean) ** 2) * f(t, v), 0, 200, 10000, v, mean))

def bisection_method(func, lower, upper, tol=1e-12, max_iter=1000):
    iteration = 0
    while (upper - lower) > tol and iteration < max_iter:
        mid = (lower + upper) / 2.0
        if func(mid) == 0:
            return mid
        elif func(mid) * func(lower) < 0:
            upper = mid
        else:
            lower = mid
        iteration += 1
    return (lower + upper) / 2.0

def find_time_for_percentage(v, percentage):
    target = percentage / 100
    cdf = lambda t: my_quad(lambda x, v: f(x, v), 0, t, 1000, v) - target
    return bisection_method(cdf, 0, 100)

def percentage_of_ducks_back(t, v):
    return my_quad(lambda x, v: f(x, v), 0, t, 1000, v) * 100

def ducks(v):
    mean = average_return_time(v)
    stddev = standard_deviation(v, mean)
    p50 = find_time_for_percentage(v, 50)
    p99 = find_time_for_percentage(v, 99)
    p1 = percentage_of_ducks_back(1, v)
    p2 = percentage_of_ducks_back(2, v)
    print(f"Average return time: {int(mean)}m {int((mean % 1) * 60):02d}s")
    print(f"Standard deviation: {stddev:.3f}")
    print(f"Time after which 50% of the ducks are back: {int(p50)}m {int((p50 % 1) * 60):02d}s")
    print(f"Time after which 99% of the ducks are back: {int(p99)}m {int((p99 % 1) * 60):02d}s")
    print(f"Percentage of ducks back after 1 minute: {p1:.1f}%")
    print(f"Percentage of ducks back after 2 minutes: {p2:.1f}%")

