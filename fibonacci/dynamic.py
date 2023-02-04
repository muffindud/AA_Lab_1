# Dynamic fibonacci sequence implementation
def dynamic_fib(n):
    if n == 0 or n == 1:
        return n
    f0 = 0
    f1 = 1
    for i in range(n - 1):
        f0, f1 = f1, f0 + f1
    return f1
