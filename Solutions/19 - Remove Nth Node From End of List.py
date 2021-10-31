from typing import List, Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    #Recursive Helper Function, returns a tuple
    def removeNthFromEndRecur(self, head: Optional[ListNode], n: int):
        #Case of the last element
        if not head.next:
            end_dist = 1
            tail = None
        #If not the last element, grab the distance to the end and the tail
        else:
            end_dist, tail = self.removeNthFromEndRecur(head.next, n)
        #If the current element is the one to be removed, return the tail
        if end_dist == n:
            return end_dist + 1, tail
        #If not, then return the head attached to the tail
        else:
            return end_dist + 1, ListNode(head.val, tail)

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #Call our helper function
        _, ans = self.removeNthFromEndRecur(head, n)
        return ans

#Walked through in debug mode
if __name__ == '__main__':
    test_node = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    sol_node = ListNode(1, ListNode(2, ListNode(3, ListNode(5))))
    test = Solution()
    comparison = test.removeNthFromEnd(test_node, 2) == sol_node
    comparison