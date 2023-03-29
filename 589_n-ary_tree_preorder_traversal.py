"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node', temp=[]) -> List[int]:

        ########## Iterative solution ###################

        # if not root:
        #     return root
        # agenda=[root]
        # result=[]
        # while agenda:
        #     node = agenda.pop()
        #     result.append(node.val)
        #     if node.children:
        #         agenda.extend(node.children[::-1])
        # return result

        ########## Recursive solution ###################
        if not root:
            return []
        result = [root.val]
        for child in root.children:
            result.extend(self.preorder(child))
        return result
