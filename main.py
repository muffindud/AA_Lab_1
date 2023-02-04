from timeit import default_timer as time

from fibonacci.recursive import recursive_fib
from fibonacci.dynamic import dynamic_fib
from fibonacci.closed import closed_fib
from fibonacci.matrix import matrix_fib


def main():
    n = range(0, 30, 5)

    recursive_time = []
    for i in n:
        start = time()
        recursive_fib(i)
        end = time()
        recursive_time.append(int((end-start) * 1e9))   # nanoseconds
    print(recursive_time)

    dynamic_time = []
    for i in n:
        start = time()
        dynamic_fib(i)
        end = time()
        dynamic_time.append(int((end - start) * 1e9))    # nanoseconds
    print(dynamic_time)

    closed_time = []
    for i in n:
        start = time()
        closed_fib(i)
        end = time()
        closed_time.append(int((end - start) * 1e9))  # nanoseconds
    print(closed_time)

    matrix_time = []
    for i in n:
        start = time()
        matrix_fib(i)
        end = time()
        matrix_time.append(int((end - start) * 1e9))
    print(matrix_time)




if __name__ == '__main__':
    main()
