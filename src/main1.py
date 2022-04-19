# def permutation_dfs(nums):
#     def dfs(nums, dct, path, ans):
#         if len(nums) == len(path):
#             ans.append(list(path))
#             return
#         for item in nums:
#             if dct.get(item, False):
#                 continue
#             dct[item] = True
#             path.append(item)
#             dfs(nums, dct, path, ans)
#             path.pop()
#             dct[item] = False
#
#     dct = {}
#     path = []
#     ans = []
#     dfs(nums, dct, path, ans)
#     return ans
#
#
# nums = [1, 2, 3]
# ans = permutation_dfs(nums)
# print(ans)
#
# from collections import deque
#
#
# def permutation_bfs(nums):
#     def bfs(nums):
#         ans = []
#         queue = deque()
#         queue.append([])
#         for item in nums:
#             qsize = len(queue)
#             for _ in range(qsize):
#                 p = queue.popleft()
#                 for i in range(len(p)+1):
#                     q = list(p)
#                     q.insert(i, item)
#                     if len(q) == len(nums):
#                         ans.append(q)
#                     else:
#                         queue.append(q)
#         return ans
#     return bfs(nums)
#
#
# ans = permutation_bfs(nums)
# print(ans)


def bfs(nums):
    ans = []
    queue = [[]]
    for item in nums:
        qsize = len(queue)
        for _ in range(qsize):
            p = queue.pop(0)
            for i in range(len(p) + 1):
                q = list(p)
                q.insert(i, item)
                if len(q) == len(nums):
                    ans.append(q)
                else:
                    queue.append(q)
    return ans


nums = [1, 2, 3]
print(bfs(nums))
