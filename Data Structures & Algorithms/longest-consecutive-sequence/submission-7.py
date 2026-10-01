class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        max = 0

        for n in s:
            curr = 1
            if n - 1 in s:
                continue
            else:
                while n + curr in s:
                    curr += 1
                
                if curr > max:
                    max = curr
        
        return max