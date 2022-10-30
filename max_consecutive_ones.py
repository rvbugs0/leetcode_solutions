class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        windowStart = 0
        windowEnd = 0
        max_length  = 0
        onesCount = 0
        
        while windowEnd<len(nums):
            if(nums[windowEnd]==1):
                onesCount+=1
            
            
            
            #also rem = windowSize - max of map values 
            while((windowEnd - windowStart+1)- onesCount>k):
                cc = nums[windowStart]
                if(cc ==1):
                    onesCount = max(0,onesCount-1)
                windowStart+=1
            
            max_length = max(max_length,(windowEnd - windowStart+1))
            windowEnd+=1
        return max_length

        