class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        length = self.lengthOfLinkedList(head)
        secondListHead = self.splitFrom(head, length // 2)
        secondListHead = self.reverseList(secondListHead)
        self.merge(head, secondListHead)

    def merge(self, first, second):
        while first and second:
            tmp1 = first.next
            tmp2 = second.next

            first.next = second
            if tmp1 is None:
                break
            second.next = tmp1

            first = tmp1
            second = tmp2

    def reverseList(self, head):
        prev = None
        while head:
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt
        return prev

    # It returns new list head which is splitted from index
    def splitFrom(self, head, index):
        node = head
        for _ in range(index - 1):
            node = node.next
        temp = node.next
        node.next = None
        return temp

    def lengthOfLinkedList(self, head):
        length = 0
        while head:
            length += 1
            head = head.next
        return length