class Solution(object):
    def hammingWeight(self, n):
        bi=bin(n)
        return bi.count('1')
        """
        :type n: int
        :rtype: int
        """
        
