s = "11106"
s = "12"
s = "226"
s = "0"

# 1 1 10 6

def aaa(s):
    def dfs(s, index, path):
        nonlocal ans
        if index == len(s):
            # ans.append(path[:])
            ans += 1
            return

        for i in range(index, index + 2):
            if i + 1 > len(s):
                return
            n = s[index:i + 1]
            if n.startswith("0"):
                return
            if int(n) > 26:
                return
            path.append(n)
            dfs(s, i + 1, path)
            path.pop()

    ans = 0
    dfs(s, 0, [])
    return ans


ans = aaa(s)
print(ans)
