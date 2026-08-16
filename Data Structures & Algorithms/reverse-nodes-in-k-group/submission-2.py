# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head

        group_prev = dummy

        while True:
            # Find the kth node in the current group
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    # Fewer than k nodes remain
                    return dummy.next

            group_next = kth.next

            # Reverse the current group
            prev = group_next
            current = group_prev.next

            while current != group_next:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node

            # Connect the previous part to the reversed group
            old_group_start = group_prev.next
            group_prev.next = kth

            # The old start is now the end of the reversed group
            group_prev = old_group_start

        