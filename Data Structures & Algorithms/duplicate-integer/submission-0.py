class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seq = {}
        for i in range(len(nums)):
            if nums[i] in seq: 
                return True
            else: 
                seq[nums[i]] = 1;
        
        return False