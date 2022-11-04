class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        
        def addToMap(m,key,index):
            if key in m:
                m[key].append(index)
                # m[key].sort()
            else:
                m[key] = [index]

        def getMinOfMap(m):
            mi=1000000000000000000000000
            for k in m.keys():
                mi= min(mi,m[k][0])
            return mi
            
        def deleteFromMap(m,key,index):
            if key in m:
                if index in m[key]:
                    m[key].remove(index)
                    # m[key].sort()
                    if(len(m[key])==0):
                        del m[key]
            return m

        def checkMap(map1,map2):
            if(len(map2.keys())!=len(map1.keys())):
                return False
            #here for this question check map will change and we only need to look for 
            #keys and values of string t to be present in string s
            for k in map1.keys():
                if((k not in map2) or  (len(map2[k])<map1[k])):
                    return False
            return True

        map_t = {}
        for c in t:
            if c in map_t:
                map_t[c]+=1
            else:
                map_t[c]=1

        windowEnd = 0
        windowStart = -1
        min_length = 10000000000000000
        map_s={}
        min_tuple = False

        while windowEnd<len(s):
            c = s[windowEnd]
            if c not in map_t:
                windowEnd+=1
            else:
                if(windowStart==-1):
                    windowStart = windowEnd

                addToMap(map_s,c,windowEnd)
                # print(map_s)
                windowEnd+=1
                
                str_len= windowEnd-windowStart
                if(checkMap(map_t,map_s)):
                    earlierMinLength = min_length
                    min_length = min(min_length,str_len)
                    tup = (windowStart,windowEnd)
                    if(earlierMinLength!=min_length):
                        min_tuple = tup
                    # print("deleting ",windowStart," from map_s for key ",s[windowStart])
                    deleteFromMap(map_s,s[windowStart],windowStart)
                    # print(map_s)                    
                    
                    windowStart = getMinOfMap(map_s)

                    
                    # while(windowStart<windowEnd and s[windowStart] not in map_t):
                    #     windowStart+=1
                    # print("==> seeked window start to ",windowStart)

                    #shrinking the window
                    map_s_copy = map_s.copy()
                    temp_start = windowStart
                    

                    while(temp_start<=windowEnd and (checkMap(map_t,map_s_copy))):
                        str_len = windowEnd-temp_start
                        if(str_len<min_length):
                            min_length = str_len
                            windowStart = temp_start
                            map_s = map_s_copy
                            min_tuple=(temp_start,windowEnd)
                        deleteFromMap(map_s_copy,s[temp_start],temp_start)
                        temp_start = getMinOfMap(map_s_copy)
                        # temp_start+=1
                        # while(temp_start<windowEnd and s[temp_start] not in map_t):
                        #     temp_start+=1
                    

        if(min_tuple):
            return s[min_tuple[0]:min_tuple[1]]        
        else:
            return ""
