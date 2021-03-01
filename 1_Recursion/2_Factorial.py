def Factorial(n):
    assert n >= 0, "Number 'n' should be positive."
    if n in [0, 1]:
        return 1
    else:
        return n*Factorial(n-1)


if __name__ == "__main__":
    res = Factorial(-4)
    print(res)

