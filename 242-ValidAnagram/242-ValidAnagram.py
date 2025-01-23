class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freqs = [0]*26
        freqt = [0]*26
        for c in s:
            freqs[ord(c)-ord('a')] +=1
        for c in t:
            freqt[ord(c)-ord('a')] +=1

        return freqs == freqt