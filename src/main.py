
from src.datastruct.treenode import TreeNode


def pathsum(root: TreeNode, targetSum:int):
    
    ans = []
    def dfs(root, path):
        if root is None:
            return
        # 叶子节点
        if root.left is None and root.right is None:
            if root.val + targetSum == sum(path):
                ans.append(path.copy())
            return
            
        path.append(root.val)
        dfs(root.left, path)
        dfs(root.right,path)
        path.pop()
        
    dfs(root, targetSum)
    return ans



def solution(self, node):
    
    def dfs(path): # 不需要改变的量，就用闭包读 solution 函数定义的量
        print(node, ans) # 这里使用 闭包的量
    
    ans = []
    path = []
    dfs(path)
    return ans
    




if __name__ == '__main__':
    pass