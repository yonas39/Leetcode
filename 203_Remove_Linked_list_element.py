# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
      """This function removes a linked list item if its equal to the given value and return a linked list with out the value item""""

        if not head:
            return head
        # define current and prevoious variable for easier understading 
        current = head
        previous = None


        while current: # loop until the current LinkedList is empty

            # if the current value is equal to the given value then go on to check the previous value 
            if current.val == val:

                # if previous is different from none (means value was assigned to it) set the next value to be the one next to the current value 
                if previous is not None:
                    previous.next = current.next
                # otherwise set the head to start fromt the second element because previous was empy(means the value is the first item in the Linkedlist)
                else:
                    head = current.next      
            # if the current value is not equal to val set the current value to be a previous value  
            else:
                previous = current
            
            # set current to current.next until the linked value reaches None so the loop terminate 
            current = current.next
        # when the loop terminate return the head after all the values have been removed
        return head
      
      
      
      ############ Recursive Solution ##############
      
#         if not head:
#             return head
        
#         head.next = self.removeElements(head.next, val)
#         return head.next if head.val == val else head
