# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ########### recursive method ################
        # result=[]
        # if root:
        #     result.append(root.val)
        #     left=self.preorderTraversal(root.left)
        #     if left:
        #         result+=left
        #     right=self.preorderTraversal(root.right)
        #     if right:
        #         result+=right
        # return result

        ############# Iterative method #############

        if not root:
            return []

        agenda=[root]
        result=[]
        while agenda:
            node = agenda.pop()
            result.append(node.val)
            
            if node.right:
                agenda.append(node.right)
            if node.left:
                agenda.append(node.left)
        
     
        return result 
