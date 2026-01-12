# Last updated: 1/12/2026, 1:41:48 PM
class Solution(object):
    def reverseString(self, s):
        i = 0
        j = len(s)-1
        while i < j:
            temp1 = s[i]
            s[i] = s[j]
            s[j] = temp1
            i+=1
            j-=1
            
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        