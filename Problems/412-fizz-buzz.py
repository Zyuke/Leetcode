# https://leetcode.com/problems/fizz-buzz

class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        result = []
        for i in range(1,n+1):
            if i%3 == 0 and i%5 != 0:
                result.append("Fizz")
            elif i%3 != 0 and i%5 == 0:
                result.append("Buzz")
            elif i%3 == 0 and i%5 == 0:
                result.append("FizzBuzz")      
            else:
                result.append(str(i))
        return result
            