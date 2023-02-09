from time import perf_counter as time
import matplotlib.pyplot as plt

from fibonacci.binet import binet_fib
from fibonacci.recursive import recursive_fib
from fibonacci.iterative import iterative_fib
from fibonacci.matrix import matrix_fib
from fibonacci.exponentiation import exponentiation_fib
from fibonacci.generator import generator_fib
from fibonacci.lucas import lucas_fib
from fibonacci.lucasrec import lucasrec_fib


def main():
    recursive_range = range(0, 30, 5)
    lucas_range = [5, 12, 21, 42, 70, 101, 256, 589, 812, 1112, 1300]
    n = [501, 631, 794, 1000, 1259, 1585, 1995, 2512, 3162, 3981, 5012, 6310, 7943, 10000, 12589, 15849]

    recursive_time = []
    for i in recursive_range:
        start = time()
        recursive_fib(i)
        end = time()
        recursive_time.append((end - start) * 1e3)
    plt.plot(recursive_range, recursive_time, "-g")
    plt.xlabel("fib(n)")
    plt.ylabel("Time, ms")
    plt.title("Recursive")
    plt.show()

    iterative_time = []
    for i in n:
        start = time()
        iterative_fib(i)
        end = time()
        iterative_time.append((end - start) * 1e3)
    plt.plot(n, iterative_time, "-g")
    plt.xlabel("fib(n)")
    plt.ylabel("Time, ms")
    plt.title("Iterative")
    plt.show()

    matrix_time = []
    for i in n:
        start = time()
        matrix_fib(i)
        end = time()
        matrix_time.append((end - start) * 1e3)
    plt.plot(n, matrix_time, "-g")
    plt.xlabel("fib(n)")
    plt.ylabel("Time, ms")
    plt.title("Matrix")
    plt.show()

    exponentiation_time = []
    for i in n:
        start = time()
        exponentiation_fib(i)
        end = time()
        exponentiation_time.append((end - start) * 1e3)
    plt.plot(n, exponentiation_time, "-g")
    plt.xlabel("fib(n)")
    plt.ylabel("Time, ms")
    plt.title("Exponentiation")
    plt.show()

    generator_time = []
    for i in n:
        start = time()
        generator_fib(i)
        end = time()
        generator_time.append((end - start) * 1e3)
    plt.plot(n, generator_time, "-g")
    plt.xlabel("fib(n)")
    plt.ylabel("Time, ms")
    plt.title("Generator")
    plt.show()

    binet_time = []
    for i in lucas_range:
        start = time()
        binet_fib(i)
        end = time()
        binet_time.append((end - start) * 1e3)
    plt.plot(lucas_range, binet_time, "-g")
    plt.xlabel("fib(n)")
    plt.ylabel("Time, ms")
    plt.title("Binet's formula")
    plt.show()

    lucas_time = []
    for i in lucas_range:
        start = time()
        lucas_fib(i)
        end = time()
        lucas_time.append((end - start) * 1e3)
    plt.plot(lucas_range, lucas_time, "-g")
    plt.xlabel("fib(n)")
    plt.ylabel("Time, ms")
    plt.title("Lucas form")
    plt.show()

    lucasrec_time = []
    for i in n:
        plt.show()
        start = time()
        lucasrec_fib(i)
        end = time()
        lucasrec_time.append((end - start) * 1e3)
    plt.plot(n, lucasrec_time, "-g")
    plt.xlabel("fib(n)")
    plt.ylabel("Time, ms")
    plt.title("Lucas recursive")
    plt.show()


if __name__ == '__main__':
    main()
