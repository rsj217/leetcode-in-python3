nums = [1, 2, 3]
k = 3


# nums = [1]
# k = 0


def aaa(nums, k):
    prefix_sum = [0] * (len(nums) + 1)
    for i in range(0, len(nums)):
        prefix_sum[i + 1] = prefix_sum[i] + nums[i]

    ans = 0
    for l in range(len(nums)):
        for r in range(l, len(nums)):
            if prefix_sum[r + 1] - prefix_sum[l] == k:
                ans += 1
    return ans


def aaa(nums, k):
    dct = dict()
    dct[0] = 1
    presum = 0
    ans = 0
    for item in nums:
        presum += item
        ans += dct.get(presum - k, 0)
        dct[presum] = dct.get(presum, 0) + 1
    return ans


ans = aaa(nums, k)
print(ans)
