def FindMaxNum(sampleArray, sizeofArray):
    if sizeofArray == 1:
        return sampleArray[0]
    else:
        return max(sampleArray[sizeofArray-1],
                   FindMaxNum(sampleArray, sizeofArray-1))


if __name__ == "__main__":
    res = FindMaxNum([1, 12, 3, 4, 5, 6, 7], 7)
    print(res)

