"""
https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
"""


class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder or not postorder:
            return None
        r = postorder.pop()
        root = TreeNode(r)
        indx = inorder.index(r)
     
        root.right = self.buildTree(inorder[indx+1:], postorder)
        root.left = self.buildTree(inorder[:indx], postorder)

        return root