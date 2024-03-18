class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        set_1 = set(nums)
        set_2 = set(range(1, len(nums) + 1))
        return list(set_2 - set_1)
        