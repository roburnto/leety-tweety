# Last updated: 1/12/2026, 1:41:22 PM
class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        res = []
        i = 0
        n = min(len(word1), len(word2))
        while i < n:
            res.extend([word1[i], word2[i]])
            i += 1
        # no need for if/elif—empty slices are harmless
        res.append(word1[i:])
        res.append(word2[i:])
        return ''.join(res)