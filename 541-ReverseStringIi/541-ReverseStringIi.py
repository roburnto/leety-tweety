# Last updated: 1/12/2026, 1:41:45 PM
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        res = []
        n = len(s)
        i = 0
        true = True
        while i < n:
            #reverse first k characters
            res.append(s[i:i+k][::-1])
            res.append(s[i+k:i+2*k])
            
            i += 2*k
        
        return "".join(res)