# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def setNext(self, next):
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        count = 0
        output = []

        
        if node == None:
            return None

        if node.next == None:
            return node

        prev = None

        while(node is not None):
            print(node.val)
            next = node.next
            node.setNext(prev)
            prev = node
            node = next
    
        
        return prev
            
            #0 --> 1 --> 2 -->3 --> None
            # 0<-- 1<-- 2<-- 3


            
        
        
        
        