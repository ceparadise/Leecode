__author__ = 'vivian'
# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def maxDepth(self, root):
        if root == None:
            return 0
        else:
            return max(self.maxDepth(root.left), self.maxDepth(root.right))+1

if __name__ == '__main__':
    root = TreeNode(1)
    left = TreeNode(2)
    right = TreeNode(3)
    root.left = left
    root.right = right
    e = Solution()
    print e.maxDepth(root)
