
def f(n):
    a, b = 0, 1
    for i in range(0, n):
        a, b = b, a + b
    return a

print f(3)

""" a, b = b , a + b
first is c = a + b then a = b and then b = c
"""