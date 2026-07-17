# Time Complexity: O(n)
# Space Complexity: O(h)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isValidBST(self, root):
        def dfs(node, low, high):
            if not node:
                return True
            if node.val <= low or node.val >= high:
                return False
            return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)

        return dfs(root, float("-inf"), float("inf"))