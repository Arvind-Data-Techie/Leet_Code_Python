class Solution:
    def isHappy(self, n: int) -> bool:
        
        seen_numbers=set()
        print(seen_numbers)
        while n not in seen_numbers:
            print(n)
            seen_numbers.add(n)
            string=str(n)
            squares_sum=0
            for i in string:
                squares_sum+=pow(int(i),2)
            if squares_sum==1:
                return True
            n=squares_sum
        return False
        