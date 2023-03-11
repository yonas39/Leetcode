# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        ########### First Attemp ##############

        # # This solution works, but it exceeds the time limit beacause it is O(m*n)
        # currA , currB = headA , headB

        # temp = []
        # while currA:
        #     temp.append(currA)
        #     currA=currA.next
        # while currB:
        #     if currB in temp:
        #         return currB
        #     currB = currB.next
        # return None


        ########## Second attempt #############

        ## this code may seem long but efficient in terms of time complexity 
        #first find the length of both linked lists and calculate the difference, then loop over
        #the difference range and compare their values directly until we find the first common 
        #intersection point 

        len_A, len_B = 0 , 0
        currentA , currentB = headA, headB
        while currentA: #to find the len of A
            len_A+=1 
            currentA = currentA.next
        
        while currentB: # to find the len of B
            len_B +=1
            currentB = currentB.next
        
        if len_A > len_B: # shorten the linked list a to equal the length of linked list b
            for i in range(abs(len_A-len_B)):
                headA = headA.next
        else:
            for i in range(abs(len_A-len_B)): # shorten the linked list b to equal length linked list a
                if headB:
                    headB = headB.next
        
        #compere their value one on one unitil we find a match or the list is exhausted and return the 
        #value accordingly 
        while headA and headB:
            if headA == headB:
                return headA
            headA =headA.next
            headB = headB.next
        return None


























        
        
