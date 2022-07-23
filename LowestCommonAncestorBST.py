# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        '''If both the nodes are > than the current node, go to the right. If both < curr node then go to the left else return the current node
        Time Complexity: O(h) --> log n if we have a perfect bst
        Space Complexity: O(1)
        '''
        if p.val < root.val and q.val<root.val:
            #Go left
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val>root.val:
            #Go right
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root
