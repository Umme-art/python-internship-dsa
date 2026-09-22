class Solution:
    def isPalindrome(self, head):
        if not head or not head.next:
            return True

        slow = fast = head

        # find middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse second half
        prev = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt

        # compare
        left, right = head, prev

        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True
        