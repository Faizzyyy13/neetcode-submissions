# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.bal=True
        def hei(x):
            if not x:
                return 0
            left=hei(x.left)
            right=hei(x.right)
            bal=abs(right-left)
            if bal>1:
                self.bal=False
            return 1+max(left,right) 
        hei(root)
        return self.bal