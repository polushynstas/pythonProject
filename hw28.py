def geom_prog(val, pas, n):
    yield val
    for item in range(n - 1):
        val *= pas
        yield val

n = 6
g_1 = geom_prog(10, 3, n)
for i in g_1:
    print(i)

n = 6
g_2 = geom_prog(-2, -5, n)
for i in g_2:
    print(i)