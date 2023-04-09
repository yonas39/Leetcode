# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 
        self.diameter=0
        def depth(node):
            if not node:
                return 0
            #These lines calculate the maximum depths of the left and right children of the current node, by making recursive calls to the max_depth function
            left_depth = depth(node.left)
            right_depth = depth(node.right)
            #This line updates the diameter variable with the maximum of its current value and the sum of the depths of the left and right children of the current node
            self.diameter = max(self.diameter,left_depth+right_depth)
            #maximum of the depths of the left and right children, plus 1 (to account for the current node).
            return max(left_depth, right_depth)+1 
        
        depth(root) # initializes the calculation of the maximum depth and diameter of the tree.
        return self.diameter #represents the diameter of the binary tree.


      
      
      
      
      
      
      
      
      
