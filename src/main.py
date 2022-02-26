from typing import List

nums = [1, 1, 2]


# 1 1 2, 1 2 1, 2 1 1

def aaa(nums):
    def dfs(nums, size, dct, visited, path, ans):
        if size == len(path):
            ans.append(path[:])
            return
        for item in nums:
            if visited.get(item, 0) >= dct[item]:
                continue
            visited[item] = visited.get(item, 0) + 1
            path.append(item)
            dfs(nums, size, dct, visited, path, ans)
            item = path.pop()
            visited[item] = visited[item] - 1

    dct = dict()
    size = len(nums)
    for item in nums:
        dct[item] = dct.get(item, 0) + 1
    visited = dict()

    ans = []
    path = []
    nums = list(set(nums))
    dfs(nums, size, dct, visited, path, ans)
    return ans


ans = aaa(nums)
print(ans)