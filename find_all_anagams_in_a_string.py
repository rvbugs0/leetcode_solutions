class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s1=p
        s2=s
        def check_maps(map1,map2):
            if(len(map1.keys())==len(map2.keys())):

                for k in map1.keys():
                    if(k not in map2 or map1[k]!=map2[k]):
                        return False
                return True
            return False



        s1_map = {}
        for c in s1:
            if c not in s1_map:
                s1_map[c]=1
            else:
                s1_map[c]+=1

        startIndices = []
        windowEnd= 0
        windowStart = 0
        s2_map={}
        str_len = 0

        while windowEnd<len(s2):
            c = s2[windowEnd]
            if(c not in s1_map):
                windowEnd+=1
                windowStart = windowEnd
                s2_map={}
                continue
            else:
                if c in s2_map:
                    s2_map[c]+=1
                else:
                    s2_map[c]=1
                windowEnd+=1
                
                str_len=windowEnd-windowStart
                
                if(check_maps(s1_map,s2_map)):
                    startIndices.append(windowStart)
                    val = s2_map[s2[windowStart]]-1
                    if(val ==0):
                        del s2_map[s2[windowStart]]
                    else:
                        s2_map[s2[windowStart]]= val
                    windowStart+=1
                elif(str_len>len(s1)):
                    val = s2_map[s2[windowStart]]-1
                    if(val==0):
                        del s2_map[s2[windowStart]]
                    else:
                        s2_map[s2[windowStart]]= val
                    windowStart+=1
                    if(check_maps(s1_map,s2_map)):
                        startIndices.append(windowStart)
                        val = s2_map[s2[windowStart]]-1
                        if(val ==0):
                            del s2_map[s2[windowStart]]
                        else:
                            s2_map[s2[windowStart]]= val
                        windowStart+=1
        return startIndices
