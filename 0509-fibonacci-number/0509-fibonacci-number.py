class Solution:
  def fib(self, n: int) -> int:    
    
    f=[0,1,1]
    
    if n == 0 or n==1:
        return n
    else:
        for i in range(2,n):
            f[0]=f[1]
            f[1]=f[2]
            f[2]=f[0]+f[1]
        return f[2]


            
    
        