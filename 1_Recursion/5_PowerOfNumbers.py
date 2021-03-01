def PowerOfNumbers(base, exp):
    assert base >= 0 and exp >= 0, "'base' and 'exp' should be positive."
    if exp == 0:
        return 1
    elif exp == 1:
        return base
    else:
        return base*PowerOfNumbers(base, exp-1)


if __name__ == "__main__":
    res = PowerOfNumbers(4, 2)
    print(res)

