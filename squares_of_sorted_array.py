class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        
        new_nums = []
        negatives=-1
        positives= len(nums)
        
        i=0
        while i <len(nums):
            if(nums[i]>=0):
                positives=i
                break
            else:
                negatives+=1
            i+=1
            


        while(negatives>=0 and positives<len(nums)):
            neg_square = nums[negatives]**2
            pos_square = nums[positives]**2
            if(neg_square<=pos_square):
                new_nums.append(neg_square)
                negatives-=1
            else:
                new_nums.append(pos_square)
                positives+=1

        # print(new_nums)
                
        while(negatives>=0):
            neg_square = nums[negatives]**2
            new_nums.append(neg_square)
            negatives-=1

        while(positives<len(nums)):
            pos_square = nums[positives]**2
            new_nums.append(pos_square)
            positives+=1
        
        return new_nums
            
        
        