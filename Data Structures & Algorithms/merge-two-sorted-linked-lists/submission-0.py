# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        p=dummy
        p1=list1
        p2=list2
        while p1 or p2:
            if p1 and p2:
                if p1.val==p2.val or p1.val<p2.val:
                    g=p1.val
                    p1=p1.next
                else:
                    g=p2.val
                    p2=p2.next
            elif p1:
                g=p1.val
                p1=p1.next
            else:
                g=p2.val
                p2=p2.next
            p.next=ListNode(g)
            p=p.next
        return dummy.next


        