def fib_inner(n):
    if n == 0:
        return 0, 2
    m = n >> 1
    q = -2 if (m & 1) == 1 else 2
    u, v = fib_inner(m)
    u, v = u * v, v * v - q
    if n & 1 == 1:
        u1 = (u + v) >> 1
        return u1, 2*u + u1
    else:
        return u, v


def lucasrec_fib(n):
    if n <= 0:
        return 0
    m = n >> 1
    u, v = fib_inner(m)
    if n & 1 == 1:
        u1 = (u + v) >> 1
        return u * u + u1 * u1
    else:
        return u * v
