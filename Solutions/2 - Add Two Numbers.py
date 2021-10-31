class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        self.solution = ListNode()
        iterator = self.solution
        while l1 or l2:
            sum = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            carry = 0
            if sum > 9:
                sum %= 10
                carry = 1
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            iterator.next = ListNode(sum)
            iterator = iterator.next
        if carry == 1:
            iterator.next = ListNode(1)
        return self.solution.next