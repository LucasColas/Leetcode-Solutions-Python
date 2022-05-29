"""

Given a string array words, return the maximum value of length(word[i]) * length(word[j]) 
where the two words do not share common letters. If no such two words exist, return 0.
From leetcode : https://leetcode.com/problems/maximum-product-of-word-lengths/

"""

class Solution:
    def compare(self, str1, str2):
        for c in str1:
            if c in str2:
                return False
        return True
        
    
    def maxProduct(self, words: List[str]) -> int:
        max_len = 0
        for idx, word in enumerate(words):
            for idx2, word2 in enumerate(words):
                if idx != idx2 and self.compare(word, word2):
                    #print(word, word2)
                    new_len = len(word)*len(word2)
                    #print(new_len)
                    if new_len > max_len:
                        max_len = new_len
        return max_len
        
        
