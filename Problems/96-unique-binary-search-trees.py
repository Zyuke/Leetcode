# https://leetcode.com/problems/unique-binary-search-trees

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = [0] * (n + 1)
        res[0] = 1
        
        for i in range(1, n + 1):
            for j in range(i):
                res[i] += res[j] * res[i-1-j]
                
        return res[-1]