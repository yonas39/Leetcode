# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ############ recursive Method ############
        # result= []
        # if root:
        #     # first add the left legs to the result list 
        #     left=self.postorderTraversal(root.left)
        #     if left:
        #         result+=left
            
        #     # after left add the right legs
        #     right= self.postorderTraversal(root.right)
        #     if right:
        #         result+=right
            
        #     # then add the root head value last
        #     result.append(root.val)
        # return result

        ############# Iterative Method #########
        # if not root:
        #     return []
        
        # agenda=[root]
        # result=[]
        # while agenda:
        #     node=agenda.pop()
        #     result.append(node.val)
        #     if node.left:
        #         agenda.append(node.left)
        #     if node.right:
        #         agenda.append(node.right)
        # # result.append(root.val) 
        # return result[::-1]

        ############# Iterative method sol-2#############
        if not root:
            return root

        agenda=[root]
        result=[]
        while agenda:
            node=agenda.pop()

            if not node.left and not node.right:
                result.append(node.val)
            else:
                left = node.left
                right= node.right
                node.left = None
                node.right = None

                agenda.append(node)
                if right:
                    agenda.append(right)
                if left:
                    agenda.append(left)
        return result
