# Recursive fibonacci sequence implementation
def recursive_fib(n):
    if n == 0 or n == 1:
        return n
    return recursive_fib(n - 2) + recursive_fib(n - 1)