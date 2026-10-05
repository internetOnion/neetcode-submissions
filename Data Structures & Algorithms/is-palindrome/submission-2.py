class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_alpha = "".join([c for c in s if c.isalnum()])
        l, r = 0, len(s_alpha) - 1

        while l < r:
            if s_alpha[l].lower() != s_alpha[r].lower():
                return False

            l += 1
            r -= 1

        return True
