# Matrix fibonacci sequence implementation
def matrix_fib(n):
    if n == 0 or n == 1:
        return n
    return matrix_pow([[1, 1], [1, 0]], n)[0][1]


# Matrix multiplication function
def matrix_mult(a, b):
    return [[a[0][0] * b[0][0] + a[0][1] * b[1][0], a[0][0] * b[0][1] + a[0][1] * b[1][1]],
            [a[1][0] * b[0][0] + a[1][1] * b[1][0], a[1][0] * b[0][1] + a[1][1] * b[1][1]]]


# Matrix power function
def matrix_pow(a, n):
    if n == 0:
        return [[1, 0], [0, 1]]
    if n == 1:
        return a
    if n % 2 == 0:
        return matrix_pow(matrix_mult(a, a), n // 2)
    return matrix_mult(a, matrix_pow(matrix_mult(a, a), (n - 1) // 2))
