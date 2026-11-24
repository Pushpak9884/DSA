class Solution:
    def reverse(self, x: int) -> int:
        if x<0:
            s=-1
        else:
            s=1
        rev=0    
        x=abs(x) 
        while x>0:
            digit=x%10
            rev=rev*10+digit
            x=x//10
        rev=rev*s
        if  rev<-2**31 or rev>2**31 - 1:
            return 0
        else:
             return rev            
        