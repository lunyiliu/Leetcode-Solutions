# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, Node):
        if Node==None:
            return
        if Node.left!=None:
            self.flatten_(Node.left,0,None)
            if Node.right!=None:
                self.flatten_(Node.left,1,Node.right)
            Node.right=Node.left
            Node.left=None
            self.flatten_(Node.right,2,None)
        else:
            if Node.right==None:
                return
            Node.left=Node.right
            Node.right=None
            self.flatten_(Node.left,0,None)
            Node.right=Node.left
            Node.left=None
            self.flatten_(Node.right,2,None)
    def flatten_(self,Node,signal,Node_right):
        if signal==0:
            if Node.left!=None:
                self.flatten_(Node.left,0,None)
                if (Node.right==None):
                    return 1
                else:
                    self.flatten_(Node.left,1,Node.right)
                    Node.right=None
                    return 1
            else:
                if Node.right!=None:
                    Node.left=Node.right
                    Node.right=None
                    self.flatten_(Node.left,0,None)
                else:
                    return 1 
        if signal==1:
            if Node.left!=None:
                self.flatten_(Node.left,1,Node_right)
            else:
                Node.left=Node_right
                self.flatten_(Node.left,0,None)
        if signal ==2:
            if Node==None:
                return
            Node.right=Node.left
            Node.left=None
            self.flatten_(Node.right,2,None)
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
