# Last updated: 1/12/2026, 1:41:32 PM
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        res = 0
        char_count = [0]*26
        
        for char in chars:
            char_count[ord(char)-ord('a')] += 1
        
        for word in words:    
            word_count = [0]*26
            can_form = True
            
            for char in word:
                idx = ord(char)-ord('a')
                word_count[idx] +=1
                
                if word_count[idx] > char_count[idx]:
                    can_form = False
                    break
                    
            if can_form:
                res += len(word)
                
        return res    
                    
                
                    
        