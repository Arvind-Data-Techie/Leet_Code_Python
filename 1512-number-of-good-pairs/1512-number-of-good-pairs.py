class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count=0
        index=1
        for i in nums:
            for j in range(index,len(nums)):
                if i==nums[j]:
                    print(i,nums[j])
                    count+=1
            index+=1
        return count
                
        