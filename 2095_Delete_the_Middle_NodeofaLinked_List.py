# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]: 
        # def listLength(head):
        #     # used to find the length of the linked list 
        #     count=0
        #     while head:
        #         count+=1
        #         head=head.next
        #     return count

        # middle= listLength(head)//2

        # current=head
        # previous= None
        # i=0
        # while current:
        #     if i == middle:
        #         if previous:
        #             previous.next= current.next
        #         else:
        #             head=current.next
        #     else:
        #         previous = current
        #     current = current.next
        #     i+=1
        # return head

        ##################  Two pointer solution   ##########################
        
        slow = head
        fast = slow
        previous = None
        
        while fast and fast.next:
            previous = slow
            slow=slow.next
            fast=fast.next.next
            
           
        if previous == None:
            return None
        previous.next = slow.next
        return head
