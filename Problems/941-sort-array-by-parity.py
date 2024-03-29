# https://leetcode.com/problems/sort-array-by-parity

class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        even = []
        odd = []
        for x in A:
            if x % 2 == 0:
                even.append(x)
            else: odd.append(x)
        return even + odd