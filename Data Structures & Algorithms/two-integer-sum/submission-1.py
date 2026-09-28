class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        
        for i in range(len(nums)):
            pair = target - nums[i]
            if pair in h:
                return [h[pair], i]
            else:
                h[nums[i]] = i

        return []