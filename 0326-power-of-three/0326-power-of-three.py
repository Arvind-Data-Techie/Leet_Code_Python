import math
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        
        if n<=0:
            return False
        
        p = round(math.log(n)/math.log(3),10)
        
        if p-int(p)==0:
            return True
        else:
            return False
        
        