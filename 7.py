import math
class Solution:
    def reverse(self, x):
        if x<0:
            x=-x
            minus=True
        else:
            minus=False
        num=[]
        number=0
        while x!=0:
            num.append(x%10)
            x=int(x/10)
        '''
        if len(num)==10 and num[0]>2 and num[1]>1 and num[2]>4 and num[3]>7 and num[4]>4 and num[5]>8 and num[6]>3 and num[7]>6 and num[8]>4 and num[9]>7:
            return 0
            '''
        for i in range(len(num)):
            number=number+num[i]*math.pow(10,(len(num)-1-i))
        if number>2147483647 or number< -2147483648:
            return 0
        if minus==True:
            return -int(number)
        else:
            return int(number)
        """
        :type x: int
        :rtype: int
        """
