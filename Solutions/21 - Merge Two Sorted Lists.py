from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #Base Case: If there is no l1, return l2
        if not l1:
            return l2
        #Base Case:If there is no l2, return l1
        elif not l2:
            return l1
        #Compare the values, set the lowest as the head, and the tail as the recursive result
        if l2.val <= l1.val:
            return ListNode(l2.val, self.mergeTwoLists(l1, l2.next))
        else:
            return ListNode(l1.val, self.mergeTwoLists(l1.next, l2))
    
if __name__ == '__main__':
    test = Solution()