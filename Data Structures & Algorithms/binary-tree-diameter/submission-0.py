# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res=0
        def theight(x):
            if not x:
                return 0
            left=theight(x.left)
            right=theight(x.right)
            self.res=max(self.res,left+right)
            return 1+max(left,right)
        theight(root)
        return self.res
        
        