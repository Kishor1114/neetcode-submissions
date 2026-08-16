# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head or k == 1:
            return head

        # Count the number of nodes in the list
        count = 0
        current = head
        while current:
            count += 1
            current = current.next

        if count < k:
            return head

        # Reverse the first k nodes
        prev, current = None, head
        for _ in range(k):
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        # Recursively reverse the remaining part of the list
        head.next = self.reverseKGroup(current, k)

        return prev
        