__author__ = 'vivian'
# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    # @param {TreeNode} p
    # @param {TreeNode} q
    # @return {boolean}
    def isSameTree(self, p, q):
        if p == None and q == None:
            return True
        if p and q and p.val == q.val:
            #p and q and p.val == q.val之所以判断p and q 目的是保证他们不是none。如果其中一个是none，会报错
            return self.isSameTree(p.left,q.left) and self.isSameTree(p.right, q.right)
        return False
if __name__== '__main__':
    val1 = TreeNode(1)
    left1 = TreeNode(2)
    right1 = TreeNode(3)
    val1.right = right1
    val1.left = left1
    val2 = TreeNode(1)
    left2 = TreeNode(2)
    right2 = TreeNode(4)
    val2.right = right2
    val2.left = left2
    e = Solution()
    print e.isSameTree(val1,val2)