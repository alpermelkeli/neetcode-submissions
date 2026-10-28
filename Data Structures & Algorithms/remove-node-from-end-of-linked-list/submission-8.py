# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        i = 1
        size = self.sizeOfList(head)
        
        if size < 2:
            return None
        if size - n == 0:
            return head.next

        pointer = head

        while i != size - n:
            pointer = pointer.next
            i += 1
        
        pointer.next = pointer.next.next

        return head

    def sizeOfList(self, head):
        counter = 0
        while head != None:
            counter += 1
            head = head.next
        return counter







    