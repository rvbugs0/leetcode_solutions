class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i =1
        lastfix = 0
        while(i<len(nums)):
            if(nums[i]==nums[lastfix]):
                i+=1
            else:
                lastfix+=1
                nums[lastfix]=nums[i]
        return lastfix+1
        