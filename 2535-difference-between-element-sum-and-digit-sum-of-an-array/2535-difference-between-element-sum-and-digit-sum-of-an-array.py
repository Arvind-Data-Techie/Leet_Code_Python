class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        a, num_sum = sum(nums), 0
        for x in nums:
            while x:
                num_sum += x % 10
                x //= 10
        return abs(a - num_sum)
                
            
        