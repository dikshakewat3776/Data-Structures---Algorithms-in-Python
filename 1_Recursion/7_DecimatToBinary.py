def DecimalToBinary(n):
    assert n >= 0, "'a' and 'b' should be positive."
    if n == 0:
        return 0
    else:
        return n % 2 + 10*DecimalToBinary(int(n/2))


if __name__ == "__main__":
    res = DecimalToBinary(7)
    print(res)

