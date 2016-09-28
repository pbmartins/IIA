def root(f, a, b, error):
    m = (a + b) / 2
    if abs(a - b) < error:
        return m
    if f(a) * f(m) <= 0:
        return root(f, a, m, error)
    if f(m) * f(b) <= 0:
        return root(f, m, b, error)
    return None

print(root(lambda x: x**2 - 1, 0, 2, 0.000000001))
