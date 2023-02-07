# Iterative Fibonacci sequence
def iterative_fib(n):
    f0 = 0
    f1 = 1
    for i in range(1, n + 1):
        f0, f1 = f1, f0 + f1
    return f1
