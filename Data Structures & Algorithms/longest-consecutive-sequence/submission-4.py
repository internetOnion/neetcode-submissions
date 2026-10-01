class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        nums.sort()
        max = 1
        curr = 1

        for i in range(1, len(nums)):
            print(i)
            if nums[i] == nums[i - 1] + 1:
                curr += 1

                if curr > max:
                    max = curr
            elif nums[i] > nums[i - 1] + 1:
                curr = 1
            
        return max