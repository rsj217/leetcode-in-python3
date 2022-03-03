s = "25525511135"
n = ["255.255.11.135", "255.255.111.35"]

# s = "0000"
# s = "101023"


def aaa(s):
    def dfs(s, size, index, path, ans):
        if len(path) == 4:
            if size == index:
                ans.append(".".join(path[:]))
            return
        for i in range(index, index+3):
            if i >= size:
                return
            n = s[index:i+1]
            if len(n) > 1 and n.startswith("0"):
                return
            if int(n) > 255:
                return
            path.append(n)
            dfs(s, size, i+1, path, ans)
            path.pop()


    size = len(s)
    index = 0
    path = []
    ans = []
    dfs(s, size, index, path, ans)
    return ans


ans = aaa(s)
print(ans)
