# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Helper function to insert a new node into a sorted list
        def insert_into_sort(sortedList, newNode):
            if not sortedList or newNode.val < sortedList.val:
                newNode.next = sortedList
                sortedList = newNode
                return sortedList

            current = sortedList
            while current.next and newNode.val > current.next.val:
                current = current.next

            newNode.next = current.next
            current.next = newNode

            return sortedList

        def insertion_sort(head):
            if not head or not head.next:
                return head

            sortedList = None
            current = head
            while current:
                next_node = current.next
                sortedList = insert_into_sort(sortedList, current)
                current = next_node
            return sortedList

        return insertion_sort(head)

"""Alternative solution with better running time at the cost of memory"""
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Convert linked list values to an array
        temp_array = []
        current = head
        while current:
            temp_array.append(current.val)
            current = current.next
        
        # Sort the array
        temp_array.sort()
        
        # Update linked list values with sorted array values
        current = head
        i = 0
        while current:
            current.val = temp_array[i]
            current = current.next
            i += 1

        return head
