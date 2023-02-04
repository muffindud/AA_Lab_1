from math import sqrt


# Closed-form fibonacci sequence implementation
def closed_fib(n):
    return int(((1 + sqrt(5)) ** n - (1 - sqrt(5)) ** n) / (2 ** n * sqrt(5)))
