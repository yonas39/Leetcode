# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        ######## solution 1 
        output=[]
        while head:
            output.append(head.val)
            head=head.next
        return output== output[::-1]

        ###### Solution 2 there is one bug that i couldn't find 
        # current = head
        # previous= None
        # # next_=None
        # while current:
        #     next_ = current.next
        #     current.next = previous
        #     previous = current
        #     current = next_      

        # while previous:
        #     if not head or previous.val != head.val:
        #         return False
        #     head = head.next
        #     previous = previous.next

        # return True

   

   
