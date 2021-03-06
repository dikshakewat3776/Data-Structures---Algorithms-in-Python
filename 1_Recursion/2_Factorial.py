"""
ALGORITHM:
STEP 1 : Recursive case : n! = n * (n-1)1
STEP 2 : Stopping Criteria : For numbers 0 and 1, factorial  of 0 and 1 is 1.
STEP 3 : User Contraints: Only positive numbers are allowed.



WORKING:
4! = fact(4) = nunber*fact(nunber-1) = 4 * fact(3) = 4 * 6 = 24
       fact(3) = nunber*fact(nunber-1) = 3 * fact(2) = 3 * 2 = 6
       fact(2) = nunber*fact(nunber-1) = 2 * fact(1) = 2 * 1 = 2
       fact(1) = 1
       fact(0) = 1
"""


def Factorial(n):
    assert n >= 0, "Number 'n' should be positive."
    if n in [0, 1]:
        return 1
    else:
        return n*Factorial(n-1)


if __name__ == "__main__":
    res = Factorial(-4)
    print(res)

