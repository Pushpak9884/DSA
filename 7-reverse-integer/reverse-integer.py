class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x<0:
            s=-1
        else:
            s=1
        x=abs(x)
        r=0
        while x!=0:
            a=x%10
            r=(r*10)+a
            x=x//10
        r*=s
        if r<-2**31 or r>2**31 - 1:
            return 0
        return r    

        