# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

        
class Solution:

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # find if a liked list is cyclic or not 
        # uses two pointer solution 
        
        if not head:
            return False

        first_pointer = head
        second_pointer = head.next

        while second_pointer and second_pointer.next:

            #check if the second pointer catches the first and confirm its a cycle Linked list
            if first_pointer == second_pointer.next:
                return True
            
            #add the next values to check 
            first_pointer = first_pointer.next
            second_pointer = second_pointer.next.next
        
        #if the second doesn't catch up and it comes to none then its not a cycle Linked list   
        return False
