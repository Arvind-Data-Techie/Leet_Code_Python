class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        ans=0
        for i in str(nums):
            if i=='[' or i==']' or i==',' or i==' ':
                continue
            else:
                ans+=int(i)
            print(i)
        return abs(sum(nums)-ans)
            
        