class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product=1
        summation=0
        for s in str(n):
            product=product*int(s)
            summation=summation+int(s)
        return product-summation
        
        