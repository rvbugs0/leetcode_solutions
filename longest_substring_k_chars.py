class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        
        def map_each_has_k(m,k):
            satisfied = True
            for key in m.keys():
                if(m[key]<k):
                    satisfied = False
                    break
            return satisfied
        
        maxUnique = len(set(s))
        max_len = 0
        
        for currUnique in range(1,maxUnique+1):
            windowStart = 0
            char_map={}
            windowEnd = 0            
            
            while windowEnd < len(s):
                
                if(len(char_map)<=currUnique):
                    #expand the window:
                    
                    if s[windowEnd] in char_map:
                        char_map[s[windowEnd]] = char_map[s[windowEnd]]+1
                    else:
                        char_map[s[windowEnd]] = 1
                    windowEnd+=1
                
                else:
                    #shrink window
                    val = char_map[s[windowStart]]
                    if(val-1==0):
                        del char_map[s[windowStart]]
                    else:
                        char_map[s[windowStart]] = char_map[s[windowStart]]-1
                    windowStart+=1

                
                
                length_str = windowEnd-windowStart
                    
                if(max(char_map.values())>=k):
                    if(map_each_has_k(char_map,k)):
                        max_len = max(max_len, length_str)

                                
                        

                
                
                
            
        return max_len
        