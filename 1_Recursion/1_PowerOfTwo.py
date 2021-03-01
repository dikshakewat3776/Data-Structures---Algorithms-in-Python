def PowerOfTwo(n):
    if n == 0:
        return 1
    else:
        power = PowerOfTwo(n-1)
        return power*2


if __name__ == "__main__":
    res = PowerOfTwo(4)
    print(res)

