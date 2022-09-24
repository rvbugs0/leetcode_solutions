class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        def max_subarray(nums,start, end):
            if(start==end): return nums[start]
            if(start>end): return -999999999999999999999999
            mid = start+int((end-start)/2)
          

            left_max = max_subarray(nums,start,mid)
            right_max = max_subarray(nums,mid+1,end)


            #checking max in left subarray
            left_sum = -99999999999999999999999
            right_sum = -99999999999999999999999
            x= mid
            isum=0
            while(x>=start):
                isum+=nums[x]
                left_sum = max(left_sum,isum)
                x-=1     
          
            isum = 0
            x= mid+1
            while(x<=end):
                isum+=nums[x]
                right_sum = max(right_sum,isum)
                x+=1     

          
            ans = max(left_max,right_max)    
            return max(ans,left_sum+right_sum)

   
    
        
        
        
        return max_subarray(nums,0,len(nums)-1)
    
    
    