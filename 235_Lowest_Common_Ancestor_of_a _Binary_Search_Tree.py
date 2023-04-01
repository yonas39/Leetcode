# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Given a binary search tree (BST), the task is to find the lowest common ancestor (LCA) of two   given nodes in the BST.

The LCA of two nodes in a binary tree is the lowest node in the tree that has both the given nodes as descendants. In a BST, the LCA is the node that has a value between the values of the two given nodes.

To solve this problem, we can traverse the BST starting from the root node. If the value of the current node is greater than both the nodes, we move to the left subtree. If the value of the current node is smaller than both the nodes, we move to the right subtree. If the value of the current node is between the two nodes, then we have found the LCA.

        """
        if not root:
            return root
        
        agenda=[root]
        while agenda or root:
            node = agenda.pop()
            if node.val > p.val and node.val > q.val:
                agenda.append(node.left)
            elif node.val < p.val and node.val <q.val:
                agenda.append(node.right)
            else:
                return node
            
