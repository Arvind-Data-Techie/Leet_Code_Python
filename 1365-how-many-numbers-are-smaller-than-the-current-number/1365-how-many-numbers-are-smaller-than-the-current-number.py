class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        smaller_list=[]
        for i in nums:
            count=0
            for j in nums:
                if j<i:
                    count+=1
            smaller_list.append(count)
        return smaller_list
        