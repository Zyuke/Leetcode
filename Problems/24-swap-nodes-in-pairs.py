# https://leetcode.com/problems/swap-nodes-in-pairs

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        
        cur = dummy
        
        
        while cur.next and cur.next.next:
            first, second = cur.next, cur.next.next
            cur.next = second
            first.next = second.next
            second.next = first
            cur = cur.next.next
        
        return dummy.next
            