dct = {0: 1, 1: 1}


def aaa(n):
    print(aaa.__name__)
    if n in dct:
        return dct[n]
    ans = 0
    for i in range(1, n + 1):
        ans += aaa(i - 1) * aaa(n - i)
    dct[n] = ans
    return ans



aaa(2)