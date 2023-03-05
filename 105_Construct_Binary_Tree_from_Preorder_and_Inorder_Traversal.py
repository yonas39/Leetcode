# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:         
        # Base case: if one of the lists are empty return None
        if not preorder or not inorder:
            return None
        
        #remove the first value from the preorder and create a Tree Node
        value = preorder.pop(0)
        Node = TreeNode(value)

        # fin the index (position) of the value in the inorder list using .index()
        idx = inorder.index(value)

        #create a node for the left and right leg using recurssion
        Node.left = self.buildTree( preorder, inorder[:idx])
        Node.right= self.buildTree(preorder, inorder[idx+1:])

        #return the nodes of the newly created binary tree
        return Node
        
        
        
        
        
        
        
        
        
        
