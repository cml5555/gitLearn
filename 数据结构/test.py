root = [3,9,20,None,None,15,7]
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.ans=0
    def maxDepth(self, root):
         self.f(root,0)
         return self.ans
    def f(self,root,path):
        if root.left:
            self.f(root.left,path+1)
        elif root.right:
            self.f(root.right,path+1)
        else:
            self.ans=max(self.ans,path)

