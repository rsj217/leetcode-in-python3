



nums = [1, 5, 3]


ans = []
def subset(nums, index, path):
    if index > len(nums):
        return
    ans.append(path[:])
    for i in range(index, len(nums)):
        path.append(nums[i])
        subset(nums, i+1, path)
        path.pop()

subset(nums, 0, [])
print(ans)

