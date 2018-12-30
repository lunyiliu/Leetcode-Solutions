class Solution:
    def findLUSlength(self, a, b):
        if len(a)>len(b):
            return len(a)
        else:
            if len(a)<len(b):
                return len(b)
            else:
                if a==b :
                    return -1
                else:
                    return len(a)
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        
