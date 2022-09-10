class Solution:

    def removeDuplicates(self, nums: List[int]) -> int:
        lastElement = A

        currentIndex=0

        for num in nums:

            if num==lastElement:

                continue

            else:

                nums[currentIndex]=num

                currentIndex+=1

                lastElement = num

        k = currentIndex

        return k

           

                

                

            

        