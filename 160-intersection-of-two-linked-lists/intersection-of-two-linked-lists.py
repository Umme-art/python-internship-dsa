# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        temp1, temp2 = headA, headB
        len1 = len2 = 0
        while temp1:
            len1 += 1
            temp1 = temp1.next
        while temp2:
            len2 += 1
            temp2 = temp2.next

        temp1, temp2 = headA, headB
        if len1 > len2:
            while len1 != len2:
                temp1 = temp1.next
                len1 -= 1
        else:
            while len1 != len2:
                temp2 = temp2.next
                len2 -= 1
        while temp1:
            if temp1 == temp2:
                return temp1
            temp1 = temp1.next
            temp2 = temp2.next
        return None
        