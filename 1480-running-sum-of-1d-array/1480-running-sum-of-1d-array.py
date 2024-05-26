class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        array_sum=[]
        for i in range(0,len(nums)):
            sum=0
            for j in range(0,i+1):
                sum=sum+nums[j]
            array_sum.append(sum)
        return array_sum
                
                
        