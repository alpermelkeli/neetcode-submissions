# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = self.fastRunner(head)
        slow = self.slowRunner(head)
        while fast != None or slow != None:
            fast = self.fastRunner(fast)
            slow = self.slowRunner(slow)
            if fast != None and slow != None and fast == slow:
                return True
        return False

    def fastRunner(self, head):
        if head != None and head.next != None:
            return head.next.next
        else:
            return None

    def slowRunner(self, head):
        if head != None:
            return head.next
        else:
            return None