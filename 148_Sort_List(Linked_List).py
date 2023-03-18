# Merge sort LInked list(leet code 148_Sort List)

 Definition for singly-linked list.
 class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    """
        Given a linked list this function sort its values using merge sort algorithm and
        return the newly sorted linked list.
    """
        #if the list is empty or only have one value then return itself bcz its already sorted by default
        if not head or not head.next:
            return head
            
        #set two pointer one moves faster than the other and reach the end while slowest reach the middle
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        #divide the list in half head and right
        right = slow.next
        slow.next = None

        #recursively sort the two lists that was divided in half
        left=self.sortList(head)
        right=self.sortList(right)
        
        # construct a new linked list by comparing values from the left and right
        Node=ListNode(None)
        currentNode = Node
        while left and right:
            if left.val < right.val:
                currentNode.next = left
                left =left.next
            else:
                currentNode.next = right
                right = right.next
            currentNode=currentNode.next
        currentNode.next = left or right #if there is any remaining value it will append it to the end of the list
        return Node.next

      
      
      
      
      
      
      
      
      
      
      
      
