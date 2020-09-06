class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head==None:
            return False
        if head.next==None:
            return False
        if head.next==head:
            return True
        d={}
        current=head
        while current!=None:
            if current.next not in d:
                d[current.next]=1
            else:
                return True
            current=current.next
        return False
