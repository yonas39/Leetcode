# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # id there is no root head return empty root
        if not root:
            return root
        
        # store the root nodes in a queue
        agenda = [root]
        result = []

        while agenda: #loop until the queue is empty 
            level_=len(agenda)
            temp= []

            for i in range(level_): 
                node = agenda.pop(0) # first in first out (BFS)
                temp.append(node.val)
                if node.left:
                    agenda.append(node.left)
                if node.right:
                    agenda.append(node.right)
            result.append(temp)
        return result
