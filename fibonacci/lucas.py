# Lucas form of Fibonacci sequence
def lucas_fib(n):
    phi = (1 + 5 ** 0.5) / 2
    return int((phi ** n - (-phi) ** (-n)) / 5 ** 0.5)
