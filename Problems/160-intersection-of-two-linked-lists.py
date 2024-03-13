# https://leetcode.com/problems/intersection-of-two-linked-lists

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        A_set = set()
        while headA:
            A_set.add(headA)
            headA = headA.next
            
        while headB:
            if headB in A_set:
                return headB
            headB = headB.next