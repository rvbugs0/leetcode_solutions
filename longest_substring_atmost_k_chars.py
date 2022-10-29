class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        char_map = {}
        windowEnd = 0
        windowStart = 0
        max_length = 0
        while windowEnd<len(s):
            if len(char_map.keys())<=k:
                # if unique chars < k, expand window
                c = s[windowEnd] 
                if c in char_map:
                    char_map[c] = char_map[c]+1
                else:
                    char_map[c] = 1
                windowEnd+=1
            else:
                #shring window from left
                c = s[windowStart]
                val = char_map[c]
                if (val-1 == 0):
                    del char_map[c]
                else:
                    char_map[c] = char_map[c]-1
                windowStart+=1
            str_length = windowEnd- windowStart
            if(len(char_map.keys())<=k):
                max_length = max(max_length, str_length)
        return max_length
                
            
            
            
            
            
        
        
        
        
        