class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        size = len(nums)
        left  = 0
        right = 0
        window_size = 10000000000000000000000
        t_sum = 0
        while(right<size):
            t_sum=t_sum+nums[right]
            while(t_sum>=target ):
                window_size  = min(right-left+1,window_size)
                t_sum = t_sum- nums[left]
                left = left+1
            right+=1
                
        if(window_size!= 10000000000000000000000):
            return window_size 
        return 0
        
        
        
        