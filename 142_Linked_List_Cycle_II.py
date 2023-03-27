# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode],temp=set()) -> Optional[ListNode]:
        #define two pointers slow and fast 
        slow=head
        fast=head
        
        while fast and fast.next:
            # make slow move one step at a time and fast move two step at a time
            slow = slow.next
            fast = fast.next.next
            # if there is a cycle then slow and fast eventually lands at the same node when that hapens break the loop
            if slow == fast:
                break
        #if there is no cylce fast or fast.next reach the end of the linked list so its value will be None it indicates there is no cycle so return None
        if not fast or not fast.next:
            return None

        # if the first loop break when slow == fast then its going to jump here
        #set the slow to head again and move both slow and fast one step at a time until they reach the same node. when that happens return slow head
        slow=head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow
        
        ############## Recrusive_1 #####################
        # def rec_helper(head, temp=set()):
        #     if not head:
        #         return None
        #     if head in temp:
        #         return head   
        #     temp.add(head)
        #     return rec_helper(head.next, temp)
        # return rec_helper(head)

        ############## Recrusive_2 #####################
        # if not head:
        #     return None
        # if head in temp:
        #     return head
        # temp.add(head)
        # return self.detectCycle(head.next , temp)
    
