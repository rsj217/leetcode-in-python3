from src.datastruct.treenode import TreeNode

nums = [-4, -4, 5, None, None, 4, -5, -5, 2, 1, None, None, -2, None, 5, None, None, None, -4, None, None, -4,
        None, 2, None, -1]
root = TreeNode.deserialize(nums)


def solve(node):
    path_max = float("-inf")
    ans = 0
    stack = [node]
    while 0 < len(stack):
        node = stack.pop()
        if path_max <= node.val:
            ans += 1
            path_max = max(path_max, node.val)

        if node.right is not None:
            stack.append(node.right)
        if node.left is not None:
            stack.append(node.left)
    return ans


ans = solve(root)
print(ans)
