def characterReplacement(s,k):

    max_length = k
    maxUnique  = len(set(s))
    
    for currUnique in range(1,maxUnique+1):
        char_map = {}
        windowEnd = 0
        windowStart = 0
        str_length = 0
        while windowEnd<len(s):
            
            if len(char_map.keys())<=currUnique and :
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
            
            if(len(char_map.keys())<=currUnique):
                #we found a subsequence meeting the constraints
                #let's shrink it
                tempEnd =windowEnd
                tempStart = windowStart
                tempMap = char_map.copy()
                #we will shrink temp window from left to see if we can make a string with at most k changes 
                while()

            
            if(currUnique==3):
                
                print("Window start: ",windowStart," WindowEnd: ",windowEnd," Map: ",char_map)
            
            # max_freq = max(char_map.values())
            # if((str_length-max_freq<=k)):
            #     max_length = max(max_length, str_length)
            #     if currUnique==3:
            #         print("Max length for unique ",currUnique," updated to ",max_length)

    
                
    return max_length 
    
a = "EQQEJDOBDPDPFPEIAQLQGDNIRDDGEHJIORMJPKGPLCPDFMIGHJNIIRSDSBRNJNROBALNSHCRFBASTLRMENCCIBJLGAITBFCSMPRO"
print(len(set(a)))
print(characterReplacement(a,2))
            



        