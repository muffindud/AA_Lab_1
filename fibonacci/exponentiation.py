# Exponentiation by squaring Fibonacci sequence
def exponentiation_fib(n):
    if n < 2:
        return n
    i = n - 1
    a, b = 1, 0
    c, d = 0, 1
    while i > 0:
        if i % 2 == 1:
            a, b = d * b + c * a, d * (b + a) + c * b
        c, d = c ** 2 + d ** 2, d * (2 * c + d)
        i = i >> 1
    return a + b
