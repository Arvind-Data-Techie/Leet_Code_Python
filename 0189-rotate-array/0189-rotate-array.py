class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        
        """
        Do not return anything, modify nums in-place instead.
        """
        
        k = k % len(nums)
        first_half = nums[:-k]
        second_half = nums[-k:]
        nums[:]=second_half+first_half
        
        
        
        