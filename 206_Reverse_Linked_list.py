# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """Reverse the given linked list
            Assume we have a linked lint as [1,2,3,4,5,None] and 
            let current = 2 and previous = 1 and Next = 3. 
            1. loop in the linked list until it reaches None
            example.
            2. set next_ to be (current.next = 3) 2
            3. set current.next  (previous = 1) none
            4. set previous to be (current = 2) 1
            5. set current to be (next_ = 3)    2
            6. make previous to be the head

            now we have 1-->2 converted to 2-->1 and it continues until current reaches None
        """
        ############### Iterative Method #################
        current = head
        previous = None
        next_ = None

        while current:
            next_ = current.next
            current.next = previous
            previous = current 
            current = next_
            
        return previous 

        ############### Recursive Method ################
        # if not head or not head.next:
        #     return head
        # reversed_ = self.reverseList(head.next)
        # head.next.next = head
        # head.next = None
        # return reversed_






