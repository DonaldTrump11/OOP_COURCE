def gcd(a, b):
    assert type(a) == int
    assert type(b) == int
    assert a>0 and b>0
    while b:
        a, b = b, a % b
    return a
