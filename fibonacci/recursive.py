# Recursive fibonacci sequence implementation
def recursive_fib(n):
    if n < 2:
        return n
    return recursive_fib(n - 1) + recursive_fib(n - 2)
