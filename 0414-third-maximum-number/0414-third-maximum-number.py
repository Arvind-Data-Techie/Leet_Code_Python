class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        final_nums=list(dict.fromkeys(nums))
        if len(final_nums)<3:
            return final_nums[0]
        else:
            return final_nums[2]
        