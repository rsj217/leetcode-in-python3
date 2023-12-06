# from src.datastruct.treenode import TreeNode
#
# nums = [-4, -4, 5, None, None, 4, -5, -5, 2, 1, None, None, -2, None, 5, None, None, None, -4, None, None, -4,
#         None, 2, None, -1]
#
# root = TreeNode.deserialize(nums)


# def solve(nums):
#     def dfs(state, path):
#         if len(path) == len(nums):
#             ans.append(path.copy())
#             return
#
#         for item in nums:
#             if state.get(item, False):
#                 continue
#
#             state[item] = True
#             path.append(item)
#             dfs(state, path)
#             path.pop()
#             state[item] = False
#
#     ans = []
#     path = []
#     state = {}
#     dfs(state, path)
#     return ans

def exist(self, board: List[List[str]], word: str) -> bool:
    def dfs(x, y, d, idx):
        if len(word) <= idx:
            return True
        else:
            if col <= x or x < 0 or row <= y or y < 0:
                return False

        if d.get(f"{y}-{x}", False):
            return False
        if board[y][x] != word[idx]:
            return False
        else:
            d[f"{y}-{x}"] = True
            ans = dfs(x + 1, y, d, idx + 1)
            if ans:
                return True
            d[f"{y}-{x}"] = False

            d[f"{y}-{x}"] = True
            ans = dfs(x - 1, y, d, idx + 1)
            if ans:
                return True
            d[f"{y}-{x}"] = False

            d[f"{y}-{x}"] = True
            ans = dfs(x, y + 1, d, idx + 1)
            if ans:
                return True
            d[f"{y}-{x}"] = False

            d[f"{y}-{x}"] = True
            ans = dfs(x, y - 1, d, idx + 1)
            if ans:
                return True
            d[f"{y}-{x}"] = False
        return False

    d = dict()
    idx = 0
    row = len(board)
    col = len(board[0])

    for y in range(row):
        for x in range(col):
            if dfs(x, y, d, idx):
                return True
    return False

if __name__ == '__main__':
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCCED"

    # board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    # word = "ABCB"

    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word ="SEE"

    board = [["A"], ["A"]]
    word = "AAA"

    ans = solve(board, word)
    print(ans)
