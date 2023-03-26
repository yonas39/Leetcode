# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # #two pointers
        # #reverse the second half
        # #intertwine the first and reversed sedcond half 

        # # when the head is empty or head only has one value return the head
        # if not head or not head.next:
        #     return head

        # # using two pointers find the mid point of the linked list 
        # slow = head
        # fast = head
        # while fast and fast.next:
        #   slow=slow.next
        #   fast=fast.next.next
            
        # middle=slow

        # previous = None
        # current = middle
        # while current:
        #   # current.next = previous
        #   # previous = current
        #   # current = current.next
        #   next_node = current.next
        #   current.next = previous
        #   previous = current
        #   current = next_node
        
        # reverse_head = previous
        # first, second = head, reverse_head

        # while second.next:
        #   next_node = first.next
        #   first.next = second
        #   first = next_node

        #   next_node = second.next
        #   second.next = first
        #   second = next_node
        
        #@##################### Another method ########################

        storage = []
        length=0
        current=head
        while current:
            storage.append(current)
            length+=1
            current = current.next
          
        first, second = 0, length-1
        last=head
        while first < second:
            storage[first].next = storage[second]
            first+=1

            if first == second:
                last =storage[second]
            #   storage[first].next = storage[second]
                break

            storage[second].next = storage[first]
            second-=1

            last = storage[first]

        if last:
            last.next=None
