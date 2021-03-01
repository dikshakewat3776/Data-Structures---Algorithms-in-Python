def GreatestCommonDivisor(a, b):
    assert a >= 0 and b >= 0, "'a' and 'b' should be positive."
    if b == 0:
        return a
    else:
        return GreatestCommonDivisor(b, a%b)


if __name__ == "__main__":
    res = GreatestCommonDivisor(48, 18)
    print(res)

