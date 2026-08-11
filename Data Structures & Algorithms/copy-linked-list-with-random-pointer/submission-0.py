class Solution:
    def copyRandomList(self, head: "Node") -> "Node":
        if not head:
            return None

        # Step 1: Duplicate nodes and insert them in between the original nodes
        current = head
        while current:
            duplicate = Node(current.val)
            duplicate.next = current.next
            current.next = duplicate
            current = duplicate.next

        # Step 2: Update random pointers for the duplicate nodes
        current = head
        while current:
            if current.random:
                current.next.random = current.random.next
            current = current.next.next

        # Step 3: Split the combined list into two separate lists
        original = head
        duplicate_head = head.next
        current = duplicate_head
        while original:
            original.next = original.next.next
            if current.next:
                current.next = current.next.next
            
            original = original.next
            current = current.next

        return duplicate_head