# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = self.defineHead(list1, list2)
        headptr = head
        if head == None:
            return 
        if head == list1:
            list1 = list1.next
        else:
            list2 = list2.next

        while list1 or list2:
            if list1 and list2: 
                if list1.val < list2.val:
                    head.next = list1
                    list1 = list1.next
                else:
                    head.next = list2
                    list2 = list2.next
                head = head.next
            else:
                if list1:
                    head.next = list1
                    break
                else:
                    head.next = list2
                    break
        return headptr


    def defineHead(self, list1, list2):
        if list1 and list2:
            if list1.val < list2.val:
                return list1
            else:
                return list2
        else:
            if list1:
                return list1
            else:
                return list2