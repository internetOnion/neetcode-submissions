class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seqs = {}
        ls = len(s)
        lt = len(t)

        if ls != lt:
            return False
        
        for i in range(ls):
            if s[i] in seqs:
                seqs[s[i]] += 1
            else:
                seqs[s[i]] = 1
        
        for i in range(ls):
            if t[i] not in seqs:
                return False
            
            seqs[t[i]] -= 1
            if seqs[t[i]] == 0:
                del seqs[t[i]]
        
        return True
            
            

