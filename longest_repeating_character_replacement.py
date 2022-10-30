class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        windowStart = 0
        windowEnd = 0
        char_map = {}
        max_length  = 0
        
        
        while windowEnd<len(s):
            c= s[windowEnd]
            if(c in char_map):
                char_map[c]+=1
            else:
                char_map[c]= 1
            
            
            #also rem = windowSize - max of map values 
            while((windowEnd - windowStart+1)- max(char_map.values())>k):
                val = char_map[s[windowStart]]-1
                if(val==0):
                    del char_map[s[windowStart]]
                else:
                    char_map[s[windowStart]]-=1
                windowStart+=1
            max_length = max(max_length,(windowEnd - windowStart+1))
            windowEnd+=1
        return max_length
    