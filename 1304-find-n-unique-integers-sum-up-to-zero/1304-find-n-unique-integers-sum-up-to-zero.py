class Solution:
    def sumZero(self, n: int) -> List[int]:
        i=n
        lst=[]
        if n%2==0:
            for i in range(1,n//2+1):
                lst.append(i)
                lst.append(-i)
        else:
            lst.append(0)
            for i in range(1,n//2+1):
                lst.append(i)
                lst.append(-i)
            
                
        print(lst)
        return lst
        