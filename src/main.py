from typing import List


# def solve(profit: List[int], weight: List[int], cap):
#     def dfs(profit: List[int], weight: List[int], selected: int, cur_weight: int):
#         nonlocal ans
#         if len(profit) <= 0:
#             return
#         tp = profit[0]
#         tw = weight[0]
#         if cur_weight + tw <= cap:
#             selected += tp
#             cur_weight += tw
#             ans = max(ans, selected)
#             dfs(profit[1:].copy(), weight[1:].copy(), selected, cur_weight)
#
#             selected -= tp
#             cur_weight -= tw
#             dfs(profit[1:].copy(), weight[1:].copy(), selected, cur_weight)
#
#     ans = 0
#     cur_weight = 0
#     selected = 0
#     dfs(profit, weight, selected, cur_weight)
#     return ans

# def solve(profit: List[int], weight: List[int], cap):
#     def dfs(profit: List[int], weight: List[int], cur_weight: int) -> int:
#         nonlocal ans
#         if len(profit) <= 0:
#             return 0
#         tp = profit[0]
#         tw = weight[0]
#         ans1 = 0
#         if cur_weight + tw <= cap:
#             cur_weight += tw
#             ans1 = tp + dfs(profit[1:].copy(), weight[1:].copy(), cur_weight)
#         cur_weight -= tw
#         ans2 = dfs(profit[1:].copy(), weight[1:].copy(), cur_weight)
#         return max(ans1, ans2)
#
#     cur_weight = 0
#     ans = dfs(profit, weight, cur_weight)
#     return ans


def solve(profit: List[int], weight: List[int], cap):
    def dfs(idx: int, curr_cap: int) -> int:
        if idx == len(profit):
            return 0
        curr_p = profit[idx]
        curr_w = weight[idx]
        
        selected = 0
        if curr_cap + curr_w <= cap:
            selected = curr_p + dfs(idx + 1, curr_cap + curr_w)
        non_selected = dfs(idx + 1, curr_cap)
        return max(selected, non_selected)
    
    return dfs(0, 0)


def solve(profit: List[int], weight: List[int], cap):
    def dfs(idx: int, curr_cap: int) -> int:
        if idx == len(profit):
            return 0
        curr_p = profit[idx]
        curr_w = weight[idx]
        
        if dp[idx][curr_cap] != -1:
            return dp[idx][curr_cap]
        
        selected = 0
        if curr_cap + curr_w <= cap:
            selected = curr_p + dfs(idx + 1, curr_cap + curr_w)
        non_selected = dfs(idx + 1, curr_cap)
        dp[idx][curr_cap] = max(selected, non_selected)
        return dp[idx][curr_cap]
    
    dp = [[-1 for x in range(cap + 1)] for y in range(len(profit))]
    return dfs(0, 0)


profit = [1, 6, 10, 16]
weight = [1, 2, 3, 5]
cap = 7


# ans = solve(profit, weight, cap)
# print(ans)


def solve(nums: List[int], target: int) -> int:
    def dfs(idx: int, target_num: int) -> int:
        if len(nums) <= idx:
            return 1 if target_num == 0 else 0
        ans1 = dfs(idx + 1, target_num + nums[idx])
        ans2 = dfs(idx + 1, target_num - nums[idx])
        return ans1 + ans2
    
    return dfs(0, target)


nums = [1, 1, 1, 1, 1]
target = 3

nums = [1]
target = 1

nums = [43, 9, 26, 24, 39, 40, 20, 11, 18, 13, 14, 30, 48, 47, 37, 24, 32, 32, 2, 26]
target = 47

ans = solve(nums, target)
print(ans)
