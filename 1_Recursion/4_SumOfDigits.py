def SumOfDigits(n):
    assert n >= 0, "Number 'n' should be positive."
    if n == 0:
        return 0
    else:
        return int(n % 10) + SumOfDigits(n / 10)


if __name__ == "__main__":
    res = SumOfDigits(54)
    print(res)

