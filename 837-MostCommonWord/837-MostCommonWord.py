# Last updated: 1/12/2026, 1:41:38 PM
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        
        words = re.split(r"[ !?',;.\"]+", paragraph)
        
        word_count = {}
        banned_set = set(banned)
        for word in words:
            if word and word.lower() not in banned_set:
                word_count[word.lower()] = 1 + word_count.get(word.lower(),0)
        
        return max(word_count, key = word_count.get)