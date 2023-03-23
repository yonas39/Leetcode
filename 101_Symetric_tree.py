# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        ############ RECURSIVE SOLUTION #################
        if not root:
            return True
        # left=root.left 
        # right=root.right
        

        def recHelper(left, right):
            if left is None and right is None:
                return True
            if left is None or right is None:
                return False
            if left.val!=right.val:
                return False
            return recHelper(left.left, right.right) and recHelper(left.right, right.left)

        return recHelper(root.left, root.right)

        ############# ITERATIVE SOLUTION ################
       
        # # if the root is empty then return true because we have nothing to compare 
        # if not root:
        #     return True
        
        # # a list of root nodes to be explored 
        # agenda=[[root.left, root.right]]


        # while agenda: #loop until the agenda is empy or false is returned 

        #     # Remove the first element from the agenda list and assign it to left and right variables
        #     node = agenda.pop(-1)
        #     left= node[0]
        #     right= node[1]
            
        #     # when both left and right are none continue to the next step 
        #     if left is None and right is None:
        #         continue

        #     # when either left or rigth node is  None or return False
        #     if left is None or right is None:
        #         return False
            
        #     # when the value of the left node is equal to the right node value great! check if their next value is also true by adding them to the agenda list.  otherwise return False
        #     if left.val == right.val:
        #         agenda.append([left.left, right.right])
        #         agenda.append([left.right, right.left])
        #     else:
        #         return False
                
        # return True #if all the above false conditions fail then the tree is symetric so return True

        
        
Console

Run
