def Fibonacci(n):
    assert n >= 0, "Number 'n' should be positive."
    if n in [0, 1]:
        return n
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)


if __name__ == "__main__":
    res = Fibonacci(4)
    print(res)

