

def aaa(n):
    def dfs(n, dct):
        if n in dct:
            return dct[n]
        ans = 0
        for i in range(1, n+1):
            ans += dfs(i-1, dct) * dfs(n-i, dct)

        dct[n] = ans
        return ans
    return dfs(n, {0:1, 1:1})

ans = aaa(3)
print(ans)