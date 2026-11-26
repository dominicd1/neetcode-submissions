class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        temp = None  # Tracks the previous node

        while node is not None:
            nxt = node.next  # 1. Save the next node before breaking the link
            node.next = temp # 2. Reverse the pointer
            temp = node      # 3. Move temp forward to current node
            node = nxt       # 4. Move node forward to the saved next node

        return temp