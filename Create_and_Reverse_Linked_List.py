# 206- Reverse Linked List

class List_node:
  def __init__(self,data=0, next=None) -> None:
    self.data = data
    self.next = next

class Solution:
  def __init__(self,head=None) :
    self.head = head

  def addValue(self, data):

    value=List_node(data)

    if not self.head:
      self.head = value

    else:
      current = self.head
      while current.next is not None:

          current = current.next
        
      current.next = value
  
  def printElements(self):
    if self.head == None:
      print ("The list is empty")

    current=self.head
    while current is not None:
      print(current.data, end="-->")
      current = current.next

  def reverseLinkedlist(self, head):
    """I will write two solution for the given problem 
      1. iterative solution 
        It will loop over until head is none and contruct the reversed linked list along the way
      2. recursive solution 
        This method set a base case and when head or head.next is none then recursively reverse the 
        remaining values in the inductive step 
    """
    ## Soltuion-1
    current = self.head
    previous = None
    next_ = None

    while current:
      next_ = current.next
      current.next = previous
      previous = current 
      current = next_

    self.head = previous
    # return previous 
    return previous

    ## Solution-2

    # if not head or not head.next:
    #   return head
    
    # head = self.reverseLinkedlist(head.next)

    # head = head.next
    # previous = head

    # return previous


if __name__=='__main__':
  normal_list=[1,2,3,4,5,6]
  linked_list=Solution()

  for i in normal_list:
    linked_list.addValue(i)

  linked_list.printElements() 

  #### print the link reverse
  
  linked_list.reverseLinkedlist(linked_list)

  print("\n print below")
  linked_list.printElements()
  # reverse.printElements()
