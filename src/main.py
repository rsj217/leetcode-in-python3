

nums = [3, 2, -2, 4]

def aaa(nums):
    def dfs(nums, index, path):
        if index == len(nums):
            print(path)
            return
        for i in range(index, len(nums)):
            path.append(nums[i])
            dfs(nums, i+1, path)
            path.pop()
    dfs(nums, 0, [])

aaa(nums)