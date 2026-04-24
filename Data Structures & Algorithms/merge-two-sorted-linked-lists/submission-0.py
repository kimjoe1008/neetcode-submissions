class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        newhead = dummy
        p1 = list1
        p2 = list2
        while p1 and p2:
            if p1.val > p2.val:
                newhead.next = p2
                p2 = p2.next
            else:
                newhead.next = p1
                p1 = p1.next
            newhead = newhead.next
        if p1:
            newhead.next = p1
        if p2:
            newhead.next = p2
        return dummy.next