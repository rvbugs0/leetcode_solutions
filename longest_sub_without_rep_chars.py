class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        windowStart = 0
        windowEnd = 0
        char_map = {}
        max_len  = 0
        
        while windowEnd<len(s):
            #we have to expand window until we see the distinct chars
            c = s[windowEnd]
            if c not in char_map:
                char_map[c] = 1
                windowEnd+=1
                
            else:
                while(c in char_map):
                    del char_map[s[windowStart]]
                    windowStart+=1
            max_len = max(max_len,windowEnd-windowStart)
        return max_len
            # we have to measure length each time
            
            #we have to shrink window until no more chars in window are repeating
            
            
            
        
        
        
        
        
        