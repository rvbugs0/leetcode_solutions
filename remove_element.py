class Solution:

    def removeElement(self, nums: List[int], val: int) -> int:

       

        currentIndex=0

        for num in nums:

            if num==val:

                continue

            else:

                nums[currentIndex]= num

                currentIndex+=1

        return currentIndex