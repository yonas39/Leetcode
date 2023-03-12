
"""
  You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, 
  and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

  You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
   
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """Traverse on both of the linked lists and add their values while keeping track of their 
          carryover value. while calculating the sum of their digit construct the new_summation 
          linkedlinke list
        """

        carryOver = 0            #keep track of carry over 
        Node = ListNode(0)       #new linked_list Node
        next_= Node              #initialize the next_node to the node created earlier 

        while l1 or l2:          # traverse through the linked lists while the longest exhausted 

            #initialize variable val_1 and val_2 to get store the value of the current node 
            val_1 = l1.val if l1 else 0   
            val_2 = l2.val if l2 else 0

            
            digit_sum = val_1 + val_2 + carryOver # add the two digits and the carry over from previous
            carryOver = digit_sum //10            # find the carry over using floor division 
            
            # finds the sum after the carry over using mod % by 10 and construct the sum_node on the go
            next_.next = ListNode(digit_sum % 10) 
            next_ = next_.next

            # move to the next node if either one of them have next vale that is not None
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        #if there is a carry over remaining add it to the end of the linked list before returnin the sum
        if carryOver:
            next_.next=ListNode(carryOver)
        
        return Node.next
